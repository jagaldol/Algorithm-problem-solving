#include <iostream>
#include <queue>
using namespace std;

int main() {
	bool visited[100001] = { false, };

	int N, K;
	cin >> N >> K;


	int l = 0;

	queue<pair<int, int>> seek;
	seek.push({ N, l });
	visited[N] = true;


	while (true) {
		N = seek.front().first;
		l = seek.front().second;
		seek.pop();

		if (N == K) break;

		if (N > 0 && !visited[N - 1]) {
			seek.push({ N - 1, l + 1 });
			visited[N - 1] = true;
		}
		if (N < 100000 && !visited[N + 1]) {
			seek.push({ N + 1, l + 1 });
			visited[N + 1] = true;
		}
		if (N <= 50000 && !visited[N * 2]) {
			seek.push({ N * 2, l + 1 });
			visited[N * 2] = true;
		}
	}

	cout << l << '\n';


	return 0;
}