
# [백준] 2667. 단지 번호 붙이기

> 🔗 [문제 링크](https://www.acmicpc.net/problem/2667) | 📁 분류: `DFS_BFS` | ⭐ 난이도: `실버 1`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 2028 KB |
|실행 시간| 0 ms |
|제출 일자|2026.03.17|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요
```text
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
```

### 입력
```text
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```

### 출력
```text
3
7
8
9
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

> 문제를 보고 처음에 어떻게 생각했는지 서술 (틀린 접근도 OK)

2D 격자에서 연결된 집의 묶음을 찾아야 하니 DFS로 연결 요소를 탐색하려고 했다.

### 2. 핵심 아이디어

> 문제를 푸는 핵심 발상이 무엇인지

* `visited` 배열 대신 방문한 칸을 `0`으로 변경해 재방문을 막았다.
* DFS가 반환값으로 덩어리 크기를 누적해서 반환하도록 설계했다.
* 결과를 `sort`로 오름차순 정렬 후 출력했다.

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(N²)` - 모든 칸을 한 번씩 방문하면서 `dfs`를 진행하기 때문이다.
- 공간 복잡도: `O(N²)` - grid 저장

-----

## 💻 최종 코드

```cpp
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
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차| False| 단지 크기를 **오름차순으로 정렬**하지 않고 출력|
|2차| Success| `sort` 추가|

-----

## 💡 배운 점 & 다음에 써먹을 패턴

- `visited` 배열 없이 grid 값을 직접 `0`으로 바꿔 방문 처리할 수 있다.
- DFS에서 크기를 반환값으로 누적하면 별도 전역 변수 없이 덩어리 크기를 셀 수 있다.
- 전역 변수로 `n`, `grid`를 선언하면 `inRange`, `dfs` 같은 함수에 매개변수를 넘기지 않아도 된다.
