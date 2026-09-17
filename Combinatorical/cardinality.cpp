/*Cardinality
count the common element between two set*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> a = {2,3,5,9};
    vector<int> b = {3,4,5,8,9,10};
    int cardinal = 0;
    unordered_set<int> s;
    for(auto x : a) {
        s.insert(x);
    }
    for(auto y : b) {
        if(s.find(y)!=s.end()) {
            cardinal++;
        }
    }
    cout << cardinal << "\n";
    return 0;
}