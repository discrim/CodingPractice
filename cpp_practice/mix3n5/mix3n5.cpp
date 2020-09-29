#include <iostream>

using std::cout;

int mix3n5(int nn) {
	int n2 = nn - 5;
	while(n2 > 0) {
		if (n2 % 3 == 0) return n2;
		n2 -= 5;
	}
	return 0;
}

int main(void) {
	cout << mix3n5(8) << "\n";
	cout << mix3n5(11) << "\n";
	cout << mix3n5(18) << "\n";
	cout << mix3n5(7) << "\n";
	cout << mix3n5(4) << "\n";
	cout << mix3n5(20) << "\n";
	return 0;
}