"""
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.
​
Implement the MaxStack class:
​
- MaxStack() Initializes the stack object.
- void push(int x) Pushes element x onto the stack.
- int pop() Removes the element on top of the stack and returns it.
- int top() Gets the element on the top of the stack without removing it.
- int peekMax() Retrieves the maximum element in the stack without removing it.
- int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
"""

class MaxStack:
    def __init__(self):
        self.elements = []
        max_element = 0
        max_elementRemoved = 0
        
    
    def push(self, x: int) -> None:
        self.elements.append(x)
    
    def pop(self) -> int:
        top_element = self.elements[0]
        self.elements.remove(top_element)
        return top_element
    
    def top(self) -> int:
        return self.elements[0]
    
    def peekMax(self) -> int:
        max_element = self.elements[0]
        for element in self.elements:
            if max_element < element:
                max_element = element
        return max_element
    
    def popMax(self) -> int:
        max_element = self.elements[0]
        for element in self.elements:
            if max_element < element:
                max_element = element
        self.elements.remove(max_element)
        return max_element

obj = MaxStack()
assert obj.push(5) == None
assert obj.push(1) == None
assert obj.push(5) == None
assert obj.top() == 5
assert obj.popMax() == 5
assert obj.top() == 1
assert obj.peekMax() == 5
assert obj.pop() == 1
assert obj.top() == 5

