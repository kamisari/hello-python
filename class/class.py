"""
class
"""


class Nyan(object):
    def __init__(self, name):
        print("constructor called")
        self.name = name

    def __del__(self):
        print("destructor called")

    def __repr__(self):
        print("repr called")
        return
