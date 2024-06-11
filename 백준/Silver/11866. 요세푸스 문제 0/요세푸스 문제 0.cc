#include <iostream>
#include <list>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int N, K;
	cin >> N >> K;
	
	list<int> l;

	for (int i = 1; i <= N; i++)
		l.push_back(i);

	cout << '<' << K;

	list<int>::iterator iter = l.begin();
	for (int i = 0; i < K - 1; i++)
		iter++;

	while (true) {
		list<int>::iterator tmp = iter;

		iter++;
		if (iter == l.end())
			iter = l.begin();

		l.erase(tmp);

		if (l.size() == 0) break;

		for (int i = 0; i < K - 1; i++) {
			iter++;
			if (iter == l.end())
				iter = l.begin();
		}
		cout << ", " << *iter;
	}


	cout << ">\n";
	return 0;
}