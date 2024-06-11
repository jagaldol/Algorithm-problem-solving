#include <iostream>
#include <queue>
#include <string>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	int N, t;
	string s;
	queue<int> st;

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> s;

		if (s == "push") {
			cin >> t;
			st.push(t);
		}
		else if (s == "pop") {
			if (st.size() != 0) {
				cout << st.front() << '\n';
				st.pop();
			}
			else
				cout << "-1\n";
		}
		else if (s == "size") {
			cout << st.size() << '\n';
		}
		else if (s == "empty") {
			if (st.size() == 0) cout << "1\n";
			else cout << "0\n";
		}
		else if (s == "front") {
			if (st.size() != 0) cout << st.front() << '\n';
			else cout << "-1\n";
		}
		else if (s == "back") {
			if (st.size() != 0) cout << st.back() << '\n';
			else cout << "-1\n";
		}

	}

	return 0;
}