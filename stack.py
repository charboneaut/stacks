class Stack():
    def __init__(self, items=[]):
        """inits stack with content from 1st param,
        otherwise empty"""
        self.items = [*items]

    def __repr__(self):
        """prints items"""
        print(self.items)

    def push(self, item):
        """adds item to end of items,
        will decide to extend or append based on item iterability"""
        if hasattr(item, "__iter__"):
            self.items.extend(item)
        else:
            self.items.append(item)

    def pop(self, count=1):
        """removes the last item or
         item list in the order of popping and returns it"""
        if count == 1:
            return self.items.pop(len(self.items) - 1)
        else:
            items = []
            for _ in range(count):
                items.append(self.items.pop(len(self.items) - 1))
            return items
