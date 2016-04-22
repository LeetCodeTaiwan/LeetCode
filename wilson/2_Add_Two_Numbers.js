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
function ListNode(val) {
    this.val = val;
    this.next = null;
}

function printList(root) {
    var cur = root;
    while(cur) {
        console.log(cur.val);
        cur = cur.next;
    }
}

var addTwoNumbers = function(l1, l2) {
    var answerListRoot = new ListNode();
    var cur1 = l1;
    var cur2 = l2;
    var answerCur = answerListRoot;
    var rest = 0, sum = 0;
    while (cur1 || cur2) {
        answerCur.next = new ListNode();
        if (!cur1) {
            sum = cur2.val + rest;
        }
        else if(!cur2) {
            sum = cur1.val + rest;
        }
        else {
            sum = cur1.val + cur2.val + rest;
        }
        if (sum > 9) {
            rest = parseInt(sum / 10);
            answerCur.val = sum % 10;
        }
        else {
            rest = 0;
            answerCur.val = sum;
        }
        if (!cur1) {
            answerCur = answerCur.next;
            cur2 = cur2.next;
        }
        else if(!cur2) {
            answerCur = answerCur.next;
            cur1 = cur1.next;
        }
        else {
            answerCur = answerCur.next;
            cur1 = cur1.next;
            cur2 = cur2.next;
        }
    }
    if (rest > 0) {
        answerCur.val = rest;
    } 
    var finalCur = answerListRoot;
    while (finalCur.next.val !== undefined) {
        finalCur = finalCur.next;
        if (!finalCur.next) {
            break;
        }
    }
    finalCur.next = null;
    return answerListRoot;
};