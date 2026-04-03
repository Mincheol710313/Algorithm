#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 1012. 유기농 배추
- 분류: DFS_BFS
- 난이도: 실버 2
- 날짜: 2026.04.03
- 링크: https://www.acmicpc.net/problem/1012
*/
int dy[] = {-1, 1, 0, 0};
int dx[] = {0, 0, -1, 1};

int y, x;

vector<vector<int>> grid;

bool inRange(int ny, int nx) {
    return ny >= 0 && ny < y && nx >= 0 && nx < x;
}

void dfs(int cy, int cx) {
    grid[cy][cx] = 0;

    for (int i = 0; i < 4; i++) {
        int ny = cy + dy[i];
        int nx = cx + dx[i];

        if(inRange(ny, nx) && grid[ny][nx]) {
            dfs(ny, nx);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int k;
        cin >> x >> y >> k;
        grid.assign(y, vector<int>(x, 0));

        for (int j = 0; j < k; j++) {
            int ix, iy;
            cin >> ix >> iy;
            grid[iy][ix] = 1;
        }

        int count = 0;
        for (int j = 0; j < y; j++) {
            for (int l = 0; l < x; l++) {
                if(grid[j][l] == 1) {
                    dfs(j, l);
                    count++;
                }
            }
        }

        cout << count;
        if(i != T-1) {
            cout << "\n";
        }
    }

    return 0;
}
