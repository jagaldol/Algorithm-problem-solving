#include <iostream>
using namespace std;

void swap(int &a, int &b) {
	int temp = a;
	a = b;
	b = temp;
}

void makeHeap(int *arr, int n) {
	for (int i = 1; i < n; i++) {
		int child = i;
		while (child > 0) {
			int root = (child - 1) / 2;
			if (arr[root] < arr[child]) {
				swap(arr[root], arr[child]);
			}
			child = root;
		}
	}
}

void downHeap(int* arr, int n) {
	int root = 0;
	int child;
	while (2 * root + 2 < n) {
		int left = 2 * root + 1;
		int right = 2 * root + 2;

		if (arr[left] < arr[right])
			child = right;
		else
			child = left;

		if (arr[child] < arr[root])
			break;
		swap(arr[root], arr[child]);
		root = child;
	}
	child = 2 * root + 1;
	if (child < n && arr[child] > arr[root])
		swap(arr[root], arr[child]);
}

void heapSort(int* arr, int n) {
	makeHeap(arr, n);
	for (int i = n - 1; i > 0; i--) {
		swap(arr[0], arr[i]);
		downHeap(arr, i);
	}
	
}

int main() {
	int n;
	cin >> n;
	int *arr = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	heapSort(arr, n);
	for (int i = 0; i < n; i++) {
		cout << arr[i] << '\n';
	}

	delete arr;
	return 0;
}