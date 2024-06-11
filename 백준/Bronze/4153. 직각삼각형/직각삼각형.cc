#include <iostream>

using namespace std;

int main() {

	while (true) {
		int a[3];
		cin >> a[0] >> a[1] >> a[2];
		if (a[0] == a[1] && a[1] == a[2] && a[2] == 0)
			break;

		if (a[0] > a[1]) {
			int tmp = a[0];
			a[0] = a[1];
			a[1] = tmp;
		}
		if (a[1] > a[2]) {
			int tmp = a[1];
			a[1] = a[2];
			a[2] = tmp;
		}

		if (a[2] * a[2] == a[0] * a[0] + a[1] * a[1])
			cout << "right" << endl;
		else
			cout << "wrong" << endl;
	}

	return 0;
}