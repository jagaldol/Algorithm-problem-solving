#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Person {
	int age;
	int number;
	string name;
};

bool compare(Person a, Person b) {
	if (a.age == b.age)
		return a.number < b.number;
	return a.age < b.age;
}

int main() {
	
	int N;

	cin >> N;
	vector<Person> v;
	for (int i = 0; i < N; i++) {
		Person p;
		cin >> p.age >> p.name;
		p.number = i + 1;
		v.push_back(p);
	}
	sort(v.begin(), v.end(), compare);

	for (int i = 0; i < N; i++) {
		cout << v[i].age << ' ' << v[i].name << '\n';
	}
	return 0;
}