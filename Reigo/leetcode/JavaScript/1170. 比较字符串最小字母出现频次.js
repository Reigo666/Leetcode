/**
 * @param {string[]} queries
 * @param {string[]} words
 * @return {number[]}
 */
var numSmallerByFrequency = function(queries, words) {
    const f=(s)=>{
        let dict=new Map();
        let minch='z';
        for(let i=0;i<s.length;i++){
            if(s[i]<minch){
                minch=s[i];
            }
            if(!dict.has(s[i])){
                dict.set(s[i],1)
            }else{
                dict.set(s[i],dict.get(s[i])+1)
            }
        }
        // console.log(dict,minch)
        return dict.get(minch)
    }
    function bisect_right(nums,target){
        let l=0,r=nums.length;
        while(l<r){
            let mid=parseInt((l+r)/2)
            if(nums[mid]<target){
                l=mid+1
            }else if(nums[mid]==target){
                l=mid+1
            }else{
                r=mid
            }
        }
        // console.log(nums,target,l)
        return l;
    }
    for(let i=0;i<words.length;i++){
        words[i]=f(words[i])
        
    }
    words.sort((a,b)=>a-b)
    
    for(let i=0;i<queries.length;i++){
        queries[i]=words.length-bisect_right(words,f(queries[i]))
    }
    return queries;
};