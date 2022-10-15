/**
 * @param {number[]} target
 * @param {number} n
 * @return {string[]}
 */
 var buildArray = function(target, n) {
    var last=target[target.length-1];
    var ans=[];
    var l=0;

    for(var i=1;i<=n;i++){
        if(i==last){
            ans.push("Push");
            break;
        }
        if(target[l]==i){
            ans.push("Push");
            l+=1;
        }else{
            ans.push("Push");
            ans.push("Pop");
        }
    }
    return ans;
};