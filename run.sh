#!/bin/bash

# ============================================================
# Test Runner
# 사용법: ./run.sh <문제폴더경로>
#         또는 VS Code 태스크로 실행 (현재 파일 기준 자동)
# ============================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

DIR="${1:-.}"

MAIN="${DIR}/main.cpp"
BINARY="${DIR}/solution"
TESTS_DIR="${DIR}/tests"

# ── 컴파일 ─────────────────────────────────────────────────

echo ""
echo -e "${BOLD}${CYAN}[ 컴파일 ]${NC}"
g++ -g -o "$BINARY" "$MAIN"
if [ $? -ne 0 ]; then
  echo -e "${RED}❌ 컴파일 실패${NC}"
  exit 1
fi
echo -e "${GREEN}✅ 컴파일 성공${NC}"

# ── 테스트 케이스 확인 ──────────────────────────────────────

if [ ! -d "$TESTS_DIR" ] || [ -z "$(ls "${TESTS_DIR}"/*.in 2>/dev/null)" ]; then
  echo -e "${YELLOW}⚠️  테스트 케이스 없음 (tests/*.in)${NC}"
  exit 0
fi

# ── 테스트 실행 ─────────────────────────────────────────────

echo ""
echo -e "${BOLD}${CYAN}[ 테스트 ]${NC}"

PASS=0
FAIL=0

for in_file in "${TESTS_DIR}"/*.in; do
  num=$(basename "$in_file" .in)
  out_file="${TESTS_DIR}/${num}.out"

  actual=$("$BINARY" < "$in_file" 2>/dev/null)

  if [ ! -f "$out_file" ] || [ ! -s "$out_file" ]; then
    echo -e "${YELLOW}⚠️  케이스 ${num}: 예상 출력 없음 → 실행 결과:${NC}"
    echo "$actual"
    continue
  fi

  expected=$(cat "$out_file")

  if [ "$actual" = "$expected" ]; then
    echo -e "${GREEN}✅ 케이스 ${num}: PASS${NC}"
    ((PASS++))
  else
    echo -e "${RED}❌ 케이스 ${num}: FAIL${NC}"
    echo -e "   기댓값: ${YELLOW}${expected}${NC}"
    echo -e "   실제값: ${RED}${actual}${NC}"
    ((FAIL++))
  fi
done

# ── 결과 요약 ───────────────────────────────────────────────

echo ""
TOTAL=$((PASS + FAIL))
if [ $FAIL -eq 0 ]; then
  echo -e "${BOLD}${GREEN}🎉 ${PASS}/${TOTAL} 통과${NC}"
else
  echo -e "${BOLD}${RED}😢 ${PASS}/${TOTAL} 통과${NC}"
fi
echo ""
