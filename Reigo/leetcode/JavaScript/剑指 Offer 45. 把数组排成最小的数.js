/**
 * @param {number[]} nums
 * @return {string}
 */
 var minNumber = function(nums) {
    for(var i=0;i<nums.length;i++){
        nums[i]=String(nums[i]);
    }
    nums.sort(function(a,b){
        if((a+b)<(b+a))return -1;
        else if((a+b)>(b+a))return 1;
        else return 0;
    });
    
    //console.log(nums);
    return nums.join("");
};