# include <iostream>
# include <algorithm>
using namespace std;

int best = 10000000;
int n;
int cost[1000][3];
int dp[1000][3];


int DP() {
	dp[0][0] = cost[0][0];
	dp[0][1] = cost[0][1];
	dp[0][2] = cost[0][2];

	for (int i = 1; i < n; i++) {
		dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0];
		dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1];
		dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2];
	}

	int result = dp[n - 1][0];
	for (int i = 1; i < 3; i++)
		if (result > dp[n - 1][i])
			result = dp[n - 1][i];
	
	return result;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> cost[i][0] >> cost[i][1] >> cost[i][2];
	}

	cout << DP() << '\n';

	return 0;
}