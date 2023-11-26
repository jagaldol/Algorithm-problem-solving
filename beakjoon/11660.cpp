#include <iostream>
using namespace std;

int N, M;
int table[1025][1025];
int dp[1025][1025];


void input();
void makeDP();
void solution();
void sectionSum(int, int, int, int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	input();
	makeDP();
	solution();

	return 0;
}

void input() {
	cin >> N >> M;

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> table[i][j];
		}
	}
}


void makeDP() {
	for (int i = 0; i <= N; i++) {
		dp[i][0] = 0;
		dp[0][i] = 0;
	}

	for (int i = 1; i <= N; i++) {
		dp[i][1] = table[i][1];
	}

	for (int i = 1; i <= N; i++) {
		for (int j = 2; j <= N; j++) {
			dp[i][j] = dp[i][j - 1] + table[i][j];
		}
	}

	for (int i = 2; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			dp[i][j] += dp[i - 1][j];
		}
	}
}

void solution() {
	int x1, y1, x2, y2;
	
	for (int i = 0; i < M; i++) {
		cin >> x1 >> y1 >> x2 >> y2;
		sectionSum(x1, y1, x2, y2);
	}
}


void sectionSum(int x1, int y1, int x2, int y2) {
	int result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1];
	cout << result << '\n';
}