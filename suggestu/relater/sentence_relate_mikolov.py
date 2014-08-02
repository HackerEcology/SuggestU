from __future__ import with_statement
from numpy import linalg as LA
import re
import numpy
import scipy
import scipy.spatial
import scipy.stats as sstats
import shelve
import linecache
from gensim.models import Word2Vec

vspace = Word2Vec.load_word2vec_format('word2vec/GoogleNews-vectors-negative300.bin', binary=True)  # C binary format

small_test_rel_pronouns = ["that","who","which","what","where","whose"]
prepositions_basic = ["as","at","but","by","down","for","from","in","into","like","near","next","of","off","on","onto","out","over","past","plus","minus","since","than","to","up","with"]
prepositions_advanced = ["aboard","about","above","across","after","against","along","around","before","behind","below","beneath","beside","between","beyond","during","except","following","inside","minus","onto","opposite","outside","round","since","through","toward","under","underneath","unlike","until","upon","without"]
determinators = ["the","a","an"]
prepositions_bnc = ['by', 'through', 'with', 'from', 'of', 'for', 'without', 'out', 'at', 'as', 'in', 'on', 'like', 'about', 'after', 'during', 'into', 'before', 'over', 'despite', 'around', 'against', 'between', 'under', 'beyond', 'until', 'via', 'within', 'since', 'upon', 'among', 'across', 'unlike', 'than', 'near', 'outside', 'towards', '\xe2\x80\x94', 'behind', 'up', 'because', 'per', 'above', 'alongside', 'inside', 'except', 'en', 'throughout', 'off', 'along', 'toward', 'amid', 'instead', 'whereas', 'besides', 'beside', 'beneath', 'past']

insigwords = small_test_rel_pronouns + prepositions_basic + prepositions_advanced + determinators + prepositions_bnc

test = ['animal loves milk','a cat']

def returnPossibleKeys(sentenceString):
	print [x for x in sentenceString.split() if (x.lower() not in insigwords)]
	return [x for x in sentenceString.split() if (x.lower() not in insigwords)]

# this is the additive model, but usually it works well
def verySimpleModelMikolov(sentence1,sentence2):
	bagS1 = returnPossibleKeys(sentence1.strip())
	bagS2 = returnPossibleKeys(sentence2.strip())
	if len(bagS1) == 0 or len(bagS2) == 0:
		print "111"
		return -2
	else:
		try:
			sVector1 = vspace[bagS1[0]]
			for ss in bagS1[1:]:
				try:
					sVector1 = numpy.add(sVector1,vspace[ss])
				except:
					pass
			sVector2 = vspace[bagS1[0]]
			for ss in bagS1[1:]:
				try:
					sVector2 = numpy.add(sVector2,vspace[ss])
				except:
					pass
			try:
				cos = scipy.spatial.distance.cosine(sVector1,sVector2)
				print cos
				return cos
			except:
				return -4
		except:
			return -3

print verySimpleModelMikolov(test[0],test[1])
