import random


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Inserts item to the front of the queue.
        Runtime - O(n) / Linear time as it forces all of the other items in the queue to move one index to the right.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Returns and removes the front-most item of the queue, represented as the last item in the list.
        Runtime - O(1)
        """
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        """
        Returns the front-most item in the queue.
        Runtime - O(1)
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Returns the length of the queue.
        Runtime - O(1)
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns a boolean value if the queue is empty or not.
        Runtime - O(1)
        """
        if self.items:
            return True
        return False


class Job:
    def __init__(self):
        self.pages = random.randint(1, 11)

    def print_page(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False


class Printer:
    def __init__(self):
        self.current_job = None

    def get_job(self, queue):
        try:
            self.current_job = queue.dequeue()
        except IndexError:
            return "No more jobs to print."

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            return "Job is complete."
        else:
            return "An error occurred."

