import sys
from xml.dom import minidom
from rdflib import Graph



if __name__ == '__main__':

	if len(sys.argv)!=3:
		print "python precision.py output annotated"
		sys.exit(1)

	xmldocAnn = minidom.parse(sys.argv[1])
	itemlistAnn = xmldocAnn.getElementsByTagName('sentence')

	xmldocRes = minidom.parse(sys.argv[2])
	itemlistRes = xmldocRes.getElementsByTagName('sentence')

	ann = dict()
	for el in itemlistAnn:
		id = int(el.getAttribute("id"))
		pol = int(el.getElementsByTagName("polarity")[0].firstChild.data)
		ann[id] = pol

	res = dict()
	for el in itemlistRes:
		id = int(el.getAttribute("id"))
		pol = int(el.getElementsByTagName("polarity")[0].firstChild.data)
		res[id] = pol

	tp = 0
	fp = 0
	tn = 0
	fn = 0
	for el in res:
		if res[el]==ann[el]:
			if res[el]==0:
				tn = tn + 1
			if res[el]==1:
				tp = tp + 1
		if res[el]!=ann[el]:
			if res[el]==0:
				fn = fn + 1
			if res[el]==1:
				fp = fp + 1

	missing = len(ann) - len(res)
	print "tp,fp,tn,fn : ",tp,fp,tn,fn

	precision = tp / (tp + fp)
	recall = tp / (tp + fn)

	print "precision:",precision
	print "recall:",recall
	F1 = 2 * precision * recall / (precision + recall)
	print "F1:",F1
	print "missing : ",missing
