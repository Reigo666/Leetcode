/**
 * @param {string} str
 * @return {number}
 */
 var strToInt = function(str) {
    var l=0;
    var n=str.length;
    var ans=0;
    var rev=false;
    
    while(l<n && str[l]==' '){
        l+=1;
    }
    if(l==n)return 0;
    if(str[l]=="+"){
        l+=1;
    }else if(str[l]=="-"){
        rev=true;
        l+=1;
    }

    
    if(str[l]>='0' && str[l]<='9'){
        ans=10*ans+Number(str[l]);
        l+=1;
        while(l<n && str[l]>='0' && str[l]<='9'){
            ans=10*ans+Number(str[l]);
            l+=1;
        }
        if(rev)ans=-ans;
        if(ans>=Math.pow(2,31))return Math.pow(2,31)-1;
        if(ans<-Math.pow(2,31))return -Math.pow(2,31);
        return ans;
    }else{
        return 0;
    }
    
};