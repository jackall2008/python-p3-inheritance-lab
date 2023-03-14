#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
    ]

    def __init__(self, first_name=None, last_name=None, knowledge=[None]):
        print("Teacher.__init__ called with knowledge")
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        random.choice(self.knowledge)

        pass