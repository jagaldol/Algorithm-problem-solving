#include <iostream>
using namespace std;

int N;


struct node {
	char c;
	node* left;
	node* right;
};


class tree {
private:
	node* tr;
	int size;
public:
	tree(int n) {
		tr = new node[n];
		for (int i = 0; i < n; i++) {
			tr[i].c = 'A' + i;
			tr[i].left = NULL;
			tr[i].right = NULL;
		}
		size = n;
	}

	void connect(char a, char b, char c) {
		if (b != '.')
			tr[a - 'A'].left = &tr[b - 'A'];
		if (c != '.')
			tr[a - 'A'].right = &tr[c - 'A'];
	}
	void preorder(char c) {
		int i = c - 'A';

		cout << c;
		if (tr[i].left != NULL)
			preorder(tr[i].left->c);
		if (tr[i].right != NULL)
			preorder(tr[i].right->c);

		if (c == 'A')
			cout << '\n';
	}
	void inorder(char c) {
		int i = c - 'A';

		if (tr[i].left != NULL)
			inorder(tr[i].left->c);
		cout << c;
		if (tr[i].right != NULL)
			inorder(tr[i].right->c);

		if (c == 'A')
			cout << '\n';
	}
	void postorder(char c) {
		int i = c - 'A';

		if (tr[i].left != NULL)
			postorder(tr[i].left->c);
		if (tr[i].right != NULL)
			postorder(tr[i].right->c);
		cout << c;

		if (c == 'A')
			cout << '\n';
	}
};


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N;
	tree tr(N);

	for (int i = 0; i < N; i++) {
		char a, b, c;
		cin >> a >> b >> c;
		tr.connect(a, b, c);
	}
	tr.preorder('A');
	tr.inorder('A');
	tr.postorder('A');

	return 0;
}