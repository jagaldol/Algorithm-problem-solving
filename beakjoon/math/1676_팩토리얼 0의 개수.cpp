#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;
	
	int two = 0;
	int five = 0;

	for (int i = 1; i <= N; i++) {
		int num = i;
		while (num % 2 == 0) {
			num = num / 2;
			two++;
		}
		while (num % 5 == 0) {
			num = num / 5;
			five++;
		}
	}

	cout << min(two, five) << '\n';
}