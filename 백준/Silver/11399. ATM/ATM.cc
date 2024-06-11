#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int N, t;
	vector<int> time;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> t;
		time.push_back(t);
	}
	sort(time.begin(), time.end());

	int result = 0;
	for (int i = 0; i < N; i++) {
		result += time[i] * (N - i);
	}

	cout << result << '\n';

	return 0;
}