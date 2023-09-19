#include <iostream>
#include <queue>
#include <vector>
#include <set>
using namespace std;


struct compare {
	bool operator() (pair<int, int> x, pair<int, int> y) {
		return x.second < y.second;
	}
};


int N, K;
priority_queue<pair<int, int>, vector<pair<int, int>>, compare> jewelry;
multiset<int> bag;


void input();
void steal();


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	input();
	steal();

	return 0;
}


void input() {
	cin >> N >> K;

	for (int i = 0; i < N; i++) {
		int buf1, buf2;
		cin >> buf1 >> buf2;
		jewelry.push({ buf1, buf2 });
	}

	for (int i = 0; i < K; i++) {
		int buf;
		cin >> buf;
		bag.insert(buf);
	}
}


void steal() {
	long long sum = 0;


	while (!bag.empty() && !jewelry.empty()) {
		int weight = jewelry.top().first;
		int price = jewelry.top().second;
		jewelry.pop();

		multiset<int>::iterator iter = bag.lower_bound(weight);

		if (iter == bag.end()) continue;

		bag.erase(iter);
		sum += price;
	}

	cout << sum << '\n';
}