/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    var l=0,r=nums.length-1;
    while(l<r){
        if(nums[l]+nums[r]==target){
            return [nums[l],nums[r]];
        }else if(nums[l]+nums[r]<target){
            l+=1;
        }else{
            r-=1;
        }
    }
};