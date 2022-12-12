/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var removeDuplicateNodes = function(head) {
    var seen=new Set();
    var p=head;
    var pre=new ListNode(-1);
    pre.next=head;
    while(p){
        if(seen.has(p.val)){
            pre.next=p.next;
            p.next=null;
            p=pre.next;
        }else{
            seen.add(p.val);
            p=p.next;
            pre=pre.next;
        }
        
    }
    return head;
};