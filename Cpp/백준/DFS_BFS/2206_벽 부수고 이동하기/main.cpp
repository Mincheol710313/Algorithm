#include <bits/stdc++.h>
using namespace std;

using namespace std;

/*
- [백준] 2206. 벽 부수고 이동하기
- 분류: DFS_BFS
- 난이도: 골드 3
- 날짜: 2026.03.20
- 링크: https://www.acmicpc.net/problem/2206
*/
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int row, column;
vector<vector<int>> graph;
vector<vector<vector<int>>> dist;

bool inRange(int x, int y) {
    return x >= 0 && x < column && y >= 0 && y < row;
}

int bfs() {
    queue<tuple<int, int, int>> q;
    dist[0][0][0] = 1;
    q.push({0, 0, 0});

    while (!q.empty()) {
        auto [y, x, broke] = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (!inRange(nx, ny)) continue;

            if (broke == 0) { // 벽을 부수지 않은 경우
                if (graph[ny][nx] == 0 && dist[ny][nx][0] == -1) { 
                    dist[ny][nx][0] = dist[y][x][0] + 1;
                    q.push({ny, nx, 0});
                } else if (graph[ny][nx] == 1 && dist[ny][nx][0] == -1) { // 그 다음 칸이 벽인 경우
                    dist[ny][nx][1] = dist[y][x][0] + 1;
                    q.push({ny, nx, 1}); 
                }
            } else { // 벽을 부순 경우
                if (graph[ny][nx] == 0 && dist[ny][nx][1] == -1) {
                    dist[ny][nx][1] = dist[y][x][1] + 1;
                    q.push({ny, nx, 1});
                }
            }
        }
    }

    int ans = -1;
    for (int i = 0; i < 2; i++) {
        if(dist[row-1][column-1][i] != -1) {
            if (ans == -1) ans = dist[row-1][column-1][i];
            else ans = min(ans, dist[row-1][column-1][i]);
        }
    }

    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> row >> column;
    graph.assign(row, vector<int>(column));
    dist.assign(row, vector<vector<int>>(column, vector<int>(2, -1))); // 벽을 부수지 않은 경우의 dist와 벽을 부수고 났을 때의 dist

    for (int i = 0; i < row; i ++) {
        string nums;
        cin >> nums;
        for (int j = 0; j < column; j++) graph[i][j] = nums[j] - '0';
    }

    cout << bfs() << "\n";

    return 0;
}
