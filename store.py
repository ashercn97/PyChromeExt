

class Storage:
    def __init__(self):
        self.stack = []
        self.data = {}
    # for stack
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    # for data
    def get(self, key):
        return self.data.get(key)
    def add(self, key, value):
        self.data[key] = value
    def remove(self, key):
        del self.data[key]
    def clear(self):
        self.data = {}
    # for both
    def get_stack(self):
        return self.stack