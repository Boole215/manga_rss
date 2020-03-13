import dill


class MangaTest:

	def __init__(self, name):
		self.myName = name;

	def retname(self):
		return self.myName;

#testobj = MangaTest("Kaguya");
dumpfile = open("pickle.dat","rb");

thisobj = dill.load(dumpfile);

print(thisobj.retname());

dumpfile.close();






