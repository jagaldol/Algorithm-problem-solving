#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;


priority_queue<long long> maxPq;
priority_queue<long long> minPq;
priority_queue<long long> maxDeleted;
priority_queue<long long> minDeleted;
int Size = 0;

void dualPriority();
void ins(long long);
void del(int);
void clean();
void clear(priority_queue<long long>&);
void showResult();


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int T;

	cin >> T;

	for (; T--;)
		dualPriority();

	return 0;
}


void dualPriority() {
	clear(maxPq);
	clear(minPq);
	clear(maxDeleted);
	clear(minDeleted);
	Size = 0;

	int K, num;
	char command;
	cin >> K;

	for (; K--;) {
		cin >> command >> num;

		if (command == 'I') {
			ins(num);
		}
		else if (command == 'D') {
			del(num);
		}
	}

	showResult();

}

void ins(long long num) {
	Size++;
	maxPq.push(num);
	minPq.push(-num);
}

void del(int num) {
	if (Size == 0)
		return;
	Size--;
	clean();
	if (num == 1) {
		maxDeleted.push(-maxPq.top());
		maxPq.pop();
	}
	if (num == -1) {
		minDeleted.push(-minPq.top());
		minPq.pop();
	}
}


void clean() {
	while (!minDeleted.empty() && !maxPq.empty() && minDeleted.top() == maxPq.top()) {
		minDeleted.pop();
		maxPq.pop();
	}
	while (!maxDeleted.empty() && !minPq.empty() && maxDeleted.top() == minPq.top()) {
		maxDeleted.pop();
		minPq.pop();
	}
}


void showResult() {
	if (Size == 0)
		cout << "EMPTY\n";	
	else {
		clean();
		cout << maxPq.top() << ' ' << -minPq.top() << '\n';
	}
}


void clear(priority_queue<long long> &que) {
	priority_queue<long long> empty;
	swap(que, empty);
}