
// INCOMPLETE

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Complete the maximumPerimeterTriangle function below.
bool isTriangle(int aa, int bb, int cc) {
    if (aa + bb <= cc) return false;
    else if (aa + cc <= bb) return false;
    else if (bb + cc <= aa) return false;
    return true;
}

bool sortVec(const vector<int> v1, const vector<int> v2) {
    if (v1[2] > v2[2]) return true;
    if (v1[2] < v2[2]) return false;
    if (v1[0] > v2[0]) return true;
    if (v1[0] < v2[0]) return false;
    return false;
}

vector<int> maximumPerimeterTriangle(vector<int> sticks) {
    vector<vector<int>> valids;
    for (int ii = 0; ii < sticks.size() - 2; ++ii) {
        for (int jj = ii + 1; jj < sticks.size() - 1; ++jj) {
            for (int kk = jj + 1; kk < sticks.size(); ++kk) {
                if (isTriangle(sticks[ii], sticks[jj], sticks[kk])) {
                    valids.push_back({sticks[ii], sticks[jj], sticks[kk]});
                }
            }
        }
    }
    
    sort(valids.begin(), valids.end(), sortVec);

    if (valids.empty()) return {-1};
    return valids.front();
}

void printVector(vector<int> vv) {
	for (int ii = 0; ii < vv.size(); ++ii) cout << vv[ii] << " ";
	cout << "\n";
}

int main()
{
	vector<int> v1 = {1, 2, 3, 4, 4, 10};
	printVector(maximumPerimeterTriangle(v1));

    return 0;
}
