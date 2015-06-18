# ESWC-CLSA
ESWC-15 Challenge on Concept-Level Sentiment Analysis

Check the <a href="https://github.com/diegoref/ESWC-CLSA/wiki">wiki</a> page to see more details



-----------------
June 18, 2015
-----------------
<b>Results of the challenge</b><br>
<i>Task 1:</i><br>
KIM - Accuracy: 0.4129<br>
FBK - Accuracy: 0.4078<br>
SENTILO - Accuracy: 0.3011<br>
<br>
<b>KIM is the winner of task 1 and is awarded with a Springer voucher of 150 euros</b>
<br><br>
<i>Task 3:</i><br>
FBK - Precision: 0.3996; Recall: 0.5336; F1: 0.4570<br>
<br>
<b>FBK is the winner of task 3 and is awarded with a Springer voucher of 150 euros</b>
<br><br>
<i>Most Innovative Approach</i><br>
SENTILO - The system builds on top of Discourse Representation Theory, relies on VerbNet for identifying and formalizing events and their associated thematic roles. SENTILO uses FRED which transforms such logical form to RDF by complying to Semantic Web and Linked Data design principles, and by extending the representation model with event- and situation- semantics as formally defined by DOLCE+DnS ontology. A new sentiment ontology is developed, OntoSentilo, that defines concepts and relations that characterize the entities composing an opinion sentence (opinion trigger events, holders, topics and subtopics, opinion features).
<br>
<b>SENTILO is the winner of the "most innovative approach" and is awarded with a Springer voucher of 150 euros</b>



-----------------
June 18, 2015
-----------------
Added <i><a href='https://github.com/diegoref/ESWC-CLSA/blob/master/task1Challenge_testGold.zip'>task1Challenge_testGold.zip</a></i> and <i><a href='https://github.com/diegoref/ESWC-CLSA/blob/master/task3Challenge_testGold.zip'>task3Challenge_testGold.zip</a></i>. These are the two testset where systems have to be run on. Results will be sent in the required format.


Please check the wiki for further information.

To ask questions and information please join our mailing list at http://groupspaces.com/ESWC2015-CLSA.<br>
After you join the group, you can post messages to the mailing list address ESWC2015-CLSA@groupspaces.com



-----------------
March 13, 2015
-----------------
Added <i>task3_CLSA.zip</i><br>
It contains the xml annotated file for testing your system.

The output of your system for task3 should use the same structure of task3AnnotatedChallenge.xml. You do not need to report the <text>...</text> content. You need to indicate the <sentence>...</sentence> and all the other tags.

You can then use <i>precisionTask3.py</i> to evaluate your results using:

<i>python precisionTask3.py task3AnnotatedChallenge.xml yourFileResults.xml</i>


Please check the wiki for further information.

To ask questions and information please join our mailing list at http://groupspaces.com/ESWC2015-CLSA.<br>
After you join the group, you can post messages to the mailing list address ESWC2015-CLSA@groupspaces.com



-----------------
February 21, 2015
-----------------

Added <i>task2_CLSA.zip</i><br>
It contains the xml annotated file for testing your system.

The dataset has been taken from SemEval2015 Task12: Aspect Based Sentiment Analysis <a href="http://alt.qcri.org/semeval2015/task12/">http://alt.qcri.org/semeval2015/task12/</a><br>
The task has been proposed for the first time during ESWC2014 for the Challenge on Concept-Level Sentiment Analysis 2014, the first edition of this current challenge. Then, the task has been reproposed by SemEval2015.

File <i>precisionTask2.zip</i> contains the instructions on how to run the precision recall analysis for the Task2.

Please check the wiki for further information.


To ask questions and information please join our mailing list at http://groupspaces.com/ESWC2015-CLSA.<br>
After you join the group, you can post messages to the mailing list address ESWC2015-CLSA@groupspaces.com



-----------------
February 18, 2015
-----------------

Added <i>task1_CLSA.zip</i><br>
It contains the task1AnnotatedChallenge.xml annotated file for testing your system.

The output of your system for task1 should use the same structure of task1AnnotatedChallenge.xml. You do not need to report the <text>...</text> content. You need to indicate the <sentence>...</sentence> and <polarity>...</polarity> tags.

You can then use <i>precisionTask1.py</i> to evaluate your results using:

<i>python precisionTask1.py task1AnnotatedChallenge.xml yourFileResults.xml</i>


Please check the wiki for further information.

To ask questions and information please join our mailing list at http://groupspaces.com/ESWC2015-CLSA.<br>
After you join the group, you can post messages to the mailing list address ESWC2015-CLSA@groupspaces.com



