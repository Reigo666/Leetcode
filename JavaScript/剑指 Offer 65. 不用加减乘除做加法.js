/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
 var add = function(a, b) {
    while(b!=0){
        var carry=(a&b)<<1;
        a=a^b;
        b=carry;
    }
    return a;
};
