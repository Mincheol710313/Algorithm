#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*
- [백준] 2750. 수 정렬하기
- 분류: 정렬
- 난이도: 브론즈 2
- 날짜: 2026.03.12
- 링크: https://www.acmicpc.net/problem/2750
*/

void bubbleSort(vector<int>& v, int& size) {
    for (int i = 0; i < size-1; i++) {
        for(int j = 0; j < size -1 -i; j++) {
            if(v[j] > v[j+1]) swap(v[j], v[j+1]);
        }
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N;
    cin >> N;

    vector<int> num_v;
    
    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;

        num_v.push_back(num);
    }

    // Sorting
    bubbleSort(num_v, N);

    for (int i = 0; i < N; i++) {
        cout << num_v[i] << "\n";
    }

return 0;
}
