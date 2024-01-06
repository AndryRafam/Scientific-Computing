// computation of the pow(x,n); where x is a real number and n is an integer.
// linear approach.
// time complexity: O(n).

#include <iostream>
using namespace std;

template <typename T>
T pow_linear(const T& x, size_t n) {
    T y = 1;
    for(size_t i = 1; i <= n; ++i) {
        y*=x;
    }
    return y;
}

int main(int argc, char **argv) {
    // if no argument is given; default value of x=2, default value of n=10.
    double x = (argc > 1) ? atof(argv[1]) : 2;
    size_t n = (argc > 2) ? atoi(argv[2]) : 10;
    cout << pow_linear(x,n);
    return 0;
}