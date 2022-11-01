/**
 * @param {number} n
 * @return {number[]}
 */
 var printNumbers = function(n) {
    var ans=[];
    for(var i=1;i<Math.pow(10,n);i++){
        ans.push(i);
    }
    return ans;
};