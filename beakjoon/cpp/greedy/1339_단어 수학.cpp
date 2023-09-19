#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
using namespace std;


vector<char> alphabets[8];
map<char, int> convert;


void input();
void setPriority();
bool compare(pair<char, int>, pair<char, int>);
void showResult();


int main() {
	input();

	setPriority();

	showResult();

	return 0;
}


void input() {
	int N;
	cin >> N;
	
	for (; N--;) {
		string word;
		cin >> word;
		int l = word.length();
		for (int i = 0; i < l; i++) {
			alphabets[l - i - 1].push_back(word[i]);
		}
	}
}


void setPriority() {
	for (int i = 0; i < 8; i++) {
		for (unsigned int j = 0; j < alphabets[i].size(); j++) {
			convert[alphabets[i][j]] = 0;
		}
	}

	int priority = 1;
	for (int i = 0; i < 8; i++) {
		for (unsigned int j = 0; j < alphabets[i].size(); j++) {
			convert[alphabets[i][j]] += priority;
		}
		priority *= 10;
	}

	vector<pair<char, int>> v(convert.begin(), convert.end());

	sort(v.begin(), v.end(), compare);

	int number = 9;
	for (unsigned int i = 0; i < v.size(); i++) {
		char alphabet = v[i].first;
		convert[alphabet] = number;
		number--;
	}
}


bool compare(pair<char, int> a, pair<char, int> b) {
	return a.second > b.second;
}



void showResult() {
	int sum = 0;

	int digit = 1;
	for (int i = 0; i < 8; i++) {
		for (unsigned int j = 0; j < alphabets[i].size(); j++) {
			char alphabet = alphabets[i][j];
			sum += convert[alphabets[i][j]] * digit;
		}
		digit *= 10;
	}
	cout << sum << '\n';
}