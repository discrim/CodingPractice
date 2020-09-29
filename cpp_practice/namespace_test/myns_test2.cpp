#include <iostream>
#include "myns.h"

using namespace yonsei;
// using michigan::year;
	// Invokes error "reference to 'year' is ambiguous"
	// because both yonsei and michigan have 'year' in them.
using michigan::city;

int main(void) {
	std::cout << year << "\n";
	yonsei::color = "Royal Blue"; // Declared but undefined in header
	std::cout << color << "\n";
	
	michigan::year = 1817; // Declared but undefined in header
	std::cout << michigan::year << "\n";
	std::cout << city << "\n";
}