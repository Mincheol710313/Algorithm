#include <bits/stdc++.h>
using namespace std;

int dx[] = {-1, 1, 0, 0, 0, 0};
int dy[] = {0, 0, -1, 1, 0, 0};
int dz[] = {0, 0, 0, 0, -1, 1};

int x, y, z;
vector<vector<vector<int>>> grid;

bool inRange(int nz, int ny, int nx) {
    return nx >= 0 && nx < x && ny >= 0 && ny < y && nz >= 0 && nz < z;
}

int bfs() {
    queue<tuple<int, int, int>> q;

    for (int i = 0; i < z; i++) {
        for (int j = 0; j < y; j++) {
            for (int k = 0; k < x; k++) {
                if (grid[i][j][k] == 1) q.push({i, j, k});
            }
        }
    }

    while (!q.empty()) {
        auto [cur_z, cur_y, cur_x] = q.front(); q.pop();
        
        for (int i = 0; i < 6; i++) {
            int next_z = cur_z + dz[i];
            int next_y = cur_y + dy[i];
            int next_x = cur_x + dx[i];

            if (inRange(next_z, next_y, next_x) && grid[next_z][next_y][next_x] == 0) {
                grid[next_z][next_y][next_x] = grid[cur_z][cur_y][cur_x] + 1;
                q.push({next_z, next_y, next_x});
            }
        }
    }

    int result = 0;
    for (int i = 0; i < z; i++) {
        for (int j = 0; j < y; j++) {
            for (int k = 0; k < x; k++) {
                if (grid[i][j][k] == 0) return -1;
                else {
                    result = max(result, grid[i][j][k]);
                }
            }
        }
    }

    return result - 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // TODO: 풀이 작성
    cin >> x >> y >> z;
    grid.assign(z, vector<vector<int>>(y, vector<int>(x, 0)));

    for (int i = 0; i < z; i++) {
        for (int j = 0; j < y; j++) {
            for (int k = 0; k < x; k++) {
                cin >> grid[i][j][k];
            }
        }
    }

    cout << bfs() << "\n";

    return 0;
}
