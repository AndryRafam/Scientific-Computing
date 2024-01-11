#include <iostream>
#include "inplace_factorize.h"
#include "inplace_solve.h"
using namespace std;

double u (double x) {return (1-x*x)/2;}

int main(int argc, char **argv) {
    size_t n = (argc > 1) ? atoi(argv[1]) : 11;
    double h = 2./n;
    valarray<double> D(2,n-1), L(-1,n-2);
    inplace_factorize(D,L);
    valarray<double> b(h*h,n-1);
    inplace_solve(D,L,b);
    valarray<double> pi_h_u(n-1);
    for(size_t i = 0; i < n-1; i++) {
        pi_h_u[i] = u(-1+(i+1)*h);
    }
    valarray<double> uerr = abs(pi_h_u-b);
    cout << "err = " << uerr.max() << endl;
    return (uerr.max() < 1e-8) ? 0:1;
}