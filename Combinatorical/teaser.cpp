// Magic Sqaure - brute force approach

#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

const int N = 3; // matrix size
const int N2 = 9; // set of numbers size

double factorial(int n) {
	vector<double> f(n+1);
	f[0]=1;
	f[1]=1;
	for(auto i=2; i <= n; ++i) {
		f[i]=i*f[i-1];
	}
	return f[n];
}

int test(int array[N][N]) {
	int sum, sumcol, sumrow, sumdiag1, sumdiag2;
	int i,j;
	for(i=sum=0.; i < N; i++) {
	sum+=array[0][i];
	}
	sumdiag1 = sumdiag2 = 0;
	for(i=0; i < N; i++) {
		sumcol=sumrow=0;
		for(j=0; j < N; j++) {
			sumrow+=array[i][j];
			sumcol+=array[j][i];
		}
		if(sumrow!=sum) return 0;
		if(sumcol!=sum) return 0;
		sumdiag1+=array[i][i];
		sumdiag2+=array[i][N-1-i];
	}
	if(sumdiag1!=sum) return 0;
	if(sumdiag2!=sum) return 0;
	return 1;
} // end test

void print(int array[N][N], int width) {
	for(int i=0; i < N; i++) {
		for(int j=0; j < N; j++) {
			cout << setw(width) << array[i][j];
		}
		cout << "\n";
	}
} // end print

void generate(int numbers[N], int width) {
	static double done = 0;
	static double total = factorial(N2);
	static int solutions = 0;
	static int used[N2];
	static int array[N][N];
	static int d = 0;
	if(d==0) {
		for(int j=0; j < N2; j++) {
			used[j]=0;
		}
	}
	if((d==N2) && (test(array))) {
		cerr << endl << "solution " << (++solutions) << endl;
		print(array,width);
		cout << "\n";
	}
	if(d==N2) {
		cerr << (++done)/total << "            \r";
		return;
	}

	for(int i=0; i < N2; i++) {
		if(!used[i]) {
			array[d/N][d%N]=numbers[i];
			d++;
			used[i]=1;
			generate(numbers,width);
			used[i]=0;
			d--;
		}
	}
} // end generate

int main() {
	int numbers[N2] = {1,2,3,4,5,6,7,8,9};
	generate(numbers,N);
	return 0;
}
