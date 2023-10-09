#include <iostream>
#include <vector>
using namespace std;


int N;
vector<vector<pair<int, int>>> tree;
bool visited[10001];
int best;
int bestPoint;


void diameter();
void dfs(int n, int distance);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N;
	tree = vector<vector<pair<int, int>>>(N + 1);


	for (int i = 1; i < N; i++) {
		int parent, child, weight;
		cin >> parent >> child >> weight;
		tree[parent].push_back({ child, weight });
		tree[child].push_back({ parent, weight });
	}

	diameter();

	return 0;
}


void diameter() {
	best = 0;
	bestPoint = 0;
	for (int i = 1; i <= N; i++)
		visited[i] = false;
	visited[1] = true;
	dfs(1, 0);

	best = 0;

	for (int i = 1; i <= N; i++)
		visited[i] = false;
	visited[bestPoint] = true;
	dfs(bestPoint, 0);

	cout << best << '\n';
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