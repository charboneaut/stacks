class Stack():
    def __init__(self, items=[]):
        """inits stack with content from 1st param,
        otherwise empty"""
        self.items = [*items]

    def __repr__(self):
        """prints items"""
        print(self.items)
