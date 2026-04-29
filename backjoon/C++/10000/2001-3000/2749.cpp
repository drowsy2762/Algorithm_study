// https://www.acmicpc.net/problem/2749 : 피보나치 수 3(c++)
// 2024-05-16
#include <iostream>
#include <string.h>
using namespace std;

int fibonachi(int n)
{
    int result;
    int fibo[1500000];
    fibo[0] = 0;
    fibo[1] = 1;
    for (int i = 2; i < n; i++)
    {
        fibo[i] = fibo[i - 1] + fibo[i - 2];
        fibo[i] %= 1000000;
    }
    result = fibo[n];
    return result;
}

int main(void)
{
    int n;
    cin >> n;
    cout << fibonachi(n % 1500000) << endl;
    return 0;
}