/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
 var getIntersectionNode = function(headA, headB) {
    var A=headA;
    var B=headB;
    while(A!=B){
        if(A){
            A=A.next;
        }else{
            A=headB;
        }

        if(B){
            B=B.next;
        }else{
            B=headA;
        }
    }
    return A;
};