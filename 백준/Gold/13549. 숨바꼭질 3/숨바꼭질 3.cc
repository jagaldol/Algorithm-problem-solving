#include <iostream>
#include <queue>
using namespace std;
int N, K;
bool visited[100001] = { false, };

int main() {

	cin >> N >> K;

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> seek;

	seek.push({ 0, N });
	visited[N] = true;

	while (true) {
		int l = seek.top().first;
		int n = seek.top().second;
		seek.pop();

		if (n == K) {
			cout << l << '\n';
			break;
		}

		if (n <= 50000 && !visited[n * 2]) {
			seek.push({ l, 2 * n });
			visited[n * 2] = true;
		}

		if (n > 0 && !visited[n - 1]) {
			seek.push({ l + 1, n - 1 });
			visited[n - 1] = true;
		}
		if (n < 100000 && !visited[n + 1]) {
			seek.push({ l + 1, n + 1 });
			visited[n + 1] = true;
		}
	}


	return 0;
}