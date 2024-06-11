#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int N;
vector<pair<int, int>> v;

void getCoordinate();
bool compare(pair<int, int> a, pair<int, int> b);
void showCoordinate();
int main() {
	cin >> N;
	
	getCoordinate();
	sort(v.begin(), v.end(), compare);
	showCoordinate();
	return 0;
}

void getCoordinate() {
	for (int i = 0; i < N; i++) {
		pair<int, int> p;
		cin >> p.first >> p.second;
		v.push_back(p);
	}
}

bool compare(pair<int, int> a, pair<int, int> b) {
	if (a.first == b.first) return a.second < b.second;
	return a.first < b.first;
}

void showCoordinate() {
	for (int i = 0; i < N; i++) {
		cout << v[i].first << ' ' << v[i].second << '\n';
	}
}