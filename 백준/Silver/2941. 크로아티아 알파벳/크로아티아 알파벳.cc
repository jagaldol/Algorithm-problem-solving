#include <iostream>
#include <string>
using namespace std;

int main() {
	string s;
	cin >> s;

	int index = 1;
	int result = s.length();

	while (index < s.length()) {
		if (s[index] == '=') {
			if (index - 2 >= 0 && s[index - 2] == 'd' && s[index - 1] == 'z')
				result -= 2;
			else if (s[index - 1] == 'c' || s[index -1] == 's' || s[index - 1] == 'z')
				result--;
		}
		else if (s[index] == '-') {
			if (s[index - 1] == 'c' || s[index - 1] == 'd')
				result--;
		}
		else if (s[index] == 'j') {
				if (s[index - 1] == 'l' || s[index - 1] == 'n')
					result--;
		}

		index++;
	}

	cout << result << '\n';

	return 0;
}