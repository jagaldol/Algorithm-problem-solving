#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int n;
	vector<int> cost;

	cin >> n;

	cost.push_back(1);
	cost.push_back(2);

	for (int i = 2; i < n; i++) {
		int nextCost = cost[i - 1] + cost[i - 2];
		nextCost %= 10007;
		cost.push_back(nextCost);
	}

	cout << cost[n - 1] << '\n';

	return 0;
}