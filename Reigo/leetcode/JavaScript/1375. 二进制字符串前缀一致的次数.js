/**
 * @param {number[]} flips
 * @return {number}
 */
var numTimesAllBlue = function(flips) {
    let ans=0
    flips.reduce((pre,cur,idx)=>{
        pre=Math.max(pre,cur);
        if(idx+1==pre)ans+=1;
        return pre
    },0)
    return ans
};