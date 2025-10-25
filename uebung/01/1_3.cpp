#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <string>
#include <stdio.h>

double comb(int N, int K, double hit_p, int* hits, double* k_p) {
    // K leading 1's
    std::string bitmask(K, 1);
    bitmask.resize(N * 2, 0); 
    int diff;
    double p;
 
    // permute bitmask
    do {
        // reseting diff and p
        diff = 0;
        p = 1;
        // first team
        for (int i = 0; i < N; ++i)
        {
            // hit
            if (bitmask[i]) {
                diff += 1;
                p *= hit_p;

            }
            // miss
            else {
                p *= (1 - hit_p);
            }
        }
        // secons team
        for (int i = N; i < 2 * N; ++i)
        {
            // hit
            if (bitmask[i]) {
                diff -= 1;
                p *= hit_p;
            }
            // miss
            else {
                p *= (1 - hit_p);
            }
        }
        // adjusting hits and probabilty
        hits[diff] += 1;
        k_p[diff] += p;
    } while (std::prev_permutation(bitmask.begin(), bitmask.end()));
    return 0;
}

int main() {
    // setting up parameters
    int n = 10;
    double p = 3. / 4.;
    int* hits = (int*) malloc((n * 2 + 1) * sizeof(int));
    // offseting array to n
    // offset array can be accesed at [-5..-1]
    int* hits_zero = hits + n;
    double* k_p = (double*) malloc((n * 2 + 1) * sizeof(double));
    // offseting array to n
    double* k_p_zero = k_p + n;

    // generating combinations
    for (int k = 0; k <= n * 2; k++)
        comb(n, k, p, hits_zero, k_p_zero);

    // printing results
    for (int a = -n; a <= n; a++) {
        std::cout << a << "\t" << hits_zero[a] << "\t" << k_p_zero[a] << std::endl;

    }

    // cleanup
    free(hits);
    free(k_p);
    return 0;
}
