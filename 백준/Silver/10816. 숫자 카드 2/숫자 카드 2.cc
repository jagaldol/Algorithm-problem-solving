#include <iostream>
#include <map>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int n, m, t;
	map<int, int> card;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> t;
		if (card.find(t) != card.end())
			card[t]++;
		else
			card[t] = 1;
	}
	
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> t;
		if (card.find(t) != card.end())
			cout << card[t] << ' ';
		else
			cout << "0 ";
	}
	cout << '\n';
	return 0;
}