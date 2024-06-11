#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int worm(int M, int N, int K);
void releaseWorm(int x, int y, int M, int N, vector<vector<int>> &earth);


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int T, M, N, K;

	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> M >> N >> K;
		cout << worm(M, N, K) << '\n';
	}


	return 0;
}


int worm(int M, int N, int K) {
	vector<vector<int>> earth(M, vector<int>(N, 0));
	int worm = 0;
	int x, y;

	for (int i = 0; i < K; i++) {
		cin >> x >> y;
		earth[x][y] = 1;
	}

	x = y = 0;
	while (true) {
		if (x == M) break;

		if (earth[x][y] == 1) {
			releaseWorm(x, y, M, N, earth);
			worm++;
		}

		y++;
		if (y == N) {
			y = 0;
			x++;
		}
	}

	return worm;

}


void releaseWorm(int x, int y, int M, int N, vector<vector<int>> &earth) {
	stack<pair<int, int>> s;

	earth[x][y] = 0;
	s.push(make_pair(x, y));
	
	while (true) {
		if (x + 1 < M && earth[x + 1][y] == 1) {
			earth[x + 1][y] = 0;
			x = x + 1;
			s.push(make_pair(x, y));
		}
		else if (y + 1 < N && earth[x][y + 1] == 1) {
			earth[x][y + 1] = 0;
			y = y + 1;
			s.push(make_pair(x, y));
		}
		else if (x - 1 > -1 && earth[x - 1][y] == 1) {
			earth[x - 1][y] = 0;
			x = x - 1;
			s.push(make_pair(x, y));
		}
		else if (y - 1 > -1 && earth[x][y - 1] == 1) {
			earth[x][y - 1] = 0;
			y = y - 1;
			s.push(make_pair(x, y));
		}
		else {
			s.pop();
			if (s.size() == 0) break;

			x = s.top().first;
			y = s.top().second;
		}
	}
}