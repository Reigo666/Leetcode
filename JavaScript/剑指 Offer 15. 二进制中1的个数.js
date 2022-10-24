/**
 * @param {number} n - a positive integer
 * @return {number}
 */
 var hammingWeight = function(n) {
    var ans=0;
    for(var i=0;i<32;i++){
        if(n>>i&1==1)ans+=1;
    }
    return ans;
};