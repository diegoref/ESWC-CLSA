# ESWC-CLSA
ESWC-15 Challenge on Concept-Level Sentiment Analysis

February 18, 2015

Added task1_CLSA.zip
It contains the task1AnnotatedChallenge.xml annotated file for testing your systems.

The output of your system for task1 should use the same structure of task1AnnotatedChallenge.xml. You do not need to report the <text>...</text> content. You need to indicate the <sentence>...</sentence> and <polarity>...</polarity> tags.

You can then use precisionTask1.py to evaluate your results using:

python precisionTask1.py task1AnnotatedChallenge.xml yourFileResults.xml
