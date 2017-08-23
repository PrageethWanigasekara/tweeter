import matplotlib.pyplot as plt
import numpy as np
import csv
from dateutil import parser
import datetime
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union  
from nltk.tokenize import PunktSentenceTokenizer  
from nltk.stem import WordNetLemmatizer
import re
from collections import Counter

######################################################################################################


places = ['AL','Alabama','AK','Alaska','AZ','Arizona','AR','Arkansas','CA','California','CO','Colorado','CT','Connecticut','DE','Delaware','FL','Florida','GA','Georgia','HI','Hawaii','ID','Idaho','IL','Illinois','Indiana','IA','Iowa','KS','Kansas','KY','Kentucky','LA','Louisiana', 'ME','Maine Augusta','MD','Maryland','MA','Massachusetts','MI','Michigan','MN','Minnesota','MS','Mississippi','MO','Missouri','MT','Montana','NE','Nebraska','NV','Nevada','NH','New Hampshire','NJ','New Jersey','NM','New Mexico','NY','New York','NC','North Carolina','ND','North Dakota','Ohio','Oklahoma','OR','Oregon','PA','Pennsylvania','RI','Rhode Island','SC','South Carolina','SD','South Dakota','TN','Tennessee','TX','Texas','UT','Utah','VA','Virginia','WA','Washington','WV','West Virginia','WI','Wisconsin','WY','Wyoming']



class preprocessing:

    def __init__(self,fileOut):
        self.outFile = fileOut

        
    def tokanizeData(self,text):
        try:
            token_words = word_tokenize(text)
            words = token_words
        except ValueError:
            a=text.decode('utf8')
            token_words = word_tokenize(a)
            words=[a.encode("utf-8") for a in token_words]
        return words

    def getHashtags(self,array):
        hashtag = []
        for i in range(0,len(array)):
            if array[i] == '#' and re.match("^[A-Za-z0-9_-]*$", array[i+1]):
                hashtag.append(array[i+1])
        return hashtag

         
    def removeCharacters(self,array):
        arrayNew= []
        i = 0
        while (i<len(array)):
            if array[i] == '#' or array[i] == '@' :
                i=i+1
            elif array[i] == 'https' or array[i] == 'http':
                i=i+1
            elif re.match("^[A-Za-z0-9_-]*$", array[i]):
                arrayNew.append(array[i])
                i=i+1
            else: 
                i=i+1
        return arrayNew



    def removeStopwords(self,array):
        stop_words = stopwords.words("english")
        filt=[]
        for w in array:
            if w.lower() not in stop_words:
                filt.append(w)
        return filt

    def stemwords(self,array):
        filt=[]
        for w in array:
            stemming_words = PorterStemmer().stem(w)
            filt.append(stemming_words)
        stemWords = words=[a.encode("utf-8") for a in filt]    
        return stemWords


    def getFrequency(self,array):
        filt=[]
        for w in array:
            filt.append(w.lower())
        words_to_count = (word for word in filt if word[:1])            
        c = Counter(words_to_count)
        return c.most_common(10)


    def getPlaces(self,array,hashs,places):
        filt=[]
        for i in array:
            for j in places:
                if i==j:
                    filt.append(i)
        for i in hashs:
            for j in places:
                if i==j:
                    filt.append(i)
        filt = list(set(filt))            
        return filt	    



############## read csv ######################
    def readCSV(self):
        
        csvfile = open(self.outFile, 'rb') 
        spamreader = csv.reader(csvfile)

        csvFileWrite = open('ExtractData.csv', 'a')
        csvWriter = csv.writer(csvFileWrite)
        #csvFileWrite.close()
        i=0
        for row in spamreader:
            i=i+1
            
            #print tokanizeData(row[2])
            initial=row[2]
            q = self.tokanizeData(row[2])
            #print getHashtags(q)
            hashs = self.getHashtags(q)
            edited1 = self.removeCharacters(q)
            edited2 = self.removeStopwords(edited1)
            edited4 = self.stemwords(edited2)
            #print edited1
            #print edited2
            #print getFrequency(edited2)
            edited3 = self.getPlaces(edited2,hashs,places)
                
            csvWriter.writerow([row[1],initial,q,self.getHashtags(q),edited1,edited4,edited3])
            #places = geograpy.get_place_context(text=row[2])
            #print places.countries
            #print places.regions
            #print places.cities
            #print '\n'
        csvFileWrite.close()    
        return        












