#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
	int M, N, t;
	cin >> M >> N;

	vector<vector<int>> box;
	queue<pair<int, int>> ripe;

	for (int i = 0; i < N; i++) {
		vector<int> row;
		for (int j = 0; j < M; j++) {
			cin >> t;
			row.push_back(t);

			if (t == 1) {
				ripe.push({ i, j });
			}
		}
		box.push_back(row);
	}

	int days = -1;

	while (!ripe.empty()) {
		int size = ripe.size();

		for (int i = 0; i < size; i++) {
			int x = ripe.front().first;
			int y = ripe.front().second;
			ripe.pop();

			if (x + 1 < N && box[x + 1][y] == 0) {
				box[x + 1][y] = 1;
				ripe.push({ x + 1, y });
			}
			if (y + 1 < M && box[x][y + 1] == 0) {
				box[x][y + 1] = 1;
				ripe.push({ x, y + 1 });
			}
			if (x - 1 >= 0 && box[x - 1][y] == 0) {
				box[x - 1][y] = 1;
				ripe.push({ x - 1, y });
			}
			if (y - 1 >= 0 && box[x][y - 1] == 0) {
				box[x][y - 1] = 1;
				ripe.push({ x, y - 1 });
			}
		}
		days++;
	}

	bool fail = false;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (box[i][j] == 0) {
				fail = true;
				break;
			}
		}
		if (fail) break;
	}
	if (fail)
		cout << -1 << '\n';
	else
		cout << days << '\n';

	return 0;
}