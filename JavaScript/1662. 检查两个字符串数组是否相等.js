/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
 var arrayStringsAreEqual = function(word1, word2) {
    var s1=word1.join("");
    var s2=word2.join("");
    //console.log(s1,s2);
    if(s1==s2)return true;
    return false;
};