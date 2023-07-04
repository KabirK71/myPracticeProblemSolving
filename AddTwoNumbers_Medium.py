# The problem here is form leet code.
# Inputs are 2 linked lists whose values are integers. The numbers that need to be added are saved in these
# linked lists are in reverse order 
# You have to add these 2 numbers and return a list again with numbers in reverse order.


# I solved it using the basic possible method.
# Editorial says you can use the carry method and directly add.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0) #declared the first node of the link list I want to return
        num1 = "" 
        num2 = ""

        # Take each number from the linked lists and convert it to string and concatenate it.
        while l1 != None:
            num1 = num1 + str(l1.val)
            l1 = l1.next 

        while l2 != None:
            num2 = num2 + str(l2.val)
            l2 = l2.next
        
        # reversing the strings to get the corret numbers
        num1 = num1[::-1] 
        num2 = num2[::-1]

        # adding the numbers
        result = int(num1) + int(num2)

        # converting the result back to string
        result = str(result)
        result = result[::-1] # reversing the result string
 
        #saving each digit of the result one by one in the linked list i will return
        res1 = res
        for i in range(len(result)):
            res.val = int(result[i])
            if i != (len(result)-1):
                res.next = ListNode(0)
                res = res.next

        return res1