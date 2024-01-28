#include <iostream>
#include <queue>
using namespace std;

bool visited[100001];


int main() {
	int N, K;

	cin >> N >> K;

	queue<pair<int, int>> seek;

	seek.push({ N, 0 });

	int method = 0;
	int best = 1000001;
	while (!seek.empty()) {
		int position = seek.front().first;
		int time = seek.front().second;
		seek.pop();

		visited[position] = true;

		if (best < time)
			break;

		if (position == K) {
			best = time;
			method++;
		}
		if (position + 1 <= 100000 && !visited[position + 1]) {
			seek.push({ position + 1, time + 1 });
		}
		if (position - 1 >= 0 && !visited[position - 1]) {
			seek.push({ position - 1, time + 1 });
		}
		if (position * 2 <= 100000 && !visited[position * 2]) {
			seek.push({ position * 2, time + 1 });
		}
	}
	cout << best << '\n' << method << '\n';
	return 0;
}