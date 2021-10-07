#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    vector<int> v1 = {1, 2, 3};
    for(int i = 0; i < v1.size(); i++)
    {
        cout << v1[i] << endl;
    }
    
    vector<int> v2[3];
    v2[0] = {1, 2};
    v2[1] = {3, 4, 5};
    v2[2] = {6, 7, 8, 9};
    for(int i = 0; i< v2[0].size(); i++)
    {
        cout << v2[0][i] << endl;
    }
    
    for(auto j: v2[1])
    {
        cout << j << endl;
    }
    return 0;
}