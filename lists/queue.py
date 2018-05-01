import time

class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def empty(self):
        return self.items == []

    # In a python list, the array index 0 is th eonly place where new data elements are inserted into the queue.
    # The Insert operation will shift existing data elements in the list by one position up.
    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    # Remove items from the list, where first in is first out.
    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data


class PrintQueueList:
    def __init__(self):
        list_queue = ListQueue()
        start_time = time.time()
        for i in range(1000):
            print(i)
            list_queue.enqueue(i)
        for i in range(1000):
            list_queue.dequeue()
        print("--- %s seconds ---" % (time.time() - start_time))