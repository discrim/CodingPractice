#include <iostream>
#include "myns.h"

int main(void) {
	std::cout << yonsei::year << "\n";
	yonsei::color = "Royal Blue"; // Declared but undefined in header
	std::cout << yonsei::color << "\n";
	
	michigan::year = 1817; // Declared but undefined in header
	std::cout << michigan::year << "\n";
	std::cout << michigan::city << "\n";
}