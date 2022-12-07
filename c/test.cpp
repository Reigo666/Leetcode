#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        int n = nums.size();
        vector<int> p(30, n);
        vector<int> res(n);
        for (int i = n - 1; i >= 0; i -- ) {
            int t = i;
            for (int j = 0; j < 30; j ++ ){
                int temp=nums[i] >> j & 1;
                if (temp) 
                {
                    p[j] = i;
                }
                else if (p[j] != n) {
                    t = max(t, p[j]);
                }
            }
            res[i] = t - i + 1;
        }
        
        return res;
    }
};

int main()
{
    Solution sol;
    int arr[5]={1,0,2,1,3};
    vector<int> p(arr,arr+5);
    sol.smallestSubarrays(p);
}
