#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
vector<bool> visited;
vector<int> path;


void solution();
void sequence(int l);


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> N >> M;
	visited = vector<bool>(N + 1, false);
	path = vector<int>(M, 0);
	
	solution();

	return 0;
}


void solution() {
	for (int i = 1; i <= N; i++) {
		visited[i] = true;
		path[0] = i;
		sequence(1);
		visited[i] = false;
	}
}

void sequence(int l) {
	if (l == M) {
		for (int i = 0; i < M; i++) {
			cout << path[i] << ' ';
		}
		cout << '\n';
		return;
	}
	for (int i = 1; i <= N; i++) {
		if (!visited[i]) {
			visited[i] = true;
			path[l] = i;
			sequence(l + 1);
			visited[i] = false;
		}
	}

}