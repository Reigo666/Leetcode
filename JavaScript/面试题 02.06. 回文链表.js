/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
 var isPalindrome = function(head) {
    let s=[];
    while(head){
        s.push(head.val)
        head=head.next;
    }
    var l=0;
    var r=s.length-1;
    while(l<r)
    {
        if (s[l]!=s[r]){
            return false;
        }
        l+=1;
        r-=1;
    }
    return true;
};