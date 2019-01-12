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
		self.spawn("./dde").stdin("2").stdin("the cat chased the rat while").stdin("the dog chased the cat into the rat house").stdout("").stdout("the cat chased 1 rat while").stdout("1 dog 3 1 2 into 1 4 house").exit(0)
		
	@check("compiles")
	def test_no_input(self):
		"""handles 0 lines of input correctly"""
		self.spawn("./dde").stdin("0").stdout("").exit(0)
		
	@check("compiles")
	def test_alphabet_twice(self):
		"""handles many short words correctly"""
		self.spawn("./dde").stdin("2").stdin("a b c d e f g h i j k l m n o p q r s t u v w x y z").stdin("a b c d e f g h i j k l m n o p q r s t u v w x y z").stdout("").stdout("a b c d e f g h i j k l m n o p q r s t u v w x y z").stdout("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26").exit(0)

	@check("compiles")
	def test_longest_line(self):
		"""handles longest possible line correctly"""
		self.spawn("./dde").stdin("2").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c dd").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c dd").stdout("a b c d e f g h i 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 dd").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 10").exit(0)

	@check("compiles")
	def test_kafka_text(self):
		"""handles kafka text correctly"""
		self.spawn("./dde").stdin("5")..stdin("one morning when gregor samsa woke from troubled dreams he found himself").stdin("transformed in his bed into a horrible vermin he lay on his armour like back and").stdin("if he lifted his head a little he could see his brown belly slightly domed and").stdin("divided by arches into stiff sections the bedding was hardly able to cover it").stdin("and seemed ready to slide off any moment his many legs pitifully thin compared").stdout("one morning when gregor samsa woke from troubled dreams he found himself").stdout("transformed in his bed into a horrible vermin 10 lay on 15 armour like back and").stdout("if 10 lifted 15 head 18 little 10 could see 15 brown belly slightly domed 26").stdout("divided by arches 17 stiff sections the bedding was hardly able to cover it").stdout("26 seemed ready 47 slide off any moment 15 many legs pitifully thin compared").exit(0)
