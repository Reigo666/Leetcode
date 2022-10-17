/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {number}
 */
 var kthToLast = function(head, k) {
    var fast=head;
    for(var i=0;i<k;i++){
        fast=fast.next;
    }
    var slow=head;
    while(fast){
        fast=fast.next;
        slow=slow.next;
        //console.log(slow.val);
    }
    return slow.val;
};