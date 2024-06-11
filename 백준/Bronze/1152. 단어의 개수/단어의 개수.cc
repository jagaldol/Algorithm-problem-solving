#include <iostream>
#include <string>

using namespace std;

int main() {
	string s;
	int cnt = 0;

	getline(cin, s);

	int i = 1;
	while (s[i] != NULL) {
		if (s[i] == ' ') cnt++;
		i++;
	}
	if (s[i - 1] != ' ') cnt++;

	cout << cnt;


	return 0;
}