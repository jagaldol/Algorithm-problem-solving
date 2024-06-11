#include <iostream>
#include <vector>
using namespace std;

int N;
vector<int> inorder;
vector<int> postorder;

void input();
void getPreOrder(int, int, int, int);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	input();
	getPreOrder(0, N - 1, 0, N - 1);

	return 0;
}


void input() {
	cin >> N;
	inorder = vector<int>(N);
	postorder = vector<int>(N);

	int t;
	for (int i = 0; i < N; i++) {
		cin >> t;
		inorder[i] = t;
	}
	for (int i = 0; i < N; i++) {
		cin >> t;
		postorder[i] = t;
	}
}


void getPreOrder(int inStart, int inEnd, int postStart, int postEnd) {

	int root = postorder[postEnd];
	int inNext = inStart;
	for (int i = inStart; i <= inEnd; i++) {
		if (root == inorder[i]) {
			inNext = i;
			break;
		}
	}
	int postOffset = inNext - inStart;

	cout << root << ' ';

	if (inStart < inNext)
		getPreOrder(inStart, inNext - 1, postStart, postStart + postOffset - 1);
	if (inNext < inEnd)
		getPreOrder(inNext + 1, inEnd, postStart + postOffset, postEnd - 1);
}


