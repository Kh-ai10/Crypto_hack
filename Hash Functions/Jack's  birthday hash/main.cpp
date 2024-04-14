#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    double a = 0.0;
    int n = pow(2,11);
    int k = 1;
    while (a < 0.5)
    {
        a= 1.0 - pow((n-1.0)/n,k);
        k++;
    }
    cout << k-1;
}
