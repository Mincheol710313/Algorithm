#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 4719. 불!
- 분류: DFS_BFS
- 난이도: 골드 3
- 날짜: 2026.04.06
- 링크: https://www.acmicpc.net/problem/4719
*/
int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

int r, c;
int jihun, fire;

vector<vector<char>> grid;
vector<vector<int>> fire_dist;
vector<vector<int>> jihun_dist;

bool inRange(int nr, int nc) {
    return nr >= 0 && nr < r && nc >= 0 && nc < c;
}

bool isExit(int cr, int cc) {
    return cr == 0 || cr == r-1 || cc == 0 || cc == c-1;
}

void fire_bfs() {
    queue<tuple<int,int>> q;
    
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if(grid[i][j] == 'F') {
                fire_dist[i][j] = 0;
                q.push({i, j});
            }
        }
    }

    while (!q.empty()) {
        auto [cur_row, cur_col] = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            int next_row = cur_row + dr[i];
            int next_col = cur_col + dc[i];

            if (inRange(next_row, next_col) && grid[next_row][next_col] != '#' && fire_dist[next_row][next_col] == -1) {
                fire_dist[next_row][next_col] = fire_dist[cur_row][cur_col] + 1;
                q.push({next_row, next_col});
            }
        }
    }
    
}

int jihun_bfs(int row, int col) {
    queue<tuple<int,int>> q;
    jihun_dist[row][col] = 0;
    q.push({row, col});

    while (!q.empty()) {
        auto [cur_row, cur_col] = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            int next_row = cur_row + dr[i];
            int next_col = cur_col + dc[i];

            if (!inRange(next_row, next_col)) {
                return jihun_dist[cur_row][cur_col] + 1; 
            }

            if (grid[next_row][next_col] != '#' && jihun_dist[next_row][next_col] == -1 &&
                (fire_dist[next_row][next_col] == -1 || jihun_dist[cur_row][cur_col] + 1 < fire_dist[next_row][next_col]))
                {
                    jihun_dist[next_row][next_col] = jihun_dist[cur_row][cur_col] + 1;
                    q.push({next_row, next_col});
                }
        }
    }

    return -1;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> r >> c;
    grid.assign(r, vector<char>(c, 0));
    fire_dist.assign(r, vector<int>(c, -1));
    jihun_dist.assign(r, vector<int>(c, -1));

    tuple<int,int> jihun_pos = {0, 0};

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> grid[i][j];
            if (grid[i][j] == 'J') jihun_pos = {i, j};
        }
    }

    // fire bfs
    fire_bfs();

    auto [jr, jc] = jihun_pos;
    int result = jihun_bfs(jr, jc);

    if (result == -1) cout << "IMPOSSIBLE";
    else cout << result;

    return 0;
}