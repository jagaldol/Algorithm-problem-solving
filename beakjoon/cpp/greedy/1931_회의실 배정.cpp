#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


bool compare(pair<int, int> x, pair<int, int> y) {
	if (x.second == y.second)
		return x.first < y.first;
	return x.second < y.second;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);


	int N;
	cin >> N;
	
	vector<pair<int, int>> time;

	for (int i = 0; i < N; i++) {
		int x, y;
		cin >> x >> y;
		time.push_back(make_pair(x, y));
	}

	sort(time.begin(), time.end(), compare);


	int count = 0;
	int last = 0;

	for (int i = 0; i < N; i++) {
		if (time[i].first >= last) {
			count++;
			last = time[i].second;
		}
	}
	cout << count << '\n';

	return 0;
}