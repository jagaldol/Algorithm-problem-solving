#include <iostream>
#include <string>

using namespace std;
int main() {
	int n;
	
	cin >> n;

	for (int i = 0; i < n; i++) {
		string s;
		int score = 0;
		int tmp = 1;
		cin >> s;
		for (int j = 0; j < s.length(); j++) {
			if (s[j] == 'O') {
				score += tmp;
				tmp++;
			}
			else
				tmp = 1;
		}
		cout << score << endl;
	}

	return 0;
}