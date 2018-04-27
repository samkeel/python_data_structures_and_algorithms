import lists_pointers as lp

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
