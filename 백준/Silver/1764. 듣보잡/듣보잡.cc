#include <iostream>
#include <set>
#include <string>
using namespace std;

int main() {
	int N, M, count = 0;

	cin >> N >> M;

	set<string> list, finalList;

	for (int i = 0; i < N; i++) {
		string p;
		cin >> p;
		list.insert(p);
	}
	
	for (int i = 0; i < M; i++) {
		string p;
		cin >> p;
		if (list.find(p) != list.end()) {
			count++;
			finalList.insert(p);
		}
	}

	cout << count << '\n';
	for (set<string>::iterator iter = finalList.begin(); iter != finalList.end(); iter++) {
		cout << *iter << '\n';
	}


	return 0;
}