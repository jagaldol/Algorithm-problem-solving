#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int arr[100001];


void searchNumber(int n) {
	int left = 0;
	int right = N - 1;
	int index;

	while (left <= right) {
		index = (left + right) / 2;

		if (n == arr[index]) {
			cout << 1 << '\n';
			return;
		}
		else if (n < arr[index])
			right = index - 1;
		else
			left = index + 1;
	}

	cout << 0 << '\n';
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> N;

	for (int i = 0; i < N; i++)
		cin >> arr[i];

	sort(arr, arr + N);

	cin >> M;
	for (int i = 0; i < M; i++) {
		int n;
		cin >> n;
		searchNumber(n);
	}

	return 0;
}