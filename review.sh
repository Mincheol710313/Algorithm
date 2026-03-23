#!/bin/bash

# ─────────────────────────────────────────
# review.sh — 화이트보드 코딩 복습 자동화
# 사용법: ./review.sh <문제_디렉토리_경로>
# 예시:   ./review.sh "Cpp/백준/DFS_BFS/1260_DFS와 BFS"
# ─────────────────────────────────────────

# ── 색상 ──────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

# ── 유틸 ──────────────────────────────────
print_header() { echo -e "\n${BOLD}${CYAN}$1${RESET}"; }
print_ok()     { echo -e "  ${GREEN}✔ $1${RESET}"; }
print_fail()   { echo -e "  ${RED}✘ $1${RESET}"; }
print_info()   { echo -e "  ${YELLOW}▶ $1${RESET}"; }

# ── 인자 확인 ─────────────────────────────
PROBLEM_DIR="${1:-.}"
if [[ ! -d "$PROBLEM_DIR" ]]; then
    echo -e "${RED}오류: 디렉토리를 찾을 수 없습니다 — '$PROBLEM_DIR'${RESET}"
    echo "사용법: ./review.sh \"Cpp/백준/DFS_BFS/1260_DFS와 BFS\""
    exit 1
fi

PROBLEM_DIR="$(realpath "$PROBLEM_DIR")"
ORIGINAL="$PROBLEM_DIR/main.cpp"
PRACTICE="$PROBLEM_DIR/practice.cpp"
PROBLEM_DOC="$PROBLEM_DIR/problem.md"
BINARY="$PROBLEM_DIR/practice_bin"
TESTS_DIR="$PROBLEM_DIR/tests"
README="$PROBLEM_DIR/README.md"

if [[ ! -f "$ORIGINAL" ]]; then
    echo -e "${RED}오류: main.cpp 가 없습니다 — '$ORIGINAL'${RESET}"
    exit 1
fi

# ── 문제 이름 추출 ────────────────────────
PROBLEM_NAME="$(basename "$PROBLEM_DIR")"

# ── practice.cpp 생성 ─────────────────────
print_header "📝 $PROBLEM_NAME — 복습 시작"

cat > "$PRACTICE" << 'EOF'
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // TODO: 풀이 작성

    return 0;
}
EOF
print_info "practice.cpp 생성 완료"

# ── problem.md 생성 (README에서 문제 설명 + 입출력만 추출) ──
if [[ -f "$README" ]]; then
    awk '
        /^## 📝 문제 설명/  { in_section=1 }
        /^## 🧠 풀이 과정/ { in_section=0 }
        in_section          { print }
    ' "$README" > "$PROBLEM_DOC"

    # 앞에 제목 + 링크 줄 붙이기
    HEADER=$(awk 'NR<=4' "$README")
    printf '%s\n\n---\n\n' "$HEADER" | cat - "$PROBLEM_DOC" > /tmp/problem_tmp.md
    mv /tmp/problem_tmp.md "$PROBLEM_DOC"

    print_info "problem.md 생성 완료"
else
    print_info "README.md 없음 — problem.md 생략"
fi

# ── VSCode로 열기 ──────────────────────────
if command -v code &> /dev/null; then
    code "$PROBLEM_DOC" "$PRACTICE"
    print_info "VSCode에서 problem.md + practice.cpp 오픈"
else
    print_info "VSCode 없음 — 직접 파일을 열어주세요: $PRACTICE"
fi

# ── 타이머 시작 ───────────────────────────
print_header "⏱  타이머"
START_TIME=$(date +%s)

# 백그라운드에서 경과 시간 출력
TIMER_PID=""
_timer() {
    while true; do
        sleep 60
        ELAPSED=$(( $(date +%s) - START_TIME ))
        MINS=$(( ELAPSED / 60 ))
        echo -e "  ${YELLOW}⏱  ${MINS}분 경과${RESET}"
    done
}
_timer &
TIMER_PID=$!
trap "kill $TIMER_PID 2>/dev/null" EXIT

