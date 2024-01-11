#include <valarray>
template <typename T>
void inplace_factorize(std::valarray<T>& D, std::valarray<T>& L) {
    for(size_t i = 1; i < D.size(); i++) {
        T s = L[i-1]/D[i-1];
        D[i] -= s*L[i-1];
        L[i-1] = s;
    }
}