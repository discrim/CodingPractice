#include <iostream>
#include <vector>

int main(void)
{
	std::vector<int> v1;
	
	v1.push_back(10);
	v1.push_back(20);
	v1.push_back(30);
	v1.push_back(40);
	v1.push_back(50);
	
	std::vector<int>::iterator iter = v1.begin();
	
	std::cout << iter[3] << "\n" << std::endl;
	
	iter += 2;
	std::cout << *iter << "\n" << std::endl;
	
	for (iter = v1.begin(); iter != v1.end(); ++iter)
		std::cout << *iter << std::endl;
	
	std::vector<int> v2{5, 4, 3, 2, 1};
	
	for (int ii = 0; ii < v1.size(); ii++)
		std::cout << v1[ii] + v2[ii] << std::endl;
	
	//std::cout << v1 > v2 << endl;
	
	return 0;
}