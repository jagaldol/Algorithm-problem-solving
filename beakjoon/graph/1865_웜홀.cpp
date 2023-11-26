#include <iostream>
#include <vector>
using namespace std;

struct edge {
	int s;
	int e;
	int t;
};

int N, M, W;
vector<edge> edges;


void input();
void solution();


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int TC;
	cin >> TC;

	for (; TC--;) {
		input();
		solution();
	}

	return 0;
}


void input() {
	edges.clear();
	cin >> N >> M >> W;

	for (int i = 0; i < M; i++) {
		int S, E, T;
		cin >> S >> E >> T;
		edges.push_back({ S, E, T });
		edges.push_back({ E, S, T });
	}

	for (int i = 0; i < W; i++) {
		int S, E, T;
		cin >> S >> E >> T;
		edges.push_back({ S, E, -T });
	}
}


void solution() {
	vector<int> distance(N + 1);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < edges.size(); j++) {
			int s = edges[j].s;
			int e = edges[j].e;
			int t = edges[j].t;
			if (distance[s] + t < distance[e]) {
				distance[e] = distance[s] + t;
				if (i == N - 1) {
					cout << "YES\n";
					return;
				}
			}
		}
	}

	cout << "NO\n";
}