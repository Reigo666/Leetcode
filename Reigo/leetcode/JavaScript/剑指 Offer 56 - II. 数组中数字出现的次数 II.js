/**
 * @param {number[]} nums
 * @return {number}
 */
 var singleNumber = function(nums) {
    var ansset=new Set();
    var dict=new Map();
    for(num of nums){
        if(!dict.has(num)){
            dict.set(num,1);
            ansset.add(num);
        }else{
            ansset.delete(num);
        }
        //console.log(ansset);
    }
    var ans=0;
    for(num of ansset.keys()){
        ans=num;
    }
    return ans;
};