/**
 * @param {number[]} nums
 * @return {number}
 */
 var majorityElement = function(nums) {
    var x=-1;
    var vote=0;
    for(num of nums){
        if(vote==0){
            x=num;
            vote+=1;
        }else{
            if(num==x){
                vote+=1;
            }else{
                vote-=1;
            }
        }
    }
    return x;
};