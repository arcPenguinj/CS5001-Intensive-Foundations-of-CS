'''
Sample Code
CS 5001, Fall 2020 - Lecture 10

An implementation of the Stack ADT.
'''


class Stack:
    '''
        Class -- Stack
            A stack data structure.
        Attributes:
            items -- A list of items stored in the stack.
        Methods:
            push -- Push an item onto the Stack
            pop -- Return and remove the item at the top of the Stack
            peek -- Return but don't remove the item at the top of the Stack
            is_empty -- Check if the Stack is empty
            size -- Return the number of items in the Stack
    '''
    def __init__(self):
        '''
            Constructor -- creates a new instance of the Stack class.
            Parameters:
                self -- the current Stack object.
        '''
        self.items = []    

    def push(self, item):
        '''
            Method -- push
                Push an item onto the stack.
            Parameters:
                self -- the current Stack object.
                item -- the item to add to the Stack.
        '''
        self.items.append(item)

    def pop(self):
        '''
            Method -- pop
                Return and remove the item at the top of the Stack.
            Parameters:
                self -- the current Stack object.
            Returns:
                The item at the top of the Stack
        '''
        return self.items.pop()

    def peek(self):
        '''
            Method -- peek
                Return but don't remove the item at the top of the Stack.
            Parameters:
                self -- the current Stack object.
            Returns:
                The item at the top of the Stack
        '''
        if self.is_empty():
            return None
        else:
            return self.items[-1]

    def is_empty(self):
        '''
            Method -- is_empty
                Checks if the stack is empty.
            Parameters:
                self -- the current Stack object.
            Returns:
                True if the Stack contains no items, False otherwise.
        '''
        return len(self.items) == 0

    def size(self):
        '''
            Method -- size
                Returns the number of items in the Stack.
            Parameters:
                self -- the current Stack object.
            Returns:
                The number of items in the Stack.
        '''
        return len(self.items)
