#include <iostream>
#include <vector>

int main(void) {
  std::vector<int> v1;				// Empty vector.
  std::vector<int> v2(3);			// {0, 0, 0}
  std::vector<int> v3(4, 2);		// {2, 2, 2, 2}
  std::vector<int> v4 = {1, 2, 3};	// {1, 2, 3}
  std::vector<int> v5(v3);			// Copy v3 to make v4.
  
  std::vector<int> vv = {1, 2};
  vv.assign(5, 2);				// Clear vv and fill it with five 2's.
  int idx = 2;
  vv.at(idx);					// Refer to idx'th element of vv.
								// Slower than vv[idx] but range check is included
								// so it is safer.
  vv.front();					// Refer to the first element.
  vv.back();					// Refer to the last element.
  vv.clear();					// Erase all the element but still occupies memory.
  vv.size();					// Number of elements in the vector.
  vv.capacity();				// Numbef of elements that the vector can store
								// without allocating more memory.
  int val = 3;
  vv.push_back(val);			// Append val at the end. If need more memory,
								// double the capacity.
  vv.pop_back();				// Delete the last element but does not free its memory.
  
  for (int ii = 0; ii < vv.size(); ii++) {
	  std::cout << vv[ii] << std::endl;
  }
}