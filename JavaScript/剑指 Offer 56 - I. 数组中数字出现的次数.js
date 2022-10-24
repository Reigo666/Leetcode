/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var singleNumbers = function(nums) {
    var set=new Set();
    for(num of nums){
        if(set.has(num)){
            set.delete(num);
        }else{
            set.add(num);
        }
    }
    
    var ans=[];
    for(num of set.keys()){
        ans.push(num);
    }
    return ans;
};