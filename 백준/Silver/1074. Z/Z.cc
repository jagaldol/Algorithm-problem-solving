#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
	int N, r, c;
	cin >> N >> r >> c;

	int nxn = pow(2, N);
	vector<int> v(nxn, 0);

	for (int i = 0; i < nxn; i++) {
		int index = i;
		int quat = 1;
		while (index > 0) {
			if (index % 2 == 1) v[i] += quat;
			index = index >> 1;
			quat *= 4;
		}
	}

	int result = v[r] * 2 + v[c];

	cout << result << '\n';


	return 0;
}