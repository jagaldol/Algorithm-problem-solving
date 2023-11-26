#include <iostream>
#include <vector>
using namespace std;


int N;
vector<vector<int>> relation;
vector<int> tree;
vector<bool> visited;


void dfs(int position) {
	int size = relation[position].size();

	for (int i = 0; i < size; i++) {
		int node = relation[position][i];
		if (!visited[node]) {
			visited[node] = true;
			tree[node] = position;
			dfs(node);
		}
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N;
	relation = vector<vector<int>>(N + 1);
	tree = vector<int>(N + 1);
	visited = vector<bool>(N + 1, false);

	for (int i = 0; i < N - 1; i++) {
		int node1, node2;
		cin >> node1 >> node2;
		relation[node1].push_back(node2);
		relation[node2].push_back(node1);
	}
	visited[1] = true;
	dfs(1);

	for (int i = 2; i <= N; i++) {
		cout << tree[i] << '\n';
	}

	return 0;
}