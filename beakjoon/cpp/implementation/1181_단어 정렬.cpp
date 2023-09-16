#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int N;
vector<string> words;

void inputWords();
void outputWords();
bool compare(string a, string b);

int main() {
	inputWords();
	sort(words.begin(), words.end(), compare);
	outputWords();

	return 0;
}

void inputWords() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		string word;
		cin >> word;
		words.push_back(word);
	}
}

void outputWords() {
	cout << words[0] << '\n';
	for (int i = 1; i < N; i++) {
		if (words[i-1] == words[i])
			continue;
		cout << words[i] << '\n';
	}
}

bool compare(string a, string b) {
	int aL = a.length();
	int bL = b.length();
	if (aL == bL) {
		return a < b;
	}
	else
		return aL < bL;
}