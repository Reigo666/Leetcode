/**
 * @param {number[]} fruits
 * @return {number}
 */
 var totalFruit = function(fruits) {
    var l=0,r=0;
    var n=fruits.length;
    var dict=new Map();
    var ans=0;
    while(r<n){
        if(!dict.has(fruits[r])){
            dict.set(fruits[r],1);
            while(l<n && dict.size>2){
                dict.set(fruits[l],dict.get(fruits[l])-1);
                if(dict.get(fruits[l])==0){
                    dict.delete(fruits[l]);
                }
                l+=1;
            }
        }else{
            dict.set(fruits[r],dict.get(fruits[r])+1);
        }
        //console.log(dict)
        ans=Math.max(ans,r-l+1);
        r+=1;
    }
    return ans;
};