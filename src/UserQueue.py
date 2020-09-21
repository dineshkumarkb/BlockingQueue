from collections import deque
import threading


class UserQueue(object):

    def __init__(self, max_limit=5):
        """
        :param max_limit:
        """
        self.max_limit = max_limit
        self.queue = deque()
        self.lock = threading.Lock()

    def enqueue(self, item):
        """
        :param item:
        :return:
        """
        self.lock.acquire(blocking=True)
        self.queue.append(item)
        self.lock.release()

    def dequeue(self):
        """
        :return:
        """
        self.lock.acquire(blocking=True)
        self.queue.popleft()
        self.lock.release()

    def get_size(self):
        return len(self.queue)

