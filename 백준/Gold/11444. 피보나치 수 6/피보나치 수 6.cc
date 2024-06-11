#include <iostream>
using namespace std;


#define MOD 1000000007


void multi(long long A[2][2], long long B[2][2]) {
	long long tmp[2][2];

	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			long long temp = 0;
			for (int k = 0; k < 2; k++) {
				temp += ((A[i][k] * B[k][j]) % MOD);
			}
			tmp[i][j] = temp % MOD;
		}
	}
	
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			A[i][j] = tmp[i][j];
		}
	}
}


int main() {
	long long N;

	cin >> N;

	long long origin[2][2] = {1, 1,1, 0};
	long long A[2][2] = {1, 0,0, 1}; // 초기행렬 I

	while (N > 0) {
		if (N % 2 == 1) {
			multi(A, origin);
		}
		multi(origin, origin);

		N /= 2;
	}


	cout << A[1][0] << '\n';

	return 0;
}

