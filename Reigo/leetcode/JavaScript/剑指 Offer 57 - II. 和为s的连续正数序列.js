/**
 * @param {number} target
 * @return {number[][]}
 */
 var findContinuousSequence = function(target) {
    if(target==1){
        return [];
    }
    var l=1;
    var r=2;
    var sum=1;
    var ans=[];
    while(l<=parseInt(target/2)){
        
        while(sum<target){
            sum+=r;
            r+=1;
        }
        if(sum==target){
            var temp=[];
            for(var i=l;i<r;i++){
                temp.push(i);
            }
            ans.push(temp);
        }
        sum=sum-l;
        l+=1;
    }
    return ans;
};