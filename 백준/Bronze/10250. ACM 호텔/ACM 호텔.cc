#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int it;
	cin >> it;

	for (; it--;) {
		int h, w, n;
		cin >> h >> w >> n;
		
		int floor = n % h;
		if (floor == 0) floor = h;
		int door = (n - 1) / h + 1;
		
		cout << floor * 100 + door << '\n';
	}

	return 0;
}