/*Josephus Problem*/

#include <iostream>
using namespace std;

int josephus(int n, int k) {
	int survivor = 0;
	
	for(auto i = 2; i <= n; ++i) {
		survivor = (survivor+k)%i;
	}
	
	return survivor+1;
}

int main() {
	int n = 9;
	int k = 5;
	cout << "Survivor is number: " << josephus(n,k) << "\n";
	return 0;
}
