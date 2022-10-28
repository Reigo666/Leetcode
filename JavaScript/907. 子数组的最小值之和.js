/**
 * @param {number[]} arr
 * @return {number}
 */
 var sumSubarrayMins = function(arr) {
    var ans=0;
    var __MOD__=10**9+7;

    function solve(l,r){
        if(l>r)return 0;
        if(l==r)return arr[l];
        var mi=arr[l];
        var midx=l;
        for(var i=l;i<=r;i++){
            if(arr[i]<mi){
                mi=arr[i];
                midx=i;
            }
        }
        var cur=(midx-l+1)*(r-midx+1)*mi;
        var ansl=solve(l,midx-1)%__MOD__;
        var ansr=solve(midx+1,r)%__MOD__;
        return (cur+ansl+ansr)%__MOD__;
    }

    return solve(0,arr.length-1);
};