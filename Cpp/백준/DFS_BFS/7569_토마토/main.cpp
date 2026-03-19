#include <bits/stdc++.h>
using namespace std;

using namespace std;

/*
- [백준] 7569. 토마토
- 분류: DFS_BFS
- 난이도: 골드 5
- 날짜: 2026.03.19
- 링크: https://www.acmicpc.net/problem/7569
*/
int dx[] = {1, -1, 0, 0, 0, 0};
int dy[] = {0, 0, 1, -1, 0, 0};
int dz[] = {0, 0, 0, 0, 1, -1};

int width, heigth, depth; // 가로, 세로, 높이
vector<vector<vector<int>>> tomato_box;

bool inRange(int x, int y, int z) {
    return x >= 0 && x < width && y >= 0 && y < heigth && z >= 0 && z < depth;
}

int bfs() {
    queue<tuple<int,int,int>> q;

    for (int i = 0; i < depth; i++) {
        for (int j = 0; j < heigth; j++) {
            for (int k = 0; k < width; k++) {
                if(tomato_box[i][j][k] == 1) q.push({i, j, k});
            }
        }
    }

    while (!q.empty()) {
        auto [z, y, x] = q.front();
        q.pop();
        for (int d = 0; d < 6; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            int nz = z + dz[d];
            if (inRange(nx, ny, nz) && tomato_box[nz][ny][nx] == 0) {
                tomato_box[nz][ny][nx] = tomato_box[z][y][x] + 1;
                q.push({nz, ny, nx});
            }
        }
    }

    int result = 0;
    for (int i = 0; i < depth; i++) {
        for (int j = 0; j < heigth; j++) {
            for (int k = 0; k < width; k++) {
                if (tomato_box[i][j][k] == 0) return -1;
                result = max(result, tomato_box[i][j][k]);
            }
        }
    }

    return result - 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> width >> heigth >> depth;
    tomato_box.assign(depth, vector<vector<int>>(heigth, vector<int>(width, 0)));
    
    for(int i = 0; i < depth; i++) {
        for(int j = 0; j < heigth; j++) {
            for(int k = 0; k < width; k++) cin >> tomato_box[i][j][k];
        }
    }

    cout << bfs() << "\n";

    return 0;
}
