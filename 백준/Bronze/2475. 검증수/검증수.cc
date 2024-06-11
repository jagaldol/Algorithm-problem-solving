#include <iostream>
using namespace std;

int main() {
	int n;
	int result = 0;

	for (int i = 0; i < 5; i++) {
		cin >> n;
		result += n * n;
	}
	cout << result % 10 << '\n';

	return 0;
}