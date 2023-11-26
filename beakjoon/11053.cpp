#include <iostream>
#include <vector>
using namespace std;


int DP(int N) {
	vector<int> dpTable;

	int t;
	cin >> t;

	dpTable.push_back(t);
	int size = 1;
	
	for (int i = 1; i < N; i++) {
		cin >> t;
		
		int j;
		for (j = 0; j < size; j++) {
			if (dpTable[j] >= t) {
				dpTable[j] = t;
				break;
			}
		}
		if (j == size) {
			dpTable.push_back(t);
			size++;
		}
		
	}

	return size;
}


int main() {
	int N;
	cin >> N;
	cout << DP(N) << '\n';
	
	return 0;
}