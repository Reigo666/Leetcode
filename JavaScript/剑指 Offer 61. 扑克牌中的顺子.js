/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var isStraight = function(nums) {
    var seen=new Set();
    var ma=-1;
    var mi=100;
    for(num of nums){
        if(num==0)continue;
        if(seen.has(num)){
            return false;
        }else{
            seen.add(num);
            ma=Math.max(ma,num);
            mi=Math.min(mi,num);
        }
    }
    if(ma-mi<=4)return true;
    return false;
};