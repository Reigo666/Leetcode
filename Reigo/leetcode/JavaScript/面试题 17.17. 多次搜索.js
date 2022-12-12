/**
 * @param {string} big
 * @param {string[]} smalls
 * @return {number[][]}
 */
 var multiSearch = function(big, smalls) {
    var dict=new Map();
    for(var i=0;i<big.length;i++){
        var temp="";
        for(var j=i;j<big.length;j++){
            temp+=big[j];
            //console.log(temp);
            if(!dict.has(temp)){
                //console.log(temp);
                dict.set(temp,[i]);
            }else{
                var l=dict.get(temp);
                l.push(i);
                dict.set(temp,l);
            }
        }
        // console.log(dict);
    }
    var ans=[];
    for(s of smalls){
        if(dict.has(s)){
            ans.push(dict.get(s));
        }else{
            ans.push([]);
        }
    }
    return ans;
};