from xml.dom.minidom import Element

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1, l2):    
        e = 0    
        sum = 0

        while (l1 is not None or l2 is not None):
            if (l1 is None):
                sum +=  (l2.val) * pow(10,e)
                l2 = l2.next
            elif (l2 is None):
                sum +=  (l1.val) * pow(10,e)
                l1 = l1.next
            else:
                sum +=  (l1.val + l2.val) * pow(10,e)
                l1 = l1.next
                l2 = l2.next
            e += 1 
          
        sumLEN = len(str(sum))
        sumSTR = str(sum)
        rNode = ListNode(int(sumSTR[0]))
        
        temp = rNode
        for i in range(1,sumLEN):
            node = ListNode(int(sumSTR[i]))
            temp.next = node
            temp = temp.next

        prev = None
        current = rNode
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        rNode = prev
        return rNode



def main():
    # 9,9,9,9,9,9,9
    l1, l2 , l3, l4,l5,l6,l7 = ListNode(), ListNode(), ListNode(), ListNode(),ListNode(), ListNode(), ListNode()
    l1.val = 9
    l2.val = 9
    l3.val = 9
    l4.val = 9
    l5.val = 9
    l6.val = 9
    l7.val = 9

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7
    l7.next = None

    #9,9,9,9
    l4, l5 , l6, l7 = ListNode(), ListNode(), ListNode(), ListNode()
    l4.val = 9
    l5.val = 9
    l6.val = 9 
    l7.val = 9

    l4.next = l5
    l5.next = l6
    l6.next = l7
    l7.next = None

    rNode = ListNode()
    s1 = Solution()
    rNode = s1.addTwoNumbers(l1, l4)
    
    while (rNode is not None): 
        print(rNode.val, end = ' ')
        rNode = rNode.next
    return

if __name__ == '__main__': 
    main()

