#include <bits/stdc++.h>
using namespace std;
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int x, y;
vector<vector<int>> grid;
vector<vector<vector<int>>> dist;

bool inRange(int ny, int nx) {
    return ny >= 0 && ny < y && nx >= 0 && nx < x;
}

int bfs() {
    int result = -1;

    dist[0][0][0] = 1;
    queue<tuple<int, int, int>> q;
    q.push({0,0,0});

    while (!q.empty()) {
        auto [cur_y, cur_x, broke] = q.front(); 
        q.pop();

        for (int i = 0; i < 4; i++) {
            int next_y = cur_y + dy[i];
            int next_x = cur_x + dx[i];

            if (!inRange(next_y, next_x)) {
                continue;
            }
            
            if (broke == 0) {
                if (grid[next_y][next_x] == 0 && dist[next_y][next_x][0] == -1) {
                    dist[next_y][next_x][0] = dist[cur_y][cur_x][0] + 1;
                    q.push({next_y, next_x, 0});
                } else if (grid[next_y][next_x] == 1 && dist[next_y][next_x][1] == -1) {
                    dist[next_y][next_x][1] = dist[cur_y][cur_x][0] + 1;
                    q.push({next_y, next_x, 1});
                }
            } else {
                if (grid[next_y][next_x] == 0 && dist[next_y][next_x][1] == -1) {
                    dist[next_y][next_x][1] = dist[cur_y][cur_x][1] + 1;
                    q.push({next_y, next_x, 1});
                }
            }
        }
    }

    for (int i = 0; i < 2; i++) {
        if(dist[y-1][x-1][i] != -1) {
            if(result == -1) result = dist[y-1][x-1][i];
            else result = min(result, dist[y-1][x-1][i]);
        }
    }
    
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // TODO: 풀이 작성
    cin >> y >> x;
    grid.assign(y, vector<int>(x));
    dist.assign(y, vector<vector<int>>(x, vector<int>(2, -1)));

    for (int i = 0; i < y; i++) {
        string nums;
        cin >> nums;
        for (int j = 0; j < x; j++) {
            grid[i][j] = nums[j] - '0';
        }
    }

    cout << bfs() << "\n";

    return 0;
}
