import sys
from xml.dom import minidom
from rdflib import Graph
import xml.etree.ElementTree as ET


def prec(ann,res,tip):
	tp = 0.0
	fp = 0.0
	fn = 0.0
	for sent in ann:
	#	print "sent:",sent
	#	print "FRAME:",ann[sent]
		for frame in ann[sent]:
			if tip==3:
				pp = frame[tip-1]
			hh = frame[tip]
			found = False
			if sent not in res:
				print "Some id sentences of the test set are not present in results. Please fix!"
				sys.exit(1)
			for frame1 in res[sent]:
				if tip==3:
					if frame1[tip].lower().strip() == hh.lower().strip() and pp.lower().strip()==frame1[tip-1].lower().strip():
						tp = tp + 1
						found = True
						break
				else:
					if frame1[tip].lower().strip() == hh.lower().strip():
						tp = tp + 1
						found = True
						break
			if found == False:
				fp = fp + 1
		for frame1 in res[sent]:
			if tip==3:
				pp = frame1[tip-1]
			hh = frame1[tip]
			found = False
			for frame in ann[sent]:
				if tip==3:
					if frame[tip].lower().strip() == hh.lower().strip() and pp.lower().strip() == frame[tip-1].lower().strip():
						found = True
						break
				else:		
					if frame[tip].lower().strip() == hh.lower().strip():
						found = True
						break
			if found == False:
				fn = fn + 1
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	F1 = 2 * precision * recall / (precision + recall)
	return precision,recall,F1,tp,fp,fn

if __name__ == '__main__':

	if len(sys.argv)!=3:
		print "python precisionTask3.py output annotated"
		sys.exit(1)

	xmldocAnn = minidom.parse(sys.argv[1])
	itemlistAnn = xmldocAnn.getElementsByTagName('sentence')

	xmldocRes = minidom.parse(sys.argv[2])
	itemlistRes = xmldocRes.getElementsByTagName('sentence')

	ann = dict()
	for el in itemlistAnn:
		id = int(el.getAttribute("id"))
		frames = list()
		for el1 in el.getElementsByTagName("frame"):
			hh = el1.getElementsByTagName("holder")[0].getAttribute("value")
			tt = el1.getElementsByTagName("topic")[0].getAttribute("value")
			oo = el1.getElementsByTagName("opinion")[0].getAttribute("value")
			pp = el1.getElementsByTagName("opinion")[0].getElementsByTagName("polarity")[0].firstChild.data
			frames.append((hh,tt,oo,pp))
		ann[id] = frames


	res = dict()
	for el in itemlistRes:
		id = int(el.getAttribute("id"))
		frames = list()
		for el1 in el.getElementsByTagName("frame"):
			hh = el1.getElementsByTagName("holder")[0].getAttribute("value")
			tt = el1.getElementsByTagName("topic")[0].getAttribute("value")
			oo = el1.getElementsByTagName("opinion")[0].getAttribute("value")
			pp = el1.getElementsByTagName("opinion")[0].getElementsByTagName("polarity")[0].firstChild.data
			frames.append((hh,tt,oo,pp))
		res[id] = frames

	prec_holder, recall_holder, f1_holder, tp_holder, fp_holder, fn_holder = prec(ann,res,0) #0 = holder
	prec_topic, recall_topic, f1_topic, tp_topic, fp_topic, fn_topic = prec(ann,res,1) #1 = topic
	prec_opinion, recall_opinion, f1_opinion, tp_opinion, fp_opinion, fn_opinion = prec(ann,res,2) #2 = opinion
	prec_oppol, recall_oppol, f1_oppol, tp_oppol, fp_oppol, fn_oppol = prec(ann,res,3) #3 = opinion and polarity

	print "holder:",prec_holder, recall_holder, f1_holder, tp_holder,fp_holder,fn_holder
	print "topic:",prec_topic, recall_topic, f1_topic, tp_topic,fp_topic,fn_topic
	print "opinion:",prec_opinion, recall_opinion, f1_opinion, tp_opinion,fp_opinion,fn_opinion
	print "oppol:",prec_oppol, recall_oppol, f1_oppol, tp_oppol,fp_oppol,fn_oppol

	print "Task3 precision",0.25*prec_holder+0.25*prec_topic+0.25*prec_opinion+0.25*prec_oppol
	print "Task3 recall",0.25*recall_holder+0.25*recall_topic+0.25*recall_opinion+0.25*recall_oppol
	print "Task3 F1",0.25*f1_holder+0.25*f1_topic+0.25*f1_opinion+0.25*f1_oppol
