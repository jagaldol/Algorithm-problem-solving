#include <iostream>
using namespace std;

int N, K;

struct stuff {
	int weight;
	int price;
};

stuff table[101];
int dp[101][100001];


int main() {
	cin >> N >> K;
	
	for (int i = 0; i < N; i++) {
		cin >> table[i].weight >> table[i].price;
	}

	for (int j = 0; j <= K; j++) {
		if (j - table[0].weight >= 0)
			dp[0][j] = table[0].price;
		else
			dp[0][j] = 0;
	}
		

	for (int i = 1; i < N; i++) {
		for (int j = 1; j <= K; j++) {
			if (j - table[i].weight >= 0)
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - table[i].weight] + table[i].price);
			else
				dp[i][j] = dp[i - 1][j];
		}			
	}

	cout << dp[N - 1][K] << '\n';
	return 0;
}