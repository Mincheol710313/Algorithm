#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 1697. 숨바꼭질
- 분류: DFS_BFS
- 난이도: 실버 1
- 날짜: 2026.03.23
- 링크: https://www.acmicpc.net/problem/1697
*/
#define MAX 100001


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int subin, brother;
    cin >> subin >> brother;

    queue<int> q;
    vector<int> dist(MAX, -1);
    q.push(subin);
    dist[subin] = 0;

    while(!q.empty()) {
        int cur = q.front();
        q.pop();
        if(cur == brother) {
            cout << dist[brother];
            break;
        }
        for(int next : {cur - 1, cur + 1, cur*2}) {
            if(next >= 0 && next < MAX && dist[next] == -1) {
                dist[next] = dist[cur] + 1;
                q.push(next);
            }
        }
    }

    return 0;
}
