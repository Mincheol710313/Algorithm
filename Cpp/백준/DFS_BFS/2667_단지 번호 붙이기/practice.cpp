#include <bits/stdc++.h>
using namespace std;
int dx[] = {-1, 1, 0, 0};
int dy[] = { 0,0, -1, 1};

int length;
vector<vector<int>> graph;

bool inRange(int next_x, int next_y) {
    return next_x >= 0 && next_x < length && next_y >= 0 && next_y < length;
}

int dfs(int x, int y) {
    int total = 1;
    graph[x][y] = 0;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(inRange(nx, ny) && graph[nx][ny] == 1) total += dfs(nx, ny);
    }

    return total;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // TODO: 풀이 작성
    cin >> length;
    graph.assign(length, vector<int>(length, 0));

    for (int i = 0; i < length; i++) {
        string nums;
        cin >> nums;
        for (int j = 0; j < length; j++) {
            graph[i][j] = nums[j] - '0';
        }
    }

    vector<int> apt_nums;
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < length; j++) {
            if(graph[i][j] == 1) {
                apt_nums.push_back(dfs(i, j));
            }
        }
    }

    sort(apt_nums.begin(), apt_nums.end());
    
    cout << apt_nums.size() << "\n";
    for (int apt_num : apt_nums) {
        cout << apt_num << "\n";
    }

    return 0;
}
