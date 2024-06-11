#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<int> v;

	while (true) {
		int a, b;
		cin >> a >> b;
		if (cin.eof() == true) break;
		v.push_back(a + b);
	}

	for (int i = 0; i < size(v); i++) {
		cout << v[i] << endl;
	}

	return 0;
}