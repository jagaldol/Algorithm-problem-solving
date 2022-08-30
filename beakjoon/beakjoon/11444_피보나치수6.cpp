#include <iostream>
#include <string>
using namespace std;

long long N;
long long origin[2][2] = { {1, 1}, {1, 0} };


long long** multiple(long long[2][2], long long[2][2]) {

}


long long** fibonacci(long long** A, int exp) {
	if (exp <= 1)
		return A;

	long long[2][2] ret = fibonacci(A, exp / 2);

	ret = multiple(ret, ret);

	if (exp % 2 == 1) {
		ret = multiple(ret, origin);
	}
}




int main() {
	cin >> N;

	fibonacci();

	return 0;
}

