#!/bin/bash

# ============================================================

# Algorithm Problem Folder Generator

# 사용법: ./create_problem.sh

# ============================================================

# ── 색상 설정 ──────────────────────────────────────────────

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

echo ""
echo -e "${BOLD}${CYAN}========================================${NC}"
echo -e "${BOLD}${CYAN}   Algorithm Problem Folder Generator   ${NC}"
echo -e "${BOLD}${CYAN}========================================${NC}"
echo ""

# ── 1. 플랫폼 선택 ─────────────────────────────────────────

echo -e "${YELLOW}[1] 플랫폼을 선택하세요:${NC}"
echo "    1) 백준 (Baekjoon)"
echo "    2) 프로그래머스 (Programmers)"
echo ""
read -p "    선택 (1/2): " PLATFORM_CHOICE

case $PLATFORM_CHOICE in
1)
PLATFORM="백준"
PLATFORM_EN="Baekjoon"
;;
2)
PLATFORM="프로그래머스"
PLATFORM_EN="Programmers"
;;
*)
echo -e "${RED}❌ 잘못된 선택입니다.${NC}"
exit 1
;;
esac

# ── 2. 알고리즘 유형 선택 ──────────────────────────────────

echo ""
echo -e "${YELLOW}[2] 알고리즘 유형을 선택하세요:${NC}"
echo "    1) 자료구조 (DataStructure)"
echo "    2) 정렬 (Sort)"
echo "    3) 이진탐색 (BinarySearch)"
echo "    4) DFS_BFS"
echo "    5) 그리디 (Greedy)"
echo "    6) 동적프로그래밍 (DP)"
echo "    7) 구현 (Implementation)"
echo "    8) 기타 직접입력"
echo ""
read -p "    선택 (1~8): " TYPE_CHOICE

case $TYPE_CHOICE in
1) CATEGORY="자료구조" ;;
2) CATEGORY="정렬" ;;
3) CATEGORY="이진탐색" ;;
4) CATEGORY="DFS_BFS" ;;
5) CATEGORY="그리디" ;;
6) CATEGORY="동적프로그래밍" ;;
7) CATEGORY="구현" ;;
8)
read -p "    유형 이름 입력: " CATEGORY
;;
*)
echo -e "${RED}❌ 잘못된 선택입니다.${NC}"
exit 1
;;
esac

# ── 3. 문제 정보 입력 ──────────────────────────────────────

echo ""
echo -e "${YELLOW}[3] 문제 정보를 입력하세요:${NC}"
echo ""

if [ "$PLATFORM_EN" == "Baekjoon" ]; then
read -p "    문제 번호 (예: 1260): " PROBLEM_NUM
read -p "    문제 이름 (예: DFS와BFS): " PROBLEM_NAME
FOLDER_NAME="${PROBLEM_NUM}_${PROBLEM_NAME}"
PROBLEM_LINK="https://www.acmicpc.net/problem/${PROBLEM_NUM}"
DISPLAY_NAME="[백준] ${PROBLEM_NUM}. ${PROBLEM_NAME}"
else
read -p "    문제 이름 (예: 완주하지_못한_선수): " PROBLEM_NAME
read -p "    레벨 (예: Level1): " LEVEL
FOLDER_NAME="${PROBLEM_NAME}"
PROBLEM_LINK="https://school.programmers.co.kr/learn/courses/30/lessons/"
DISPLAY_NAME="[프로그래머스] ${PROBLEM_NAME}"
fi

read -p "    난이도 (예: Silver III / Level 1): " DIFFICULTY
TODAY=$(date +"%Y.%m.%d")

# ── 4. 경로 설정 ───────────────────────────────────────────

# 스크립트 위치 기준으로 경로 설정

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ "$PLATFORM_EN" == "Baekjoon" ]; then
TARGET_DIR="${SCRIPT_DIR}/Cpp/백준/${CATEGORY}/${FOLDER_NAME}"
else
TARGET_DIR="${SCRIPT_DIR}/Cpp/프로그래머스/${LEVEL}/${FOLDER_NAME}"
fi

# ── 5. 폴더 & 파일 생성 ────────────────────────────────────

echo ""
echo -e "${BLUE}📁 생성 경로: ${TARGET_DIR}${NC}"
echo ""

# 이미 존재하는 경우 확인

if [ -d "$TARGET_DIR" ]; then
echo -e "${RED}⚠️  이미 존재하는 폴더입니다. 덮어쓰시겠습니까? (y/n): ${NC}"
read -p "    " OVERWRITE
if [ "$OVERWRITE" != "y" ]; then
echo -e "${YELLOW}취소되었습니다.${NC}"
exit 0
fi
fi

mkdir -p "$TARGET_DIR"

# ── main.cpp 생성 ──────────────────────────────────────────

export DISPLAY_NAME CATEGORY DIFFICULTY TODAY PROBLEM_LINK

envsubst '${DISPLAY_NAME}${CATEGORY}${DIFFICULTY}${TODAY}${PROBLEM_LINK}' \
  < "${SCRIPT_DIR}/templates/main.cpp.tpl" \
  > "${TARGET_DIR}/main.cpp"

# ── README.md 생성 ─────────────────────────────────────────

envsubst '${DISPLAY_NAME}${CATEGORY}${DIFFICULTY}${TODAY}${PROBLEM_LINK}' \
  < "${SCRIPT_DIR}/templates/README.md.tpl" \
  > "${TARGET_DIR}/README.md"

# ── tests/ 생성 ────────────────────────────────────────────

mkdir -p "${TARGET_DIR}/tests"
touch "${TARGET_DIR}/tests/1.in"
touch "${TARGET_DIR}/tests/1.out"

# ── 완료 메시지 ────────────────────────────────────────────

echo -e "${GREEN}✅ 생성 완료!${NC}"
echo ""
echo -e "    📄 ${CYAN}main.cpp${NC}      → C++ 풀이 템플릿"
echo -e "    📄 ${CYAN}README.md${NC}     → 풀이 기록 템플릿"
echo -e "    📁 ${CYAN}tests/1.in${NC}    → 테스트 입력"
echo -e "    📁 ${CYAN}tests/1.out${NC}   → 예상 출력"
echo ""
echo -e "${BOLD}${GREEN}========================================${NC}"
echo -e "${BOLD}${GREEN}  Happy Coding! 🚀  ${TODAY}${NC}"
echo -e "${BOLD}${GREEN}========================================${NC}"
echo ""

code "${TARGET_DIR}/main.cpp"