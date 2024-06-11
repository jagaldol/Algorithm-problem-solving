#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    int res = 1;
    while(n>0) {
        res *= n--;
    }
    cout << res << '\n';
    
    return 0;
}