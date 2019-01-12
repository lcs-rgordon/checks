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
	def test_max_lines_input(self):
		"""handles maximum number of lines correctly"""
		self.spawn("./dde").stdin("50").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdin("a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d e f g h i a b c d").stdout("a b c d e f g h i 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").stdout("1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4").exit(0)

	@check("compiles")
	def test_many_unique_words_input(self):
		"""handles 30 lines of mainly unique words correctly"""
		self.spawn("./dde").stdin("30").stdin("zth ang pmt zfb kwl dmd fqq bxz ckh unl tie ocz ute qgn djr acz irl qqs xdm mib").stdin("zzk drx yru sub rmq opc fso mnx ksc afr pon cmy knv rop xok xbf dor alq dsv gbf").stdin("zmu kxy tac kig zga tum nva qgn zdv vjy apc ral jkc hjz wen nps gil ujt wjg awi").stdin("whm vqk nmh pil vbd ydd eav lhg bsg jwl wzd kpg qyg ogf vup hft gpr rfy uqf dwh").stdin("ght lym afl tla poh guq rvf gmb trh skx zoi jhu rzf ubn eww off vpj wnx zze pcn").stdin("lxq tgf pnr vho ewi wcm jhi xfb dka pos aos vtc uow rwo znu lrm kyt ryd bhv jtz").stdin("lxq tgf pnr vho ewi wcm jhi xfb dka pos aos vtc uow rwo znu lrm kyt ryd bhv jtz").stdin("cwk bhr wvi atf pbq pfv xto ony vzf inb mxm cdm zxz ydt xhg rap raz fpu iye hvz").stdin("zzk drx yru sub rmq opc fso mnx ksc afr pon cmy knv rop xok xbf dor alq dsv gbf").stdin("skk shz gdn oxy fmi mmu uad ggs esa xjy qop lmx hal med yyy wlk ihl ltp mrw dft").stdin("egw ehg omq qzg gqy nju crc ywk erg qft gka qzp zoo yvu gnb lca xzr rbt cyi mff").stdin("ssa mta btc xyu ove vpm fwd wup jnn dmk wrx yzo cyw fdj yqt hyn bzo dbc qwv mkn").stdin("ssa mta btc xyu ove vpm fwd wup jnn dmk wrx yzo cyw fdj yqt hyn bzo dbc qwv mkn").stdin("nmn gfr wwe sjw uaa qhv noj ehj lgr jsz tjq cyu eek nwj rhl bly ssp qkv hkj jgt").stdin("cwk bhr wvi atf pbq pfv xto ony vzf inb mxm cdm zxz ydt xhg rap raz fpu iye hvz").stdin("kju uvf uau ofz tpv nav jmm wui llo tlx cgm zcm xwc kps ekm ixa xwh ynj ldu yby").stdin("uwq krb ptt pzl mks fzf lfh ino mkf cti voc ceh yyx vbq jty lrr fdw cob yad wmp").stdin("ssa mta btc xyu ove vpm fwd wup jnn dmk wrx yzo cyw fdj yqt hyn bzo dbc qwv mkn").stdin("bdm miv bji epu ylg bvi lea vmi uux fap fnq ctt zsg ioa gjl daw plr ypn vsg zuc").stdin("eio kzm pap uoq txl rhh gkl kpm cot lmt hqo iuh kai lwv mcu dwx lnl ahy aab sqv").stdin("rnm ruu ptp oao qxj rcu kmh unz smi xoy smi tll mln jzg dis nrq hyl cva nvf fny").stdin("kju uvf uau ofz tpv nav jmm wui llo tlx cgm zcm xwc kps ekm ixa xwh ynj ldu yby").stdin("uwq krb ptt pzl mks fzf lfh ino mkf cti voc ceh yyx vbq jty lrr fdw cob yad wmp").stdin("ssa mta btc xyu ove vpm fwd wup jnn dmk wrx yzo cyw fdj yqt hyn bzo dbc qwv mkn").stdin("fba gge sud rmq cqu xts hta rmp aze xof lgn str dom dux oac pxc cfm qsl ftw kmo").stdin("tky tww jae exe cjn ttz xfb zsp cbt boh rtj jfo yyi bih dgc zak fcq hrk pse wni").stdin("zbs ynn apc dhg khl jzz yso fji vqa xyw khh fbh vil kea hgi xxp npz zle tof gsd").stdin("ccp yny znc bsz btt jtt oab qbi dxu saa hoq bbl lug icn waf xjn jpk ayz wwe taf").stdin("zij pxe pzs cid mjc szv uha ypm szl enn iqx egx wct asr mlw ykz pac uzn apq pfm").stdin("irt rfm omb cre pcr bwg clc swy bdo nro vpo lnh vtl roj mvf zrf xzx gur zrd lyl").stdout("zth ang pmt zfb kwl dmd fqq bxz ckh unl tie ocz ute qgn djr acz irl qqs xdm mib").stdout("zzk drx yru sub rmq opc fso mnx ksc afr pon cmy knv rop xok xbf dor alq dsv gbf").stdout("zmu kxy tac kig zga tum nva 14 zdv vjy apc ral jkc hjz wen nps gil ujt wjg awi").stdout("whm vqk nmh pil vbd ydd eav lhg bsg jwl wzd kpg qyg ogf vup hft gpr rfy uqf dwh").stdout("ght lym afl tla poh guq rvf gmb trh skx zoi jhu rzf ubn eww off vpj wnx zze pcn").stdout("lxq tgf pnr vho ewi wcm jhi xfb dka pos aos vtc uow rwo znu lrm kyt ryd bhv jtz").stdout("100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119").stdout("cwk bhr wvi atf pbq pfv xto ony vzf inb mxm cdm zxz ydt xhg rap raz fpu iye hvz").stdout("21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40").stdout("skk shz gdn oxy fmi mmu uad ggs esa xjy qop lmx hal med yyy wlk ihl ltp mrw dft").stdout("egw ehg omq qzg gqy nju crc ywk erg qft gka qzp zoo yvu gnb lca xzr rbt cyi mff").stdout("ssa mta btc xyu ove vpm fwd wup jnn dmk wrx yzo cyw fdj yqt hyn bzo dbc qwv mkn").stdout("180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199").stdout("nmn gfr wwe sjw uaa qhv noj ehj lgr jsz tjq cyu eek nwj rhl bly ssp qkv hkj jgt").stdout("120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139").stdout("kju uvf uau ofz tpv nav jmm wui llo tlx cgm zcm xwc kps ekm ixa xwh ynj ldu yby").stdout("uwq krb ptt pzl mks fzf lfh ino mkf cti voc ceh yyx vbq jty lrr fdw cob yad wmp").stdout("180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199").stdout("bdm miv bji epu ylg bvi lea vmi uux fap fnq ctt zsg ioa gjl daw plr ypn vsg zuc").stdout("eio kzm pap uoq txl rhh gkl kpm cot lmt hqo iuh kai lwv mcu dwx lnl ahy aab sqv").stdout("rnm ruu ptp oao qxj rcu kmh unz smi xoy 308 tll mln jzg dis nrq hyl cva nvf fny").stdout("220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239").stdout("240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259").stdout("180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199").stdout("fba gge sud 25 cqu xts hta rmp aze xof lgn str dom dux oac pxc cfm qsl ftw kmo").stdout("tky tww jae exe cjn ttz 107 zsp cbt boh rtj jfo yyi bih dgc zak fcq hrk pse wni").stdout("zbs ynn 50 dhg khl jzz yso fji vqa xyw khh fbh vil kea hgi xxp npz zle tof gsd").stdout("ccp yny znc bsz btt jtt oab qbi dxu saa hoq bbl lug icn waf xjn jpk ayz 202 taf").stdout("zij pxe pzs cid mjc szv uha ypm szl enn iqx egx wct asr mlw ykz pac uzn apq pfm").stdout("irt rfm omb cre pcr bwg clc swy bdo nro vpo lnh vtl roj mvf zrf xzx gur zrd lyl").exit(0)

	@check("compiles")
	def test_kafka_text(self):
		"""handles kafka text correctly"""
		self.spawn("./dde").stdin("5").stdin("one morning when gregor samsa woke from troubled dreams he found himself").stdin("transformed in his bed into a horrible vermin he lay on his armour like back and").stdin("if he lifted his head a little he could see his brown belly slightly domed and").stdin("divided by arches into stiff sections the bedding was hardly able to cover it").stdin("and seemed ready to slide off any moment his many legs pitifully thin compared").stdout("one morning when gregor samsa woke from troubled dreams he found himself").stdout("transformed in his bed into a horrible vermin 10 lay on 15 armour like back and").stdout("if 10 lifted 15 head 18 little 10 could see 15 brown belly slightly domed 26").stdout("divided by arches 17 stiff sections the bedding was hardly able to cover it").stdout("26 seemed ready 47 slide off any moment 15 many legs pitifully thin compared").exit(0)
