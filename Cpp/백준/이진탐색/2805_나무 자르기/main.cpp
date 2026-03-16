#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
- [백준] 2805. 나무 자르기
- 분류: 이진탐색
- 난이도: 실버 2
- 날짜: 2026.03.16
- 링크: https://www.acmicpc.net/problem/2805
*/
long long sum_height(vector<int>& v, int cut) {
    long long total_height = 0;
    for (int tree : v) {
        if (tree > cut) total_height += tree - cut;
    }
    return total_height;
}

int solution(vector<int>& v, long long target) {
    int start = 0, end = v.back();

    int answer;
    while (start <= end) {
        int mid = (start + end) / 2;
        
        long long total = sum_height(v, mid);
        if (total >= target) {
            answer = mid;
            start = mid +1;
        }
        else end = mid - 1;
    }

    return answer;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    
    int tree_num;
    long long need_height;
    cin >> tree_num >> need_height;

    vector<int> tree_heights;
    for (int i = 0; i < tree_num; i++) {
        int height;
        cin >> height;
        tree_heights.push_back(height);
    }
    
    sort(tree_heights.begin(), tree_heights.end());

    cout << solution(tree_heights, need_height);

    return 0;
}
