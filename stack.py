class Stack():
    def __init__(self, items=[]):
        """inits stack with content from 1st param,
        otherwise empty"""
        self.items = [*items]

    def __repr__(self):
        """prints items"""
        print(self.items)

    def push(self, items):
        """adds items to end of items"""
        self.items.append(items)
    
    def pop(self):
        """removes the last item and returns it"""
        return self.items.pop(len(self.items) - 1)