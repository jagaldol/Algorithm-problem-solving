#include <iostream>
using namespace std;


class maxHeap {
private:
	int heap[100002];
	int size = 0;

	void swap(int &a, int &b) {
		a ^= b ^= a ^= b;
	}

public:
	void push(int n) {
		size++;
		heap[size] = n;

		int child = size;

		while (child > 1) {
			int parent = child / 2;
			if (heap[child] > heap[parent]) {
				swap(heap[child], heap[parent]);
				child = parent;
			}
			else
				break;
		}
	}

	int pop() {
		int ret = heap[1];

		swap(heap[1], heap[size]);
		size--;

		int parent = 1;
		
		while (true) {
			int child = 2 * parent;
			
			if (child > size) break;

			if (child < size) {
				if (heap[child] < heap[child + 1]) {
					child++;
				}
			}
			if (heap[child] > heap[parent]) {
				swap(heap[child], heap[parent]);
				parent = child;
			}
			else
				break;
		}

		return ret;
	}

	int getSize() {
		return size;
	}
};


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);


	int N, t;
	cin >> N;

	maxHeap heap;

	for (int i = 0; i < N; i++) {
		cin >> t;
		if (t == 0) {
			if (heap.getSize() == 0)
				cout << "0\n";
			else {
				cout << heap.pop() << '\n';
			}
		}
		else
			heap.push(t);
	}

	return 0;
}