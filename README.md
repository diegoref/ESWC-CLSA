# ESWC-CLSA
ESWC-15 Challenge on Concept-Level Sentiment Analysis

Check the <a href="https://github.com/diegoref/ESWC-CLSA/wiki">wiki</a> page to see more details


-----------------
June 18, 2015
-----------------
Added <i>task1Challenge_testGold.xml</i> and <i>task3Challenge_testGold.xml</i>. These are the two testset where systems have to be run on. Results will be sent in the required format.


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



