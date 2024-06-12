#include <iostream>
#include <vector>

const unsigned long long MOD = 1000000007;
using namespace std;

vector<vector<unsigned long long>> dp(1001, vector<unsigned long long>(1001, 0));

unsigned long long fibonacci2D(int x, int y) {

    for (int i = 0; i <= x; i++) {
        for (int j = 0; j <= y; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 1;
            } else {
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] + dp[i - 1][j - 1]) % MOD;
            }
        }
    }
    
    return dp[x][y];
}

int main() {
    int T;
    cin >> T;
    
    while (T--) {
        int x, y;
        cin >> x >> y;
        
        unsigned long long result = fibonacci2D(x, y);
        cout << result << endl;
    }
    
    return 0;
}