#include <iostream>
#include <stack>
#include <string>
using namespace std;

string s;

void postfix();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> s;

	postfix();


	return 0;
}


void postfix() {
	int l = s.length();
	stack<char> st;
	char c;

	for (int i = 0; i < l; i++) {
		if (s[i] >= 'A' && s[i] <= 'Z')
			cout << s[i];
		else if (st.empty()) {
			st.push(s[i]);
		}
		else if (s[i] == '(') {
			st.push(s[i]);
		}
		else if (s[i] == '*' || s[i] == '/') {
			while (!st.empty() && (st.top() == '*' || st.top() == '/')) {
				cout << st.top();
				st.pop();
			}
			st.push(s[i]);
		}
		else if (s[i] == '+' || s[i] == '-') {
			while (!st.empty() && st.top() != '(') {
				cout << st.top();
				st.pop();
			}
			st.push(s[i]);
		}
		else if (s[i] == ')') {
			while (!st.empty() && st.top() != '(') {
				cout << st.top();
				st.pop();
			}
			st.pop();
		}
	}

	while (!st.empty()) {
		cout << st.top();
		st.pop();
	}
	cout << '\n';
}