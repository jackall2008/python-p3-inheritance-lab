#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name=None, last_name=None, knowledge=[None]):
        print("Teacher.__init__ called with knowledge")
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
    
    def learn(self, empty_string=None):
        self.knowledge.append(empty_string)
        pass