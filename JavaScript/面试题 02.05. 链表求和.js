/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
 var addTwoNumbers = function(l1, l2) {
    let dummynode=new ListNode(-1);
    var temp=dummynode;
    let carry=false;
    while(l1 || l2){
        let val=0;
        if(l1){
            val+=l1.val;
        }
        if(l2){
            val+=l2.val;
        }

        if(carry){
            val+=1;
            carry=false;
        }

        if(val>=10){
            carry=true;
            val-=10;
        }
        var newnode=new ListNode(val);
        temp.next=newnode;
        if(l1){
            l1=l1.next;
        }
        if(l2){
            l2=l2.next;
        }
        temp=temp.next;
    }
    if(carry){
       temp.next=new ListNode(1); 
    }
    return dummynode.next;
    
}