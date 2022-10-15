/**
 * @param {string} s
 * @return {string}
 */
 var reverseWords = function(s) {
    var wordlist=[];
    var l=0;
    while(l<s.length){
        var temp="";
        while(l<s.length && s[l]==" "){
            l+=1;
        }
        while(l<s.length && s[l]!=" "){
            temp+=s[l];
            l+=1;
        }
        if(temp)wordlist.push(temp);
    }
    //console.log(wordlist);
    return wordlist.reverse().join(" ");
};