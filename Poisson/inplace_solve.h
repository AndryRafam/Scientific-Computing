#include <valarray>
template <typename T>
void inplace_solve(const std::valarray<T>& D, const std::valarray<T>& L, std::valarray<T>& b) {
    for(size_t i = 1; i < D.size(); i++) {
        b[i] -= L[i-1]*b[i-1];
    }
    for(size_t i = 0; i < D.size(); i++) {
        b[i] /= D[i];
    }
    for(long i = D.size()-1; i > 0; i--) {
        b[i-1] -= L[i-1]*b[i];
    }
}