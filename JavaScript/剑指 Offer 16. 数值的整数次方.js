/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
 var myPow = function(x, n) {
    function solve(x,n){
        if(n==1){
            return x;
        }
        if(n%2==0){
            var temp=solve(x,n/2);
            return temp*temp;
        }else{
            var temp=solve(x,parseInt(n/2));
            return temp*temp*x;
        }
    }
    if(x==0){
        return 0;
    }else if(n==0){
        return 1;
    }else{
        var ans=0;
        var rev=false;
        if(n<0){
            rev=true;
            n=-n;
        }
        ans=solve(x,n);
        if(rev){
            return 1/ans;
        }
        return ans;
    }
    return null;
};