echo -e "  풀이를 완성하면 ${BOLD}Enter${RESET}를 누르세요..."
read -r

# 타이머 종료 및 경과 시간 표시
kill $TIMER_PID 2>/dev/null
TIMER_PID=""
END_TIME=$(date +%s)
ELAPSED=$(( END_TIME - START_TIME ))
MINS=$(( ELAPSED / 60 ))
SECS=$(( ELAPSED % 60 ))
print_ok "소요 시간: ${MINS}분 ${SECS}초"

# ── 컴파일 ────────────────────────────────
print_header "🔨 컴파일"
if g++ -std=c++17 -O2 -o "$BINARY" "$PRACTICE" 2>/tmp/review_compile_err; then
    print_ok "컴파일 성공"
else
    print_fail "컴파일 실패"
    echo -e "${RED}"
    cat /tmp/review_compile_err
    echo -e "${RESET}"
    echo -e "  수정 후 다시 실행하세요: ${BOLD}./review.sh \"$1\"${RESET}"
    exit 1
fi

# ── 테스트 실행 ───────────────────────────
print_header "🧪 테스트"

PASS=0
FAIL=0
NO_OUT=0

if [[ -d "$TESTS_DIR" ]]; then
    for IN_FILE in "$TESTS_DIR"/*.in; do
        [[ -f "$IN_FILE" ]] || continue
        TEST_NUM=$(basename "$IN_FILE" .in)
        OUT_FILE="${TESTS_DIR}/${TEST_NUM}.out"

        ACTUAL=$("$BINARY" < "$IN_FILE" 2>/dev/null | sed 's/[[:space:]]*$//')

        if [[ -f "$OUT_FILE" ]]; then
            EXPECTED=$(cat "$OUT_FILE" | sed 's/[[:space:]]*$//')
            if [[ "$ACTUAL" == "$EXPECTED" ]]; then
                print_ok "테스트 $TEST_NUM PASS"
                (( PASS++ ))
            else
                print_fail "테스트 $TEST_NUM FAIL"
                echo -e "    ${YELLOW}예상:${RESET} $(echo "$EXPECTED" | head -3)"
                echo -e "    ${RED}실제:${RESET} $(echo "$ACTUAL" | head -3)"
                (( FAIL++ ))
            fi
        else
            # .out 없으면 출력만 표시
            echo -e "  ${CYAN}테스트 $TEST_NUM 출력:${RESET}"
            echo "$ACTUAL" | sed 's/^/    /'
            (( NO_OUT++ ))
        fi
    done
else
    print_info "tests/ 디렉토리가 없습니다 — 테스트 건너뜀"
fi

# 결과 요약
echo ""
if (( FAIL == 0 && PASS > 0 )); then
    echo -e "  ${GREEN}${BOLD}전체 통과 ✔  ($PASS/$((PASS+FAIL)))${RESET}"
elif (( PASS + FAIL > 0 )); then
    echo -e "  ${RED}${BOLD}일부 실패  ($PASS 통과 / $FAIL 실패)${RESET}"
fi
(( NO_OUT > 0 )) && print_info ".out 없는 테스트 ${NO_OUT}개 — 출력을 직접 확인하세요"

# ── diff 비교 ──────────────────────────────
print_header "📊 원본 비교 (main.cpp vs practice.cpp)"
echo -e "  ${YELLOW}보려면 Enter, 건너뛰려면 q 입력:${RESET} \c"
read -r CHOICE
if [[ "$CHOICE" != "q" && "$CHOICE" != "Q" ]]; then
    diff --color=always -u "$ORIGINAL" "$PRACTICE" | head -80 || true
    echo ""
    print_info "전체 diff: diff \"$ORIGINAL\" \"$PRACTICE\""
fi

# ── 정리 ─────────────────────────────────
rm -f "$BINARY" "$PROBLEM_DOC"
print_header "✅ 완료"
echo -e "  소요 시간: ${BOLD}${MINS}분 ${SECS}초${RESET}"
echo -e "  파일 위치: $PRACTICE"
