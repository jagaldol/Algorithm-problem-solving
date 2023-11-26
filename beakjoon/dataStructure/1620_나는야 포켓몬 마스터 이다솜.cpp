#include <iostream>
#include <cstdlib>
#include <string>
#include <map>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);

	map <string, int> m1;
	map <int, string> m2;
	int n, m;
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		string name;
		cin >> name;
		m1.insert(make_pair(name, i+1));
		m2.insert(make_pair(i+1, name));
	}

	for (int i = 0; i < m; i++) {
		char problem[21];
		cin >> problem;
		if (problem[0] < 'A') {
			int num = atoi(problem);
            cout << m2[num] << '\n';
		}
		else {
			cout << m1[problem] << '\n';
		}
	}

	return 0;
}
