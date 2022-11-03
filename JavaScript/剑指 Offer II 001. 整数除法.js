/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
 var divide = function(a, b) {
    __MAX__=Math.pow(2,31)-1;
    __MIN__=-Math.pow(2,31);
    if(a==0)return 0;
    var rev=false;
    if(a<0){
        rev=!rev;
        a=-a;
    }
    if(b<0){
        rev=!rev;
        b=-b;
    }

    var ans=0;
    var cnt=30;
    while(a>=b){
        //cnt-=1
        // console.log(a,b);
        // if(!cnt){
        //     return ans;
        // }
        var c=1;
        var d=b;
        while(d+d<=a){
            d=d+d;
            c=c+c;
        }
        ans+=c;
        a-=d;
    }
    if(rev)ans=-ans;
    if(ans>__MAX__ || ans<__MIN__)return __MAX__;
    return ans;
};