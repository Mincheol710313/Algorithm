#include <bits/stdc++.h>
using namespace std;

#define MAX 100001

int subin, brother;
vector<int> dist;

void bfs() {
    queue<int> q;
    q.push(subin);
    dist[subin] = 0;

    while (!q.empty()) {
        int cur_pos = q.front(); 
        q.pop();

        if (cur_pos == brother) {
            cout << dist[brother];
            break;
        }
        
        for (int next : {cur_pos - 1, cur_pos + 1, cur_pos * 2}) {
            if(next >= 0 && next < MAX && dist[next] == -1) {
                dist[next] = dist[cur_pos] + 1;
                q.push(next);
            }
        }

    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // TODO: 풀이 작성
    cin >> subin >> brother;
    dist.assign(MAX, -1);

    bfs();

    return 0;
}
