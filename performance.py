from sklearn.externals import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import graphviz
from sklearn import tree
import pydotplus

class Performance:
    def __init__(self,labels,test_features):
        self.Y_true = pd.read_csv(labels, sep=" ", header=None)
        self.X_test = pd.read_csv(test_features, sep=" ", header=None)
        #self.list = 'SVM_model.pkl','NearestNei_model.pkl','LogReg_model.pkl','DecisionTree.pkl'
        self.list = 'DecisionTree.pkl','SVM_model.pkl'
    
    def testModels(self):
        pred_list = []
        for i in range(0,len(self.list)):
            clf = joblib.load(self.list[i])
            clf = tree.DecisionTreeClassifier(max_depth=3)
            result = clf.predict(self.X_test)
            pred_list.append(result)

            #colnames=df.columns.values.tolist()
            #Xlabels='non disaster','disaster' # feature names
            #ynames=y.unique().tolist() # class names
            

            dot_data = tree.export_graphviz (clf , out_file =None,
            filled=True, rounded=True,
            special_characters =True)

            graph = pydotplus.graph_from_dot_data(dot_data)
            graph.write_png("zoo.png")

        return pred_list


    def write(self):
        file = open("labels_test.text", "w")
        a = self.testModels()
        for item in a:
            str1 = ''.join(str(item))
            str1 = str1.replace(',', '')
            #print str1
            #item = ''.join(str(item))  
            file.write("%s\n" % str1.strip('[,]'))
        file.close()


    def read(self):
        Y = pd.read_csv('labels_test.text',error_bad_lines=False, sep=" ", header=None)
        for i in range(0,4):
            Y_pred = Y.loc[i]
            print "accuracy: ",accuracy_score(self.Y_true, Y_pred)
            print "precision: ",precision_score(self.Y_true, Y_pred, average='macro')
            print "recall: ",recall_score(self.Y_true, Y_pred, average='macro')
            print "\n"

"""
    def accuracy(self):
        #accuracy_score(y_true, y_pred)
        #accuracy_score(y_true, y_pred, normalize=False)


    def precision(self):
        #precision_score(y_true, y_pred, average='macro')  
        #precision_score(y_true, y_pred, average='micro')  
        #precision_score(y_true, y_pred, average='weighted')
        #precision_score(y_true, y_pred, average=None) 


    def recall(self):
        #recall_score(y_true, y_pred, average='macro')  
        #recall_score(y_true, y_pred, average='micro')  
        #recall_score(y_true, y_pred, average='weighted')  
        #recall_score(y_true, y_pred, average=None)

"""


    #clf = joblib.load('filename.pkl') 
    #clf.predict()





 




























