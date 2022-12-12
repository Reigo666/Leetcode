/**
 * @param {number} n
 * @return {number}
 */
 var sumNums = function(n) {
    function solve(n){
        n&&(n+=solve(n-1))
        return n;
    }
    return solve(n);
};