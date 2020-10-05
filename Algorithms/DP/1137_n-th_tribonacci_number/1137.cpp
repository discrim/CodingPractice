#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::stoi;

int tribonacci(int n);

int main(int argc, char* argv[])
{
    if (argc == 1)
    {
        cout << "Usage: ./1137.exe 13" << endl;
        return 0;
    }

    int n = stoi(argv[1]);
    cout << "Tribonacci Number" << endl;
    cout << "Input: " << n;
    cout << " / Output: " << tribonacci(n) << endl;
    return 0;
}

int tribonacci(int n)
{
    if (n == 0)
        return 0;
    else if (n == 1 || n == 2)
        return 1;
    else
        return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1);
}
