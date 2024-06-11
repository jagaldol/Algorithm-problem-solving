#include <iostream>
using namespace std;

long long a, b, c;

int func(long long n) {
	if (n == 1) return a % c;

	long long k = func(n / 2) % c;

	if (n % 2 == 0) return k * k % c;
	return k * k % c * a % c;
}


int main() {
	cin >> a >> b >> c;

	
	cout << func(b) << '\n';

	return 0;
}