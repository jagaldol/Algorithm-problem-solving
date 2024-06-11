#include <iostream>

using namespace std;

int main() {
	int max = 0;
	int tmp = 0;
	int index = 0;

	for (int i = 0; i < 9; i++) {
		cin >> tmp;
		if (max < tmp) {
			max = tmp;
			index = i + 1;
		}
	}
	
	cout << max << endl;
	cout << index << endl;	

	return 0;
}