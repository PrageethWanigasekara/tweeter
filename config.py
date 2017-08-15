from combineCSV import combCSV
from clustering import clustering

#class_Combine = combCSV('combinedNew.csv')
#class_Combine.readCSV('tokenDatanew.csv','tokenDatanew2.csv')

class_Cluster = clustering('combinedNew.csv')
#class_Cluster.pca()
#print class_Cluster.top_words()
#print class_Cluster.getFrequency()
class_Cluster.write()




print 'End of the code'














