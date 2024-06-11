#include <iostream>

using namespace std;
int main() {
	int n;
	int chk = 0;

	for (int i = 0; i < 8; i++) {
		cin >> n;
		if (n == i + 1) chk++;
		else if (n == 8 - i) chk--;
	}

	cout << (chk == 8 ? "ascending" : (chk == -8 ? "descending" : "mixed") ) << endl;

	return 0;
}