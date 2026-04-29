#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    unsigned int length;
    cout << "input the length: " << endl;

    while (cin >> length) {


        for (unsigned int i; i <= length; i++) {

            if (length % 2 == 0){
                cout << "Please input a valid odd length (>= 3)!\n";
                break;
            }

            if ((length <= 2) || (length >= 21)) {
                cout << "Please input valid length!\n";
                break;
            }

            switch (i % length) {
            case 1:
            case 0:
                for (unsigned int j; j <= length; j++) {
                    cout << "#";
                }
                cout << endl;
                break;

            default:
                cout << "#";

                cout << " ";
                cout << "#";
                cout << endl;
            }

        }

    }
}