#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'gradingStudents' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY grades as parameter.
 */

vector<int> gradingStudents(vector<int> grades) {
    vector<int> result;
    vector<int>::iterator iter;
    for (iter = grades.begin(); iter != grades.end(); iter++)
    {
        if (*iter < 38)
            result.push_back(*iter);
        else if (*iter < 41)
            result.push_back(40);
        else
        {
            switch(*iter % 10)
            {
                case 3:
                case 8:
                    result.push_back(*iter + 2);
                    break;
                case 4:
                case 9:
                    result.push_back(*iter + 1);
                    break;
                default:
                    result.push_back(*iter);
                    break;
            }
        }
    }
    return result;

}

int main()
{
    string grades_count_temp;
    getline(cin, grades_count_temp);

    int grades_count = stoi(ltrim(rtrim(grades_count_temp)));

    vector<int> grades(grades_count);

    for (int i = 0; i < grades_count; i++) {
        string grades_item_temp;
        getline(cin, grades_item_temp);

        int grades_item = stoi(ltrim(rtrim(grades_item_temp)));

        grades[i] = grades_item;
    }
	
	cout << endl;

    vector<int> result = gradingStudents(grades);

    for (int i = 0; i < result.size(); i++) {
		cout << result[i] << endl;
		}

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
