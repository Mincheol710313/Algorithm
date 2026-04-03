#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 7576. 토마토(2D)
- 분류: DFS_BFS
- 난이도: 골드 5
- 날짜: 2026.04.03
- 링크: https://www.acmicpc.net/problem/7576
*/
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int y, x;
vector<vector<int>> grid;

bool inRange(int ny, int nx) {
    return ny >= 0 && ny < y && nx >= 0 && nx < x;
}

int bfs() {
    queue<tuple<int, int>> q;

    for (int i = 0; i < y; i++) {
        for (int j = 0; j < x; j++) {
            if (grid[i][j] == 1) q.push({i,j});
        }
    }

    while(!q.empty()) {
        auto [cy, cx] = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            int ny = cy + dy[i];
            int nx = cx + dx[i];

            if (inRange(ny,nx) && grid[ny][nx] == 0) {
                grid[ny][nx] = grid[cy][cx] + 1;
                q.push({ny, nx});
            }
        }
    }

    int result = -1;
    for (int i = 0; i < y; i++) {
        for (int j = 0; j < x; j++) {
            if (grid[i][j] == 0) return -1;
            else if (grid[i][j] == -1) continue;
            else {
                if(result == -1) result = grid[i][j];
                else result = max(result, grid[i][j]);
            }
        }
    }
    
    return result-1;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> x >> y;
    grid.assign(y, vector<int>(x, 0));

    for (int i = 0; i < y; i++) {
        for(int j = 0; j < x; j++) {
            cin >> grid[i][j];
        }
    }

    cout << bfs();

    return 0;
}
