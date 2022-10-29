/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
 var countMatches = function(items, ruleKey, ruleValue) {
    var checkidx=-1;
    if(ruleKey=="type"){
        checkidx=0;
    }else if(ruleKey=="color"){
        checkidx=1;
    }else if(ruleKey=="name"){
        checkidx=2;
    }else{
        return 0;
    }
    var ans=0;
    for(var i=0;i<items.length;i++){
        if(items[i][checkidx]==ruleValue) ans+=1
    }
    return ans;
};