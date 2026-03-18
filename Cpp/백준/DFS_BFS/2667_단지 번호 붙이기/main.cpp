#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 2667. 단지 번호 붙이기
- 분류: DFS_BFS
- 난이도: 실버 1
- 날짜: 2026.03.17
- 링크: https://www.acmicpc.net/problem/2667
*/
int length;
vector<vector<int>> grid;

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

bool inRange(int x, int y) {
    return x >= 0 &&  x < length && y >= 0 && y < length;
}

int dfs(int x, int y) {
    grid[x][y] = 0;
    int size = 1;

    for (int d = 0; d < 4; d++){
        int nx = x + dx[d];
        int ny = y + dy[d];
        if(inRange(nx, ny) && grid[nx][ny] == 1) {
            size += dfs(nx, ny);
        }
    }
    return size;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> length;
    grid.assign(length, vector<int>(length));
    
    for(int i = 0; i < length; i++) {
        string s;
        cin >> s;
        for(int j = 0; j < length; j++) grid[i][j] = s[j] - '0'; 
    }

    
    vector<int> size_list;
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < length; j++) {
            if (grid[i][j] == 1) {
                int size = dfs(i, j);
                size_list.push_back(size); 
            }
        }
    }
    
    sort(size_list.begin(), size_list.end());
    cout << size_list.size() << "\n";
    for (int size : size_list) {
        cout << size << "\n";
    }

    return 0;
}