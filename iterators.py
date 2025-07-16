class max_count():
    def __init__(self,n):
        self.start = 1
        self.end = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            num = self.start
            self.start += 1
            return num

'''
count=max_count(10)
for i in count:
    print(i)
'''

class remote_control():
    def __init__(self):
        self.index = -1
        self.channels = ['BCC','HBO','CNN','ESPN']

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.channels) - 1 :
            self.index += 1
            return self.channels[self.index]
        else:
            raise StopIteration

r=remote_control()
for i in r:
    print(i)


