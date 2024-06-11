#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;

	int  max = 0;
	int mini = 0;

	if (n >= 1) cin >> max;
	mini = max;

	for (int i = 1; i < n; i++) {
		int temp;
		cin >> temp;
		if (temp < mini) mini = temp;
		if (temp > max) max = temp;
	}

	cout << mini << " " << max << endl;

	return 0;
}