#!/usr/bin/env python
# mapper_2.py
import sys
import re
import math
import numpy as np

list = []
inStatus = False
inText = False
inTime = False

def readSentimentList(file_name):
    ifile = open(file_name, 'r')
    happy_log_probs = {}
    sad_log_probs = {}
    ifile.readline() #Ignore title row
    
    for line in ifile:
        tokens = line[:-1].split(',')
        happy_log_probs[tokens[0]] = float(tokens[1])
        sad_log_probs[tokens[0]] = float(tokens[2])

    return happy_log_probs, sad_log_probs

def classifySentiment(words, happy_log_probs, sad_log_probs):
    # Get the log-probability of each word under each sentiment
    happy_probs = [happy_log_probs[word] for word in words if word in happy_log_probs]
    sad_probs = [sad_log_probs[word] for word in words if word in sad_log_probs]

    # Sum all the log-probabilities for each sentiment to get a log-probability for the whole tweet
    tweet_happy_log_prob = np.sum(happy_probs)
    tweet_sad_log_prob = np.sum(sad_probs)

    # Calculate the probability of the tweet belonging to each sentiment
    prob_happy = np.reciprocal(np.exp(tweet_sad_log_prob - tweet_happy_log_prob) + 1)
    prob_sad = 1 - prob_happy

    return prob_happy, prob_sad

happy_log_probs, sad_log_probs = readSentimentList('twitter_sentiment_list.csv')

time = []

for line in sys.stdin:
    line = line.strip()
    if inText:
        list.append(line)
    if inTime:
        time.append(line)
    if line.find( "<status>" ) != -1:
        inStatus = True
        continue
    if line.find( "</status>" ) != -1:
        inStatus = False
        continue
    if inStatus and line.find("<created_at>") != -1:
        inTime = True
	time = line
	time = time[12:21]
	inTime = False
        continue
    if inStatus and line.find( "<text>" ) != -1:
        inText = True
	if line.find("</text>"):
		temp = line.lower()
		temp = temp.decode("utf-8")
		text_new  = temp.split()
	        happy_prob, sad_prob = classifySentiment(text_new, happy_log_probs, sad_log_probs)
        	score = math.log(happy_prob/sad_prob)
        	print(score,time)
		inText = False
        	list = []
        	time = []
		continue
	else:
        	continue
    if inStatus and line.find( "</text>" ) != -1:
        inText = False
        text = ' '.join(list)
        temp = text.lower()
	temp = temp.decode("utf-8")
	text_new  = temp.split()
        happy_prob, sad_prob = classifySentiment(text_new, happy_log_probs, sad_log_probs)
        score = math.log(happy_prob/sad_prob)
        print(score,time)
        list = []
        time = []
        continue
    


