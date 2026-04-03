#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 2178. 미로 탐색
- 분류: DFS_BFS
- 난이도: 실버 1
- 날짜: 2026.04.03
- 링크: https://www.acmicpc.net/problem/2178
*/
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int y, x ;
vector<vector<int>> grid;
vector<vector<int>> dist;

bool inRange(int ny, int nx) {
    return ny >= 0 && ny < y && nx >= 0 && nx < x;
}

int bfs() {
    queue<tuple<int,int>> q;

    dist[0][0] = 1;
    q.push({0,0});

    while (!q.empty()) {
        auto [cur_y, cur_x] = q.front(); q.pop();
        
        for (int i = 0; i < 4; i++) {
            int ny = cur_y + dy[i];
            int nx = cur_x + dx[i];

            if(inRange(ny, nx) && grid[ny][nx] == 1 && dist[ny][nx] == 0) {
                dist[ny][nx] = dist[cur_y][cur_x] + 1;
                q.push({ny,nx});
            }
        }
    }

    return dist[y-1][x-1];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> y >> x;
    grid.assign(y, vector<int>(x, 0));
    dist.assign(y, vector<int>(x, 0));

    for (int i = 0; i < y; i++) {
        string nums;
        cin >> nums;
        for(int j = 0; j < x; j++) { 
            grid[i][j] = nums[j] - '0';
        }
    }

    cout << bfs();

    return 0;
}
