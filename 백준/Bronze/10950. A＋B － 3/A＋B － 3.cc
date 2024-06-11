#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n;
	cin >> n;

	vector<int> v;

	for (int i = 0; i < n; i++) {
		int a, b;
		cin >> a >> b;
		v.push_back(a + b);
	}

	for (int i = 0; i < n; i++) {
		cout << v[i] << endl;
	}

	return 0;
}