#include <iostream>
#include <set>
#include <string>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int M, t;
	set<int> s;

	cin >> M;

	for (int i = 0; i < M; i++) {
		string state;
		cin >> state;
		if (state == "add") {
			cin >> t;
			s.insert(t);
		}
		if (state == "remove") {
			cin >> t;
			s.erase(t);
		}
		if (state == "check") {
			cin >> t;
			if (s.find(t) != s.end())
				cout << "1\n";
			else
				cout << "0\n";
		}
		if (state == "toggle") {
			cin >> t;
			if (s.find(t) != s.end())
				s.erase(t);
			else
				s.insert(t);
		}
		if (state == "all") {
			for (int i = 1; i <= 20; i++)
				s.insert(i);
		}
		if (state == "empty") {
			s.clear();
		}
	}


	return 0;
}