#include <iostream>
using namespace std;


#define MOD 1000000007


void multiple(long long A[2][2], long long B[2][2]) {
	long long tmp[2][2];

	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			tmp[i][j] = 0;
			for (int k = 0; k < 2; k++) {
				tmp[i][j] += (A[i][k] * B[k][j]) % MOD;
			}
		}
	}
	
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			A[i][j] = tmp[i][j] % MOD;
		}
	}
}


void fibonacci(long long A[][2], long long origin[][2], long long exp) {
	while (exp > 0) {
		if (exp % 2 == 1) {
			multiple(A, origin);
		}
		multiple(origin, origin);

		exp /= 2;
	}
}




int main() {
	long long N;

	cin >> N;

	long long origin[2][2] = { {1, 1}, {1, 0} };
	long long A[2][2] = { {1, 0}, {0, 1} }; // 초기행렬 I

	fibonacci(A, origin, N);

	cout << A[1][0] << '\n';

	return 0;
}

