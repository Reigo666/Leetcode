/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
 var partition = function(head, x) {
    var dummyhead=new ListNode(-1);
    dummyhead.next=head;
    var pre=dummyhead;
    var p=head;
    var guardl=null;
    while(p){
        if(guardl){
            if(p.val>=x){
                p=p.next;
                pre=pre.next;
            }else{
                pre.next=p.next;
                p.next=guardl.next;
                guardl.next=p;
                guardl=p;
                p=pre.next;
            }
        }else{
            if(p.val>=x){
                guardl=pre;
                p=p.next;
                pre=pre.next;
            }else{
                p=p.next;
                pre=pre.next;
            }
        }
    }
    return dummyhead.next;
};