import lists_pointers as lp
import doubly_linked_list

print("--- Singly Linked list start")
# add new items to SinglyLinkedList
words = lp.SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('bacon')

current = words.tail
# Simple method to print list output
for word in words.iter():
    print(word)

# print List count without needing to iterate over each element in list. taking running time from O(n) to O(1).
print("Word count: " + str(words.count))

words.delete('ham')
print("After deleting word, word count is: " + str(words.count))

# Find a word in the list using the iter method. Returns True if found False if missing.
if words.search('bacon'):
    print("found bacon in the list.")

print("/--- Singly Linked list end")
print("--- Doubly Linked list start")
dll = doubly_linked_list.DoublyLinkedList()
dll.append('Croissants')
dll.append('Pies')
dll.append('Danishes')
dll.append('Macaroons')
dll.append('Pretzels')
print('- Printed forwards:')
dll.print_forwards()
print('- Printed backwards:')
dll.print_backwards()
print('Insert new item to front of list')
dll.insert_head('honey cake')
print('Get first element: {}'.format(dll[0]))
print("/--- Doubly Linked list end")
