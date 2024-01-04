#include "quaternion.h"
using namespace std;

auto main(int argc, char **argv)->int {
    quaternion<double> h1(1,1,7,9), h2(1,-1,-7,-9);
    cout << "h1 = " << h1 << endl
         << "h2 = " << h2 << endl
         << "h1+h2 = " << h1+h2 << endl
         << "h1-h2 = " << h1-h2 << endl
         << "h1*h2 = " << h1*h2 << endl
         << "h1/h2 = " << h1/h2 << endl
         << "(h1/h2)*h2 = " << (h1/h2)*h2 << endl;
    return 0;
}