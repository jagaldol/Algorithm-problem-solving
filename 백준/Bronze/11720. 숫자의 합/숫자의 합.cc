#include <iostream>
#include <string>
using namespace std;
int main() {
	int n;
	string num;
	int sum = 0;

	cin >> n;
	cin >> num;

	for (; n--;) {
		sum += num[n] - '0';
	}
	cout << sum << endl;

	return 0;
}