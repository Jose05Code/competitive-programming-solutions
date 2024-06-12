#include <iostream>
#include <cmath>
#include <iomanip> // setprecision
using namespace std;

int main()
{
    int q;
    cin>>q;
    while(q--)
    {
        float a;
        cin>>a;
        double b=a*a-(M_PI*(a/2)*(a/2));
        cout << fixed <<setprecision(2) << b << endl;
    }
    return 0;
}