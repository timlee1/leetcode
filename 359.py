class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.log:
            self.log[message] = timestamp
            return True
        else:
            if timestamp - self.log[message] < 10:
                return False
            else:
                self.log[message] = timestamp
                return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

if __name__ == '__main__':
    logger = Logger()
    print logger.shouldPrintMessage(1, 'foo')
    print logger.shouldPrintMessage(2, 'bar')
    print logger.shouldPrintMessage(3, 'foo')
    print logger.shouldPrintMessage(8, 'bar')
    print logger.shouldPrintMessage(10, 'foo')
    print logger.shouldPrintMessage(11, 'foo')