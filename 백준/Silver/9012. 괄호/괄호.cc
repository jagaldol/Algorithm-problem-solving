#include <iostream>
#include <stack>
using namespace std;

bool vps(string s) {
	stack<int> ps;
	ps.push(0);
	for (int i = 0; i < s.length(); i++) {
		if (ps.size() == 0) return false;
		if (s[i] == '(') ps.push(1);
		if (s[i] == ')') ps.pop();
	}
	if (ps.size() == 1) return true;
	else return false;
}

int main() {
	ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		if (vps(s) == true)
			cout << "YES" << '\n';
		else
			cout << "NO" << '\n';
	}

	return 0;
}