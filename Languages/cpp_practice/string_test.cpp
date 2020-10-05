#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;
using std::__cxx11::to_string;

string timeConversion(string s) {
    /*
     * Write your code here.
     */
    string ap;
    s.pop_back();
    ap = s.back();
    if (ap.compare("A") == 0)
        return s.substr(0, 7);
    else
    {
		cout << ".substr(0, 2) of " << s << " is " << s.substr(0, 2) << endl;
        int hi = stoi(s.substr(0, 2), nullptr, 10) + 12;
        string hs = to_string(hi);
		cout << ".substr(2, 6) of " << s << " is " << s.substr(2, 2) << endl;
        return hs + s.substr(2, 6);
    }
}


int main(void)
{
	string str1 = "sample string", bk;
	cout << str1 << endl;
	str1.pop_back();
	cout << str1 << endl;
	cout << str1.back() << endl;
	cout << str1.substr(1, 1) << endl;
	bk = str1.back();
	if (bk.compare("n") == 0)
		cout << "Yeah" << endl;
	
	string str2 = "07:05:45PM";
	cout << timeConversion(str2) << endl;
	return 0;
}