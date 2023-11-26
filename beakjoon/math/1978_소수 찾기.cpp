#include <iostream>
using namespace std;
bool* primeArray;

void eratos(int n) {
	if (n <= 1) return;

	primeArray = new bool[n + 1];

	for (int i = 2; i <= n; i++) {
		primeArray[i] = true;
	}

	for (int i = 2; i <= n; i++) {
		if (primeArray[i] == true) {
			for (int j = i * i; j <= n; j += i) {
				primeArray[j] = false;
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	eratos(1000);

	int n, t, ans = 0;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> t;
		if (primeArray[t] == true)
			ans++;
	}
	cout << ans << '\n';

	delete primeArray;
	
	return 0;
}