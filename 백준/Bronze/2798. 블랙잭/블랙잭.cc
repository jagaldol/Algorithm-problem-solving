#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n, m;
	cin >> n >> m;

	vector<int> card;

	for (int i = 0; i < n; i++) {
		int t;
		cin >> t;
		card.push_back(t);
	}
	sort(card.begin(), card.end());

	int topSum = 0;

	for (int i = 0; i < n - 2; i++) {
		for (int j = i + 1; j < n - 1; j++) {
			for (int k = j + 1; k < n; k++) {
				int sum = card[i] + card[j] + card[k];
				if (sum > m)
					break;
				if (sum > topSum)
					topSum = sum;
			}
		}
	}

	cout << topSum << endl;

	return 0;
}