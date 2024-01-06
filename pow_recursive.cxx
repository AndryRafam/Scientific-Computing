// computation of the pow(x,N); where x is a real number and N is an integer.
// recursive approach.
// time complexity: O(logN).

#include <iostream>
using namespace std;

template <typename T>
T pow_recursive(const T& x, size_t n) {
    if(n==0)
        return 1;
    if(n==1)
        return x;
    T y = pow_recursive(x,n/2);
    return (n%2==0) ? y*y : y*y*x;
}

int main(int argc, char **argv) {
    // if no argument is given; default value of x=2, default value of n=10.
    double x = (argc > 1) ? atof(argv[1]) : 2;
    size_t n = (argc > 2) ? atoi(argv[2]) : 10;
    cout << pow_recursive(x,n);
    return 0;
}