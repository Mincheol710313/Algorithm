#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
- [백준] 2751. 수 정렬하기 2
- 분류: 정렬
- 난이도: 실버 5
- 날짜: 2026.03.13
- 링크: https://www.acmicpc.net/problem/2751
*/

void bubble_sort(vector<int>& v, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size - 1 -i; j++) {
            if (v[j] > v[j+1]) swap(v[j], v[j+1]);
        }
    }
}

void quick_sort(vector<int>& v, int start, int end) {
    if (start >= end) return;
    int pivot = start;
    int left = start + 1;
    int right = end;

    while (left <= right) {
        while (left <= end && v[left] <= v[pivot]) left += 1;
        while (right > start && v[right] >= v[pivot]) right -= 1;
        
        if(left > right) {
            swap(v[right], v[pivot]);
        } else {
            swap(v[right], v[left]);
        }
    }

    quick_sort(v, start, right-1);
    quick_sort(v, right+1, end);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;

    vector<int> v;

    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;

        v.push_back(num);
    }

    // bubble_sort(v, N);
    // quick_sort(v, 0, N-1);
    sort(v.begin(), v.end());

    for (int i = 0; i < N; i++) {
        cout << v[i] << "\n";
    }

    return 0;
}
