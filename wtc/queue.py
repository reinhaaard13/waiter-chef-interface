class OrderQueue:
    DEFAULT_SIZE = 10 # Ukuran default dari base array yang dibuat

    def __init__(self):
        self._data = [None] * OrderQueue.DEFAULT_SIZE
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise IndexError('Order queue is currently empty!')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Order queue is currently empty!')

        # Menyimpan elemen di index front ke dalam variabel
        ans = self._data[self._front]
        # Assign nilai NONE ke index front
        self._data[self._front] = None
        # Mengatur nilai _front menjadi index selanjutnya
        self._front = (self._front + 1) % len(self._data)
        # Mengurangi variable _size
        self._size -= 1

        # Shrinking array if the num of its elems is less than
        # one four of its capacity
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
            
        return ans
    
    def enqueue(self, order): 
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        back = (self._front + self._size) % len(self._data)
        self._data[back] = order
        self._size += 1

    def _resize(self, new_capacity):
        old_queue = self._data
        self._data = [None] * new_capacity
        old_front = self._front
        # Re-align queue sehingga front menjadi 0 kembali
        for i in range(self._size):
            self._data[i] = old_queue[old_front]
            old_front = (1 + old_front) % len(old_queue)
        self._front = 0

    def getQueueToList(self):
        queue_list = [None] * len(self._data)
        front = self._front
        for i in range(self._size):     # Re-align queue sehingga front menjadi 0 kembali
            queue_list[i] = self._data[front]
            front = (1 + front) % len(self._data)
        return queue_list