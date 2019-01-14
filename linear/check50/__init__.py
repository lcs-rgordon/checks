from check50 import *


class Linear(Checks):

    @check()
    def exists(self):
        """linear.c exists"""
        self.require("linear.c")

    @check("exists")
    def compiles(self):
        """linear.c compiles"""
        self.spawn("clang -std=c11 -o linear linear.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_handles_addition(self):
        """linear search finds Malan"""
        self.spawn("./linear").stdin("Malan").stdout("Calling Malan\n").exit(0)

    @check("compiles")
    def test_handles_subtraction(self):
        """linear search finds Smith"""
        self.spawn("./linear").stdin("Smith").stdout("Calling Smith\n").exit(0)

    @check("compiles")
    def test_handles_division(self):
        """linear search does not fine Tanzosh"""
        self.spawn("./linear").stdin("Tanzosh").stdout("Quitting\n").exit(0)

