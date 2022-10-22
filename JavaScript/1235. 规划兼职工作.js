/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number[]} profit
 * @return {number}
 */
 var jobScheduling = function(startTime, endTime, profit) {
    var z=startTime;
    for(var i=0;i<z.length;i++){
        z[i]=[endTime[i],startTime[i],profit[i]];
    }
    z.sort((a,b)=>{
        return a[0]-b[0];
    })
    dp=new Array(z.length+1).fill(0);

    function bisect_right(arr,val,hi){
        var l=0;
        var r=hi;
        while(l<r){
            var mid=parseInt((l+r)/2);
            if(arr[mid][0]>val){
                r=mid;
            }else{
                l=mid+1;
            }
        }
        return l;
    }

    for(var i=0;i<z.length;i++){
        [et,st,p]=z[i];
        j=bisect_right(z,st,i)
        dp[i+1]=Math.max(dp[i],dp[j]+p)
    }
    //console.log(z);
    return dp[z.length]
};