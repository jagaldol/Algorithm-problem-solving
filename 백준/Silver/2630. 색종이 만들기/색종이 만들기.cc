#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> square;
int white = 0, blue = 0;


void splitWhiteBlue(int x, int y, int l) {
	int color = square[x][y];
	for (int i = x; i < x + l; i++) {
		for (int j = y; j < y + l; j++) {
			if (square[i][j] != color) {
				splitWhiteBlue(x, y, l / 2);
				splitWhiteBlue(x + l / 2, y, l / 2);
				splitWhiteBlue(x, y + l / 2, l / 2);
				splitWhiteBlue(x + l / 2, y + l / 2, l / 2);
				return;
			}
		}
	}
	if (color == 1) blue++;
	else white++;

}


int main() {
	

	int N, t;

	cin >> N;
	
	for (int i = 0; i < N; i++) {
		vector<int> row;
		for (int j = 0; j < N; j++) {
			cin >> t;
			row.push_back(t);
		}
		square.push_back(row);
	}

	splitWhiteBlue(0, 0, N);

	cout << white << '\n' << blue << '\n';
		
	


	return 0;
}