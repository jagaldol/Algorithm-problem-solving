#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N, M;
vector<int> v;
vector<bool> visited;
vector<int> ans;
void dfs(int count) {
	if (count == M) {
		for (int i = 0; i < M; i++)
			cout << ans[i] << ' ';
		cout << '\n';
		return;
	}
	for (int i = 0; i < N; i++) {
		if (!visited[i]) {
			visited[i] = true;
			ans[count] = v[i];
			dfs(count + 1);
			visited[i] = false;
		}
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		int t;
		cin >> t;
		v.push_back(t);
	}
	sort(v.begin(), v.end());
	visited = vector<bool>(N, false);
	ans = vector<int>(N);
	dfs(0);

	return 0;
}