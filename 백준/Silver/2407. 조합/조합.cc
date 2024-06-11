#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string Combination(int, int);
string stringAdd(string, string);

int main() {
	long long int N, M;
	cin >> N >> M;
	cout << Combination(N, M) << '\n';

	return 0;
}

string Combination(int n, int m) {
	vector<vector<string>> comb(n + 1, vector<string>(n + 1));
	for (int i = 1; i <= n; i++) {
		comb[i][i] = '1';
		comb[i][0] = '1';
	}
	for (int i = 2; i <= n; i++) {
		for (int j = 1; j < i; j++) {
			comb[i][j] = stringAdd(comb[i - 1][j], comb[i - 1][j - 1]);
		}
	}

	return comb[n][m];
}


string stringAdd(string s1, string s2) {
	string result;
	int sum = 0;
	while(!s1.empty() || !s2.empty() || sum != 0) {
		if (!s1.empty()) {
			sum += s1.back() - '0';
			s1.pop_back();
		}
		if (!s2.empty()) {
			sum += s2.back() - '0';
			s2.pop_back();
		}
		result.push_back(sum % 10 + '0');
		sum /= 10;
	}
	reverse(result.begin(), result.end());
	return result;
}