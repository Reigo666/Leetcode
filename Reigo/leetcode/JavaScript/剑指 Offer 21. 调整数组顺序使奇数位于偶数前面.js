/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var exchange = function(nums) {
    var l=0,r=nums.length-1;
    while(l<r){
        while(l<r && nums[l]%2!=0){
            l+=1;
        }
        while(l<r && nums[r]%2==0){
            r-=1;
        }
        [nums[l],nums[r]]=[nums[r],nums[l]];
    }
    return nums;
};