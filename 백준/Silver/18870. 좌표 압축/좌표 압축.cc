#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	vector<pair<int, int>> v;
	int N, t;

	cin >> N;
	
	vector<int> ans(N);

	for (int i = 0; i < N; i++) {
		cin >> t;
		v.push_back({t, i});
	}

	sort(v.begin(), v.end());

	int rank = 0;
	for (int i = 0; i < N; i++) {
		if (i > 0 && v[i].first != v[i - 1].first) rank++;
		ans[v[i].second] = rank;
	}

	for (int i = 0; i < N; i++) {
		cout <<ans[i] << ' ';
	}

	return 0;
}