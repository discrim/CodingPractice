#include <iostream>

using namespace std;

#define ROW 3
#define COL 4

int sum1D(int len, int *arr1d) {
	int sum = 0;
	for (int ii = 0; ii < len; ++ii) {
		sum += arr1d[ii];
	}
	return sum;
}

int sum2D(int role, int cole, int **arr2d) {
	int sum = 0;
	for (int row = 0; row < role; ++row) {
		for (int col = 0; col < cole; ++col) {
			sum += arr2d[row][col];
		}
	}
	return sum;
}

void show2D(int role, int cole, int **arr2d) {
	for (int row = 0; row < role; ++row) {
		for (int col = 0; col < role; ++col) {
			cout << "&(arr[" << row << "][" << col << "]): " << &(arr2d[row][col]) << "\t";
		}
		cout << endl;
	}
}

int main(void) {
	int arr[ROW][COL] = {{1, 2, 3, 4},
					 {5, 6, 7, 8},
					 {9, 10, 11, 12}};
	
	cout << typeid(arr).name() << endl;
	cout << typeid(arr[0]).name() << endl;
	cout << typeid(*arr).name() << endl;
	
	for (int row = 0; row < ROW; ++row) {
		for (int col = 0; col < COL; ++col) {
			cout << arr[row][col] << "\t";
		}
		cout << endl;
	}
	cout << endl;
	
	cout << **arr << endl;
	
	cout << sum1D(COL, arr[0]) << endl;
	cout << sum1D(COL, *arr) << endl;
	
	for (int row = 0; row < ROW; ++row) {
		for (int col = 0; col < COL; ++col) {
			cout << "&(arr[" << row << "][" << col << "]): " << &(arr[row][col]) << "\t";
		}
		cout << endl;
	}
	
	//show2D(ROW, COL, arr);
	//cout << sum2D(ROW, COL, arr) << endl;
}