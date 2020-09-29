#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::getline;
using std::__cxx11::to_string;

string timeConversion(string s) {
    /*
     * Write your code here.
     */
	string hh = s.substr(0, 2);
    string ap;
    s.pop_back();
    ap = s.back();
    if (ap.compare("A") == 0)
	{
		if (hh.compare("12") == 0)
			s.replace(0, 2, "00");
        return s.substr(0, 8);
	}
	
    else
    {
		int hi;
		if (hh.compare("12") == 0)
			return s.substr(0, 8);
		else
		{
			hi = stoi(s.substr(0, 2), nullptr, 10) + 12;
			return to_string(hi) + s.substr(2, 6);
		}
    }
}


int main(void)
{
	string str1;
	getline(cin, str1);
	cout << timeConversion(str1) << endl;
	return 0;
}