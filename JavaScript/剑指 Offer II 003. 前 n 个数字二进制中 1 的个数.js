/**
 * @param {number} n
 * @return {number[]}
 */
 var countBits = function(n) {
    var dp=new Array(n+1).fill(0);
    var mult=1;
    for(var i=1;i<=n;i++){
        if(mult*2==i){
            mult=i;
        }
        //console.log(i-mult,i,mult,dp);
        dp[i]=dp[i-mult]+1;
    }
    return dp;
};