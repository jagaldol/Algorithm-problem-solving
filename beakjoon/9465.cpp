#include <iostream>
#include <vector>
using namespace std;

void sticker(int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int T;
	cin >> T;

	for (; T--;) {
		int n;
		cin >> n;
		sticker(n);
	}


	return 0;
}


void sticker(int n) {
	int stick[100001][2];
	int dp[100001][2];

	int t;
	for (int j = 0; j < 2; j++) {
		for (int i = 0; i < n; i++) {
			cin >> t;
			stick[i][j] = t;
		}
	}

	dp[0][0] = stick[0][0];
	dp[0][1] = stick[0][1];
	dp[1][0] = stick[1][0] + stick[0][1];
	dp[1][1] = stick[1][1] + stick[0][0];
	for (int i = 2; i < n; i++) {
		dp[i][0] = max(dp[i - 2][1], dp[i - 1][1]) + stick[i][0];
		dp[i][1] = max(dp[i - 2][0], dp[i - 1][0]) + stick[i][1];
		
	}

	cout << max(dp[n -1][0], dp[n - 1][1]) << '\n';
}