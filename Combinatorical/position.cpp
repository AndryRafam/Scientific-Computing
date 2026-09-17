/*position*/

#include <bits/stdc++.h>
using namespace std;

void position(string s, int& m, int& n) {
    m = n = 0;
    for(auto i = 0; i < s.length(); i++) {
        switch(s[i]) {
            case 'r': m++; break;
            case 'u': n++; break;
            case 'l': m--; break;
            case 'd': n--; break;
        }
    }
}

int main() {
    int m, n;
    position("rullddrrruuullll",m,n);
    cout << "(" << m << "," << n << ")" << "\n";
    position("lluurrrrddll",m,n);
    cout << "(" << m << "," << n << ")" << "\n";
    position("",m,n);
    cout << "(" << m << "," << n << ")" << "\n";
    return 0;
}
