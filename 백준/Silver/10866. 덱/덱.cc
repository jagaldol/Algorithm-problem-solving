#include <iostream>
#include <queue>
#include <string>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	int N, t;
	string s;
	deque<int> st;
	
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> s;

		if (s == "push_front") {
			cin >> t;
			st.push_front(t);
		}
		else if (s == "push_back") {
			cin >> t;
			st.push_back(t);
		}
		else if (s == "pop_front") {
			if (st.size() != 0) {
				cout << st.front() << '\n';
				st.pop_front();
			}
			else
				cout << "-1\n";
		}
		else if (s == "pop_back") {
			if (st.size() != 0) {
				cout << st.back() << '\n';
				st.pop_back();
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