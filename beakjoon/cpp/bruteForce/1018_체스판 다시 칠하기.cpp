#include <iostream>
char chess[50][50];
int calculate(int _i, int _j);
using namespace std;

int main() {
	int m, n;
	cin >> m >> n;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			cin >> chess[i][j];
		}
	}

	int min = 64;
	for (int i = 0; i < m - 7; i++) {
		for (int j = 0; j < n - 7; j++) {
			int tmp = calculate(i, j);
			tmp = tmp < 64 - tmp ? tmp : 64 - tmp;
			min = min < tmp ? min : tmp;
		}
	}
	cout << min << '\n';
}

int calculate(int _i, int _j) {
	int count = 0;
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			char color = (i + j) % 2 == 0 ? 'B' : 'W';
			if (chess[_i + i][_j + j] != color)
				count++;
		}
	}
	return count;
}
