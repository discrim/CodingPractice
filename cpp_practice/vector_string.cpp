#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // sort()

using namespace std;

int main(void) {
	vector<string> v1;
	v1.push_back("first");
	v1.push_back("second");
	v1.push_back("third");
	cout << v1.size() << endl;
	cout << v1[0].size() << endl;
	
	vector<string>::iterator iter;
	for (iter = v1.begin(); iter != v1.end(); iter++) {
		cout << *iter << endl;
	}
	
	sort(v1[1].begin(), v1[1].end());
	cout << v1[1] << endl;
	
	cout << v1[1][1] << endl;
}