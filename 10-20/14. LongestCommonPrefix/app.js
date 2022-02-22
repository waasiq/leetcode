/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */


function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}


var mergeTwoLists = function(list1, list2) {
    if (list1 == null) return list2
    if (list2 == null) return list1

    let head = new ListNode()
    let temp = head

    while (list1 != null && list2 != null)
    {  
            if (list1.val > list2.val) 
            {            
                temp.next = new ListNode(list2.val)
                list2 = list2.next
            }
            else
            {
                temp.next = new ListNode(list1.val)
                list1 = list1.next       
            }
            temp = temp.next
    }
       
    if (list1 != null) temp.next = list1
    if (list2 != null) temp.next = list2 
    
    return head.next
};
    
let l3 = new ListNode(4)
let l2 = new ListNode(2,l3)
let l1 = new ListNode(1, l2)

let l6 = new ListNode(4)
let l5 = new ListNode(3,l6)
let l4 = new ListNode(1,l5)

let node = mergeTwoLists(l1,l4)

let temp = node
while (temp != null)
{
    console.log(temp.val)
    temp = temp.next
}
