/**
 * @param {string} s
 * @return {string[]}
 */


 var letterCasePermutation = function(s) {
    var ans=[];
    function backTrack(combination,left){
        if(left.length==0){
            ans.push(combination);
            return;
        }
        var ch=left[0];
        if((ch<='z' && ch>='a') ||(ch>='A' && ch<='Z')){
            //var diff='A'-'a';
            backTrack(combination+ch.toLowerCase(),left.slice(1));
            backTrack(combination+ch.toUpperCase(),left.slice(1));
        }else{
            backTrack(combination+ch,left.slice(1));
        }
    }

    backTrack("",s);
    return ans;
};