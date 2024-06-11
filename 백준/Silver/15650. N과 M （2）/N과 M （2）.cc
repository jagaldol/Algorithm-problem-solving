#include <iostream>
using namespace std;

int N, M;

bool visited[9] = { 0, };
int ans[9] = { 0, };


void dfs(int index, int cnt) {
	if (cnt == M) {
		for (int i = 0; i < M; i++)
			cout << ans[i] << ' ';
		cout << '\n';
		return;
	}
	for (int i = index; i <= N; i++) {
		if (!visited[i]) {
			visited[i] = true;
			ans[cnt] = i;
			dfs(i + 1, cnt + 1);
			visited[i] = false;
		}
	}
}


int main() {	
	cin >> N >> M;

 	dfs(1, 0);

	return 0;
}