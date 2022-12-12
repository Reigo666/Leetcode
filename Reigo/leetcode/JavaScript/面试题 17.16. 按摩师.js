/**
 * @param {number[]} nums
 * @return {number}
 */
 var massage = function(nums) {
    if(nums.length==0)return 0;
    dp0=0;
    dp1=nums[0];

    for(var i=1;i<nums.length;i++){
        newdp0=Math.max(dp0,dp1);
        newdp1=dp0+nums[i];
        dp0=newdp0;
        dp1=newdp1;
    }

    return Math.max(dp0,dp1);
};