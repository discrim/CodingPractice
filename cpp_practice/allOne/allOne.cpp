#include <iostream>
#include <cmath> // For pow()

using std::cout;

int allOne(int digits) {
	if (digits == 1) return 1;
	return pow(10, digits - 1) + allOne(digits - 1);
}

int main(void) {
	cout << allOne(10) << "\n";
	return 0;
}