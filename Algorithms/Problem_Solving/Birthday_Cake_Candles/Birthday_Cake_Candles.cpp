#include <iostream>
#include <vector>
#include <algorithm> // std::max_element

//using std::cout;
using namespace std;

int birthdayCakeCandles(vector<int> ar);

int main(void)
{
	vector<int> ar{3, 2, 1, 3};
	cout << birthdayCakeCandles(ar) << endl;
	return 0;
}

int birthdayCakeCandles(vector<int> ar) {
	int count = 0, max = 0;
	vector<int>::iterator iter;
	
	max = *max_element(ar.begin(), ar.end());
	//for (iter = ar.begin(); iter != ar.end(); iter++)
	//	if (*iter > max) max = *iter;
	
	for (iter = ar.begin(); iter != ar.end(); iter++)
		if (*iter == max) count++;
	
	return count;
}