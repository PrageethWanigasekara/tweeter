import csv
from collections import Counter
from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
import pylab as pl

#[('flood', 268), ('flash', 50), ('report', 41), ('co', 38), ('warn', 34), ('counti', 26),
#('close', 26), ('due', 25), ('rd', 20), ('rain', 20), ('tx', 19), ('houston', 14)]

#[('like', 57), ('love', 44), ('go', 43), ('get', 38), ('got', 37), ('know', 34), ('amp', 32),
#('lol', 29), ('ca', 29), ('time', 28), ('good', 27), ('alway', 27), ('need', 27), ('shit', 26),
#('u', 25), ('see', 25), ('even', 24), ('feel', 24), ('day', 24), ('la', 24), ('friend', 23),
#('peopl', 23), ('one', 23), ('want', 22), ('make', 22)]
word_set = ['flood','flash','report','co','warn', 'counti','close','due','rd','rain',
            'like','love','go','get','got','know','amp','lol','ca','time']

class clustering:
    def __init__(self,fileIn):
        self.inFile = fileIn

    def checkCSV(self):    
        csvfile = open(self.inFile, 'rb') 
        spamreader = csv.reader(csvfile)
        filt = []
        listOfList = []
        i = 0  
        for row in spamreader:
            i=i+1
            c=row[5].replace("'","")
            d=c.strip('[,]')
            e=d.replace(',','')
            final=e.split()
            if len(final)>0:
                for word in word_set:
                    if word in final:
                        filt.append(1)
                    else:
                        filt.append(0)
                listOfList.append(filt)
                filt = []  
        return listOfList


    def pca(self):
        a = self.checkCSV()     
        X = np.array(a)
        pca = PCA(n_components=2).fit(X)
        pca_2d = pca.transform(X)   
        kmeans = KMeans(n_clusters= 2, init='k-means++', max_iter=300, n_init=10,random_state =1).fit(pca_2d)
        print(len(kmeans.labels_))

        array = []
        for i in range(0,len(kmeans.labels_)):
            array.append(str(kmeans.labels_[i]))
            

        for i in range(0, len(pca_2d)):
            if kmeans.labels_[i] == 0:
                c1 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='r', marker='o',s=15)
            elif kmeans.labels_[i] == 1:
                c2 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='g',marker='o',s=15)
         
        centroids = kmeans.cluster_centers_
        pl.scatter(centroids[:, 0], centroids[:, 1],marker='x',color='black')


        myclass = [i for i,j in zip(X, kmeans.labels_) if j==1]
        print len(myclass)

        pl.legend([c1, c2], ['non disaster', 'disaster'])
        pl.title('Tweet labeling (total 1334 (290+1044) tweets)')
        pl.show()


        
    def top_words(self):
        csvfile = open(self.inFile, 'rb') 
        spamreader = csv.reader(csvfile)
        filt = []
        j=1
        for row in spamreader:
            if len(row[5])>2 and j>290:
                c=row[5].replace("'","")
                d=c.strip('[,]')
                e=d.replace(',','')
                final=e.split()
                filt = filt + final
            j=j+1
        return filt


    def getFrequency(self):
        array = self.top_words()
        filt=[]
        for w in array:
            filt.append(w.lower())
        words_to_count = (word for word in filt if word[:1])            
        c = Counter(words_to_count)
        return c.most_common(25)  #top number


    def write(self):
        file = open("features.text", "w")
        a = self.checkCSV()
        for item in a:
            str1 = ''.join(str(item))
            str1 = str1.replace(',', '')
            #print str1
            #item = ''.join(str(item))  
            file.write("%s\n" % str1.strip('[,]'))
        file.close()  
                




       
#a=checkCSV('combinedNew.csv')
#then pca
#top_words
###########################################
"""
words = top_words('combinedNew.csv',5)
print 'Top words: ',getFrequency(words)



#to read, write i/o
file = open("features3.text", "w")
for item in a:
  item = ''.join(str(item))
  print item  
  file.write("%s\n" % item.strip('[,]'))
file.close()
"""


"""
file = open("train_labels.text", "r")
for line in file: 
    print line
"""




