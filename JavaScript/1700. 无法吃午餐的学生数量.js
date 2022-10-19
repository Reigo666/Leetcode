/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
 var countStudents = function(students, sandwiches) {
    var s0=0;
    var s1=0;
    for(s of students){
        if(s){
            s1+=1;
        }else{
            s0+=1;
        }
    }
    var ans=0;
    for(s of sandwiches){
        if(s){
            s1-=1;
        }else{
            s0-=1;
        }
        if(s1<0 || s0<0){
            s0+=1;
            break;
        }
    }
    return s0+s1
};