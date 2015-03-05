import sys
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.alldata = dict()
		self.currentSentence = ""
		self.currentTag = ""
		self.currentAspect = ""

	def handle_starttag(self, tag, attrs):
		self.current_tag = tag
		if tag=="aspect":
			#print "ATTRS:",attrs[0][1]
			for el in attrs:
				if el[0]=="rdf:resource":
					self.alldata[self.currentSentence]["aspects"][el[1].strip()]=dict()
					self.currentAspect = el[1].strip()

    	def handle_endtag(self, tag):
		self.current_tag = ""
									  
	def handle_data(self, data):
		data = data.strip()
		if self.current_tag=="text":
			self.currentSentence = data
			self.alldata[data] = dict()
			self.alldata[data]["aspects"]=dict()
			#self.alldata[data]["polarity"]=list()
		if self.current_tag=="polarity":
			self.alldata[self.currentSentence]["aspects"][self.currentAspect] = data

if __name__ == '__main__':
	if len(sys.argv)!=3:
		print "python precision.py output annotated"
		sys.exit(1)

	fout = open(sys.argv[1],'r')
	fann = open(sys.argv[2],'r')

	cont = 0

	contentOut = ""
	contentAnn = ""
	for el in fout:
		contentOut = contentOut + el.strip()

	for el in fann:
		contentAnn = contentAnn + el.strip()
	fout.close()
	fann.close()

	parserOut = MyHTMLParser()
	parserOut.feed(contentOut)


	parserAnn = MyHTMLParser()
	parserAnn.feed(contentAnn)


	# EXTRACTION TASK
	processed = 0
	notprocessed = 0
	tp = 0
	fp = 0
	tn = 0
	fn = 0
	tpp = 0
	fpp = 0

	tp_paper = 0
	fp_paper = 0
	fn_paper = 0

	for sent in parserAnn.alldata:
		aspectsAnn = parserAnn.alldata[sent]["aspects"]
		aspectsOut = parserOut.alldata[sent]["aspects"]
		if sent not in parserOut.alldata:
			notprocessed = notprocessed + 1
			continue
		else:
			processed = processed + 1
		for el in aspectsAnn:
			if el in aspectsOut:
				tp = tp + 1.0
				if aspectsAnn[el]==aspectsOut[el]:
					tpp = tpp + 1
					tp_paper = tp_paper + 1
				else:
					fpp = fpp + 1
					fn_paper = fn_paper + 1.0
			else:
				fn = fn + 1.0
				fn_paper = fn_paper + 1.0

		for el in aspectsOut:
			if el not in aspectsAnn:
				fp = fp + 1.0
				fp_paper = fp_paper + 1.0
	
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	F1 = 2 * precision * recall / (precision + recall)

	precision_paper = tp_paper / (tp_paper + fp_paper)
	recall_paper = tp_paper / (tp_paper + fn_paper)
	F1_paper = 2 * precision_paper * recall_paper / (precision_paper + recall_paper)
	
	print "tp:",tp
	print "fp:",fp
	print "tn:",tn
	print "fn:",fn
	print "tpp:",tpp
	print "fpp:",fpp
	print "processed:",processed
	print "notprocessed:",notprocessed
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
        
	print "precision:",precision
        print "recall:",recall
        F1 = 2 * precision * recall / (precision + recall)
        print "F1:",F1

	print "precision_paper:",precision_paper
	print "recall_paper:",recall_paper
	print "F1_paper:",F1_paper
	

