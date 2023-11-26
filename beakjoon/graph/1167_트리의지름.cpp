	#include <iostream>
	#include <vector>
	using namespace std;

	int V;
	vector<vector<pair<int, int>>> tree;
	bool visited[100001];
	int best;
	int bestPoint;


	void makeTree();
	void solution();
	void findFarVertex(int v);
	void dfs(int n, int distance);


	int main() {
		ios_base::sync_with_stdio(false);
		cin.tie(NULL); cout.tie(NULL);

		cin >> V;
		makeTree();
		solution();

		return 0;
	}



	void makeTree() {
		tree = vector <vector<pair<int, int>>>(V + 1);

		for (int i = 0; i < V; i++) {
			int v1, v2, cost;
			cin >> v1;
			while (true) {
				cin >> v2;
				if (v2 == -1) break;
				cin >> cost;
				tree[v1].push_back({ v2, cost });
			}	
		}
	}


	void solution() {
		findFarVertex(1);
		findFarVertex(bestPoint);

		cout << best << '\n';
	}


	void findFarVertex(int v) {
		for (int i = 0; i < V; i++)
			visited[i] = false;

		visited[v] = true;
		best = 0;
		dfs(v, 0);
	}


	void dfs(int n, int distance) {

		for (int i = 0; i < tree[n].size(); i++) {
			if (!visited[tree[n][i].first]) {
				visited[tree[n][i].first] = true;
				if (best < distance + tree[n][i].second) {
					best = distance + tree[n][i].second;
					bestPoint = tree[n][i].first;
				}
				dfs(tree[n][i].first, distance + tree[n][i].second);
				visited[tree[n][i].first] = false;
			}
		}
	}