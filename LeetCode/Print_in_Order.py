"""
1114. Print in Order
https://leetcode.com/problems/print-in-order

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(),
thread B will call second(), and thread C will call third(). Design a mechanism and modify the
program to ensure that second() is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers
in the input seem to imply the ordering. The input format you see is mainly to ensure our tests'
comprehensiveness.

"""

# Could use threading conditions, but I don't know how yet.  Instead, this seems to work.
from time import sleep
from typing import Callable

class Foo:
    def __init__(self):
        self.working_thread=1


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.working_thread+=1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while(self.working_thread==1):
          sleep(0.001)
        printSecond()
        self.working_thread+=1


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while(self.working_thread==1 or self.working_thread==2):
          sleep(0.001)
        printThird()