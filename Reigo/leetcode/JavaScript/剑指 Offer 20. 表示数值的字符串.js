/**
 * @param {string} s
 * @return {boolean}
 */
 var isNumber = function(s) {
    var state={
        0:{'b':0,'s':1,'d':2,'dot':5},
        1:{'d':2,'dot':5},
        2:{'d':2,'dot':3,'e':6,'b':9},
        3:{'d':4,'b':9,'e':6},
        4:{'d':4,'e':6,'b':9},
        5:{'d':4},
        6:{'s':7,'d':8},
        7:{'d':8},
        8:{'d':8,'b':9},
        9:{'b':9},
    }

    var ansset=new Set([2,3,4,8,9]);
    var curstate=0;
    for(l of s){
        var cur='unknown';
        if(l>='0' && l<='9'){
            cur='d';
        }else if(l==' '){
            cur='b';
        }else if(l=='+' || l=='-'){
            cur='s';
        }else if(l=='.'){
            cur='dot';
        }else if(l=='e' || l=='E'){
            cur='e';
        }
        if(cur=='unknown')return false;
        if(cur in state[curstate]){
            curstate=state[curstate][cur];
        }else{
            return false;
        }
    }
    if(ansset.has(curstate))return true;
    return false;
};