#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool vecsort2d(const vector<int> v1, const vector<int> v2);
int luckBalance(int k, vector<vector<int>> contests);

bool vecsort2d(const vector<int> v1, const vector<int> v2) {
	return v1[0] > v2[0];
}

int luckBalance(int k, vector<vector<int>> contests) {
	int luck = 0;
	vector<vector<int>> impt, noim;
	vector<vector<int>>::iterator iter;
	
	for (iter = contests.begin(); iter != contests.end(); ++iter) {
		if ((*iter)[1] == 1) impt.push_back(*iter);
		else 				 noim.push_back(*iter);
	}
	
	sort(impt.begin(), impt.end(), vecsort2d);
	
	for (iter = impt.begin(); iter != impt.end(); ++iter) {
		if (k-- > 0) luck += (*iter)[0];
		else 		 luck -= (*iter)[0];
	}
	
	for (iter = noim.begin(); iter != noim.end(); ++iter) {
		luck += (*iter)[0];
	}
	
	return luck;
}

int main(void) {
	vector<vector<int>> v1 = {{5, 1}, {2, 1}, {1, 1}, {8, 1}, {10, 0}, {5, 0}};
	cout << luckBalance(3, v1) << endl;
	return 0;
}