#include <iostream>
#include <vector>
using namespace std;

int N;
int result = 0;
int map[15][15];
vector<int> queen;

void nQueen();
void dfs(int depth);


int main() {
	cin >> N;

	nQueen();

	return 0;
}


void nQueen() {
	dfs(0);
	
	cout << result << '\n';
}


void dfs(int depth) {
	if (depth == N) {
		result++;
		return;
	}
	for (int col = 0; col < N; col++) {
		bool pushFlag = true;
		for (int i = 0; i < queen.size(); i++) {
			int sub = abs(col - queen[i]);
			if (col == queen[i] || sub == depth - i) {
				pushFlag = false;
				goto EXIT;
			}

		}
	EXIT:
		if (pushFlag) {
			queen.push_back(col);
			dfs(depth + 1);
			queen.pop_back();
		}
	}
}

bool check(int i, int j) {
	for (int index = 0; index < queen.size(); index++) {
		int sub = abs(j - queen[i]);
		if (j == queen[i] || sub == i - index) {
			return false;
		}
	}
	return true;
}