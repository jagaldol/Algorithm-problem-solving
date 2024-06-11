#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string s1, s2;
int dp[1001][1001];

void LCS();


int main() {
	cin >> s1 >> s2;
	LCS();

	return 0;
}


void LCS() {
	int length1 = s1.length();
	int length2 = s2.length();

	for (int i = 0; i < length1; i++) {
		dp[i][0] = 0;
	}
	for (int j = 0; j < length2; j++) {
		dp[0][j] = 0;
	}


	for (int i = 1; i <= length1; i++) {
		for (int j = 1; j <= length2; j++) {
			if (s1[i-1] == s2[j-1]) dp[i][j] = dp[i - 1][j - 1] + 1;
			else
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
		}
	}

	cout << dp[length1][length2] << '\n';
}