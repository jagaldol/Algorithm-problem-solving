#include <iostream>
#include <queue>
using namespace std;

struct position {
	int x;
	int y;
	int crush;
};

int N, M;
int map[1002][1002];
int visited[1002][1002][2];

int xMove[4] = { 1, -1, 0, 0 };
int yMove[4] = { 0, 0, 1, -1 };


int bfs();


int main() {
	cin >> N >> M;

	for (int i = 0; i < N + 2; i++) {
		map[i][0] = -1;
		map[i][M + 1] = -1;
	}

	for (int i = 0; i < M + 2; i++) {
		map[0][i] = -1;
		map[N + 1][i] = -1;
	}

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			char c;
			cin >> c;
			map[i][j] = c - '0';
		}
	}

	cout << bfs();

	return 0;
}


int bfs() {

	queue<position> move;

	position zero = { 1, 1, 0 };
	move.push(zero);
	visited[1][1][0] = 1;

	while (!move.empty()) {
		position p = move.front();
		move.pop();

		int x = p.x;
		int y = p.y;
		int crush = p.crush;

		if (x == N && y == M) return visited[x][y][crush];

		for (int i = 0; i < 4; i++) {
			position next;
			next.x = x + xMove[i];
			next.y = y + yMove[i];
			next.crush = crush;

			if (map[next.x][next.y] == -1) continue;

			if (visited[next.x][next.y][next.crush]) continue;

			if (map[next.x][next.y] == 0) {
				visited[next.x][next.y][next.crush] = visited[x][y][crush] + 1;
				move.push({ next });
			}
			else if (next.crush == 0) {
				next.crush = 1;
				visited[next.x][next.y][next.crush] = visited[x][y][crush] + 1;
				move.push({ next });
			}
		}
	}
	return -1;
}
