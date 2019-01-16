from check50 import *

class PartnerUp(Checks):

	@check()
	def exists(self):
		"""partnerup.c exists"""
		self.require("partnerup.c")

	@check("exists")
	def compiles(self):
		"""partnerup.c compiles"""
		self.spawn("clang -o partnerup partnerup.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_odd_number(self):
		"""odd number of students rejected (could everyone have a unique partner?)"""
		self.spawn("./partnerup").stdin("13").stdin("Eddie Eric Geoff Jennifer Jheeven Kevin Matt Matthew Octavio Ryan Umai Zach Zeech").stdin("Zeech Zach Umai Ryan Octavio Matthew Matt Kevin Jheeven Jennifer Geoff Eric Eddie").stdout("bad").exit(0)
		
	@check("compiles")
	def test_simple_reverse(self):
		"""given list of students is simply reversed in second line"""
		self.spawn("./partnerup").stdin("6").stdin("Eddie Eric Geoff Jennifer Jheeven Kevin").stdin("Kevin Jheeven Jennifer Geoff Eric Eddie").stdout("good").exit(0)

	@check("compiles")
	def test_smallest_case(self):
		"""smallest number of students"""
		self.spawn("./partnerup").stdin("2").stdin("Eddie Umai").stdin("Umai Eddie").stdout("good").exit(0)

	@check("compiles")
	def test_largest_case(self):
		"""test the largest number of students"""
		self.spawn("./partnerup").stdin("30").stdin("Carlene Carmon Celinda Chan Edris Enda Etha Fernande Hyun Ignacio Janiece Juliana Kerry Kristofer Mayme Meghan Nancee Nicolasa Octavia Odell Raquel Renate Sherill Sindy Tameika Tamisha Tiffani Valentina Vina Ward").stdin("Ward Vina Valentina Tiffani Tamisha Tameika Sindy Sherill Renate Raquel Odell Octavia Nicolasa Nancee Meghan Mayme Kristofer Kerry Juliana Janiece Ignacio Hyun Fernande Etha Enda Edris Chan Celinda Carmon Carlene").stdout("good").exit(0)

	@check("compiles")
	def test_split_list(self):
		"""partners are consistent with something other than a simple reversal of first list order"""
		self.spawn("./partnerup").stdin("4").stdin("McRae Gordon Harris McGill").stdin("Harris McGill McRae Gordon").stdout("good").exit(0)

	@check("compiles")
	def test_all_assigned_self(self):
		"""partners all assigned to self"""
		self.spawn("./partnerup").stdin("6").stdin("Alice Bobby Charlie David Earl Frank").stdin("Alice Bobby Charlie David Earl Frank").stdout("bad").exit(0)

	@check("compiles")
	def test_double_self_assignment(self):
		"""two partners assigned to self"""
		self.spawn("./partnerup").stdin("6").stdin("Gary Harriet Ilana Jason Karl Laura").stdin("Jason Karl Ilana Gary Harriet Laura").stdout("bad").exit(0)

	@check("compiles")
	def test_four_wrong(self):
		"""four partners inconsistent"""
		self.spawn("./partnerup").stdin("6").stdin("Matthew Nancy Olivia Patty Quincy Robert").stdin("Quincy Robert Patty Nancy Matthew Olivia").stdout("bad").exit(0)