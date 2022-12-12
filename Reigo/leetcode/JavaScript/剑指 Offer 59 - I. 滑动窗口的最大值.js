/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
 var maxSlidingWindow = function(nums, k) {
    var ans=[];
    var q=[];
    for(var i=0;i<nums.length;i++){
    
        if(i>=k){
            if(nums[i-k]==q[0])q.shift();
        }
        while(q.length && q[q.length-1]<nums[i]){
            q.pop();
        }
        q.push(nums[i]);
        ans.push(q[0]);
        
        //console.log(q);
    }
    return ans.slice(k-1);
};