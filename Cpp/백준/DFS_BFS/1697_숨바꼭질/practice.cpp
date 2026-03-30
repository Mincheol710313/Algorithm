#include <bits/stdc++.h>
using namespace std;

#define MAX 100001

int subin, target;
vector<int> dist;

int bfs() {
    queue<int> q;
    q.push(subin);

    dist[subin] = 0;

    while (!q.empty()) {
        int cur_pos = q.front();
        q.pop();

        for(int next_pos : {cur_pos-1, cur_pos+1, cur_pos*2}) {
            if (next_pos >= 0 && next_pos < MAX) {
                if (next_pos == target) {
                    dist[target] = dist[cur_pos] + 1;
                    return dist[target];
                }
                else if (dist[next_pos] == -1) {
                    dist[next_pos] = dist[cur_pos] + 1;
                    q.push(next_pos);
                }
            }
        }
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // TODO: 풀이 작성
    cin >> subin >> target;
    dist.assign(MAX, -1);

    cout << bfs();

    return 0;
}
