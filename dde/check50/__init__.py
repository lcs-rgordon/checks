from check50 import *

class DDE(Checks):

	@check()
	def exists(self):
		"""dde.c exists"""
		self.require("dde.c")

	@check("exists")
	def compiles(self):
		"""dde.c compiles"""
		self.spawn("clang -o dde dde.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_base_case(self):
		"""input from example provided in problem description provides correct output"""
		self.spawn("./dde").stdin("2\nthe cat chased the rat while\nthe dog chased the cat into the rat house\n").stdout("\nthe cat chased 1 rat while\n1 dog 3 1 2 into 1 4 house\n", "\nthe cat chased 1 rat while\n1 dog 3 1 2 into 1 4 house\n").exit(0)