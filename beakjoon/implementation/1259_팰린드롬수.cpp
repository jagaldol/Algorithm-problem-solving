#include <iostream>
#include <stack>

using namespace std;

bool isZero(int n) {
	return n == 0 ? true : false;
}

bool isPalindrome(int n) {
	stack<int> s;
	int num = n;
	int len = 0;
	while (num > 0) {
		s.push(num % 10);
		num /= 10;
		len++;
	}

	for (int i = 0; i < len / 2; i++) {
		if (s.top() != n % 10) {
			return false;
		}
		n /= 10;
		s.pop();
	}
	return true;
}

int main() {
	int n = 0;
	while (true) {
		cin >> n;
		if (isZero(n))
			break;
		if (isPalindrome(n))
			cout << "yes" << '\n';
		else
			cout << "no" << '\n';
	}

	return 0;
}