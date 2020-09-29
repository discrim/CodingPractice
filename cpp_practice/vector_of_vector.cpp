#include <iostream>
#include <vector>

using namespace std;

int main(void){
	vector<vector<int>> v1{{1, 2}, {3, 4}, {5, 6}};
	for (int ii = 0; ii < 3; ii++) {
		for (int jj = 0; jj < 2; jj++) {
			cout << v1[ii][jj] << " ";
		}
		cout << endl;
	}
	
	vector<vector<int>>::iterator iter1;
	vector<int>::iterator iter2;
	for (iter1 = v1.begin(); iter1 != v1.end(); ++iter1) {
		if (*(iter1->end()) != 0) {
			cout << *(iter1->begin()) << endl;
		}
		//for (iter2 = iter1->begin(); iter2 != iter1->end(); ++iter2) {
		//	cout << *iter2 << endl;
		//}
	}
}