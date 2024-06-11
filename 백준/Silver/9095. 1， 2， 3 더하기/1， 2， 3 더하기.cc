#include <iostream>
using namespace std;


int factorial(int n) {
	int res = 1;
	while (n > 0) {
		res *= n;
		n--;
	}
	return res;
}

int add123(int n) {
	int res = 0;
	for (int i = 0; i < n/2 + 1; i++) { // i: number of 2
		int r = n - 2 * i;
		for (int j = 0; j < r/3 + 1; j++) {	// j: number of 3
			int ea = n - i - 2 * j;
			res += factorial(ea) / (factorial(ea - i - j) * factorial(i) * factorial(j));
		}
	}
	return res;
}


int main() {
	int T, n;
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		cin >> n;
		cout << add123(n) << '\n';
	}

	return 0;
}