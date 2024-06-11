#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;


void DP() {
	vector<int> *dp = new vector<int>[N];
	int t;
	cin >> t;
	dp[0].push_back(t);
	for (int i = 1; i < N; i++) {
		for (int j = 0; j <= i; j++) {
			int t;
			cin >> t;
			if (j == 0)
				dp[i].push_back(t + dp[i - 1][0]);
			else if (j == i)
				dp[i].push_back(t + dp[i - 1][j - 1]);
			else
				dp[i].push_back(t + max(dp[i - 1][j - 1], dp[i - 1][j]));
		}
	}

	int result = dp[N - 1][0];
	for (int i = 1; i < N; i++)
		if (result < dp[N - 1][i])
			result = dp[N - 1][i];

	cout << result << '\n';
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N;

	DP();

	return 0;
}