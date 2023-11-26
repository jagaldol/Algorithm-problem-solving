#include <iostream>
using namespace std;

#define MAX 1000001

int calculation[MAX];

int numberOfCalculation(int n) {
	calculation[1] = 0;
	
	for (int i = 2; i < n + 1; i++) {
		if (i % 3 == 0 && i % 2 == 0) {
			int leastValue = calculation[i / 3] < calculation[i / 2] ? calculation[i / 3] : calculation[i / 2];
			calculation[i] = leastValue < calculation[i - 1] ? leastValue + 1 : calculation[i - 1] + 1;
		}
		else if (i % 3 == 0) {
			calculation[i] = calculation[i / 3] < calculation[i - 1] ? calculation[i / 3] + 1 : calculation[i - 1] + 1;
		}
			
		else if (i % 2 == 0) {
			calculation[i] = calculation[i / 2] < calculation[i - 1] ? calculation[i / 2] + 1 : calculation[i - 1] + 1;
		}
		else
			calculation[i] = calculation[i - 1] + 1;
	}
	return calculation[n];
}

int main() {
	int N;
	cin >> N;

	cout << numberOfCalculation(N) << '\n';

	return 0;
}