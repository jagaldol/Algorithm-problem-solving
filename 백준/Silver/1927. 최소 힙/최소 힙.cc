#include <iostream>
using namespace std;



class heap {
private:
	int heap[100002];
	int heap_size = 0;
	void swap(int& a, int& b) {
		a ^= b ^= a ^= b;
	}

public:
	void push(int n) {
		heap_size++;
		heap[heap_size] = n;

		int child = heap_size;
		while (child > 0) {
			int parent = child / 2;
			if (heap[parent] > heap[child]) {
				swap(heap[parent], heap[child]);
				child = parent;
			}
			else
				break;
		}
	}

	int pop() {
		int ret = heap[1];

		swap(heap[1], heap[heap_size]);
		heap_size--;

		int parent = 1;
		while (true) {
			int child = parent * 2;
			
			if (child > heap_size) break;
			
			if (child < heap_size) {
				if (heap[child] > heap[child + 1])
					child = child + 1;
			}
			
			if (heap[parent] > heap[child]) {
				swap(heap[parent], heap[child]);
				parent = child;
			}
			else
				break;
				
		}

		return ret;
	}

	bool empty() {
		if (heap_size == 0)
			return true;
		else
			return false;
	}

};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	heap h;

	int N, t;

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> t;
		if (t == 0) {
			if (h.empty())
				cout << "0\n";
			else
				cout << h.pop() << '\n';
		}
		else
			h.push(t);
	}



	return 0;
}