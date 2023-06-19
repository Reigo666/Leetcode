/**
 * @param {number[]} nums
 * @return {number}
 */
var unequalTriplets = function(nums) {
    let dict=new Map();
    nums.forEach((num)=>{
        if(!dict.has(num)){
            dict.set(num,1)
        }else{
            dict.set(num,dict.get(num)+1)
        }
    })
    let ans=0;
    let n=nums.length
    let a=0
    console.log(dict)
    for(let b of dict.values()){
        // console.log(b)
        // let b=dict.get(val);
        ans+=a*b*(n-a-b)
        a+=b;
    }
    return ans
    
};