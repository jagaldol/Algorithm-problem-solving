#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int n, r, a, b, infectedNumber = 0;

	cin >> n >> r;
	
	vector<vector<int>> net(n + 1);
	vector<int> computer(n + 1);
	queue<int> infect;

	for (int i = 0; i < r; i++) {
		cin >> a >> b;
		net[a].push_back(b);
		net[b].push_back(a);
	}

	infect.push(1);
	computer[1] = 1; // 감염

	while (true) {
		if (infect.size() == 0) break;

		int virus = infect.front();
		infect.pop();
		for (int i = 0; i < net[virus].size(); i++) {
			if (computer[net[virus][i]] == 0) {
				infect.push(net[virus][i]);
				computer[net[virus][i]] = 1;
			}
		}
	}
	
	for (int i = 1; i <= n; i++)
		if (computer[i] == 1)
			infectedNumber++;

	cout << infectedNumber - 1 << '\n';

	return 0;
}