class MyQueue(object):

    def __init__(self):
        self.stackin = []
        self.stackout = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stackin.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.transfer()
        return self.stackout.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.transfer()
        return self.stackout[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stackin and not self.stackout

    def transfer(self):
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())