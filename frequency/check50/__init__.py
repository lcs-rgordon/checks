from check50 import *

class PartnerUp(Checks):

	@check()
	def exists(self):
		"""frequency.c exists"""
		self.require("frequency.c")

	@check("exists")
	def compiles(self):
		"""frequency.c compiles"""
		self.spawn("clang -o frequency frequency.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_base_case(self):
		"""does the program provide the expected output from the example given?"""
		self.spawn("./frequency").stdin("2").stdin("THE QUICK BROWN FOX").stdin("JUMPED OVER THE LAZY DOG").stdout("A *").stdout("B *").stdout("C *").stdout("D **").stdout("E ****").stdout("F *").stdout("G *").stdout("H **").stdout("I *").stdout("J *").stdout("K *").stdout("L *").stdout("M *").stdout("N *").stdout("O ****").stdout("P *").stdout("Q *").stdout("R **").stdout("S").stdout("T **").stdout("U **").stdout("V *").stdout("W *").stdout("X *").stdout("Y *").stdout("Z *").exit(0)