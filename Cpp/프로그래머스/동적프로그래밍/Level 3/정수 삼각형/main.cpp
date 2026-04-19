#include <string>
#include <vector>
#include <iostream>

using namespace std;

/*
- [프로그래머스] 정수 삼각형
- 분류: 동적프로그래밍
- 난이도: Level 3
- 날짜: 2026.04.19
- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/
*/

// ================================================================
// TODO: solution 함수 시그니처를 문제에 맞게 수정하세요.
// ================================================================

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    int row_len = triangle.size();
    vector<int> col_lens(row_len, 0);
    for (int i = 0; i < row_len; i++) {
        col_lens[i] = i+1;
    }

    vector<vector<int>> dp;
    for (int i = 0; i < row_len; i++) {
        vector<int> in_vec;
        for (int j = 0; j < col_lens[i]; j++) {
            in_vec.push_back(0);
        }
        dp.push_back(in_vec);
    }

    dp[0][0] = triangle[0][0];
    for (int i = 1; i < row_len; i++) {
        for (int j = 0; j < col_lens[i]; j++) {
            if (j == 0) {
                dp[i][j] = dp[i-1][j] + triangle[i][j];
            } else if (j == col_lens[i] - 1) {
                dp[i][j] = dp[i-1][j-1] + triangle[i][j];
            } else {
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j];
            }
        }
    }

    for (int i = 0; i < row_len; i++) {
        answer = max(answer, dp[row_len-1][i]);
    }

    return answer;
}

// ================================================================
// 로컬 테스트용 main (제출 시 solution 함수만 사용됨)
// ================================================================

int main() {
    // TODO: 테스트 케이스 직접 입력
    // 예시:
    // vector<int> v = {1, 2, 3};
    // cout << solution(v) << "\n";
    vector<vector<int>> example = {
        {7}, 
        {3, 8},
        {8, 1, 0}, 
        {2, 7, 4, 4},
        {4, 5, 2, 6, 5}
    };

    cout << solution(example);

    return 0;
}