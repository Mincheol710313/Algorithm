#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 2606. 바이러스
- 분류: DFS_BFS
- 난이도: 실버 3
- 날짜: 2026.04.03
- 링크: https://www.acmicpc.net/problem/2606
*/
int computer, edge;
vector<vector<int>> graph;
vector<bool> visited;

void dfs(int cur_node) {
    visited[cur_node] = true;

    for(int node : graph[cur_node]) {
        if(!visited[node]) dfs(node);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> computer;
    cin >> edge;
    graph.assign(computer+1, vector<int>(0));
    visited.assign(computer+1, false);
    
    for (int i = 0; i < edge; i++) {
        int first, second;
        cin >> first >> second;

        graph[first].push_back(second);
        graph[second].push_back(first);
    }

    dfs(1);

    int count = 0;
    for (int i = 2; i <= computer; i++) {
        if(visited[i]) count++;
    }

    cout << count;

    return 0;
}
