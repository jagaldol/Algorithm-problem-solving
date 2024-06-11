#include <iostream>
using namespace std;
int N, X;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N >> X;

	for (; N--;) {
		int t;
		cin >> t;
		if (t < X)
			cout << t << ' ';
	}
	return 0;
}