#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {

	int n;
	cin >> n;

	vector<pair<int, int>> building;

	for (int i = 0; i < n; i++) {
		int x, h, r;
		cin >> x >> h >> r;
		building.push_back({ x, h });
		building.push_back({ r, -h });
	}

	sort(building.begin(), building.end());
	building.push_back({ 2000000001,1000000001 });

	multiset<int> S;

	S.insert(0);

	int prev_x = building[0].first;
	int prev_v = -1;
	int i = 0;
	while (i < 2 * n) {
		while (prev_x == building[i].first) {
			int v = building[i].second;
			if (v < 0) S.erase(S.find(-v));
			else S.insert(v);
			i++;
		}
		int val = *prev(S.end());
		if (val != prev_v) {
			cout << prev_x << ' ' << val << ' ';
			prev_v = val;
		}
		prev_x = building[i].first;
	}
}