#include <iostream>
#include <string>
using namespace std;

int main() {
	string s;
	cin >> s;
	int index[26];
	for (int i = 0; i < 26; i++)
		index[i] = -1;

	for (int i = s.length() - 1; i >= 0; i--) {
		index[s[i] - 'a'] = i;
	}

	for (int i = 0; i < 26; i++) {
		cout << index[i] << ' ';
	}
	cout << '\n';
	return 0;
}