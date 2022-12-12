/**
 * @param {string[]} words
 * @return {string}
 */
 var longestWord = function(words) {
    words.sort(function(x,y){
        if(x.length<y.length)return 1;
        else if(x.length>y.length)return -1;
        else{
            if(x>y)return 1;
            else return -1;
        }
    });

    function dfs(cur,words){
        if(cur.length==0)return true;
        for(var i=0;i<words.length;i++){
            if(cur.slice(0,words[i].length)==words[i]){
                if(dfs(cur.slice(words[i].length),words))return true;
            }
        }
        return false;
    }
    for(var i=0;i<words.length;i++){
        if(dfs(words[i],words.slice(i+1))){
            return words[i];
        }
    }
    return "";
    // console.log(words);

};