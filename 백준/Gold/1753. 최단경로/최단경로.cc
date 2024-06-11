#include <iostream>
#include <queue>
using namespace std;

#define INF 200000000

int V, E;
int root;
vector<vector<pair<int, int>>> graph;
vector<bool> visited;
vector<int> length;


void shortpath();


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> V >> E;
	cin >> root;

	graph = vector<vector<pair<int, int>>>(V + 1);
	visited = vector<bool>(V + 1, false);
	length = vector<int>(V + 1, INF);

	for (int i = 0; i < E; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		graph[u].push_back({ w, v });
	}

	shortpath();

	return 0;
}


void shortpath() {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

	pq.push({ 0, root });
	length[root] = 0;

	while (!pq.empty()) {
		int w = pq.top().first;
		int v = pq.top().second;
		pq.pop();
		

		for (int i = 0; i < graph[v].size(); i++) {
			int cost = graph[v][i].first + w;
			int adj_v = graph[v][i].second;
			if (!visited[adj_v]) {
				if (cost < length[adj_v]) {
					length[adj_v] = cost;
					pq.push({ cost, adj_v });
				}
			}
		}
		visited[v] = true;
	}

	for (int i = 1; i <= V; i++) {
		if (length[i] == INF)
			cout << "INF\n";
		else
			cout << length[i] << '\n';
	}
}
