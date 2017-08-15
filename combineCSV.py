import csv

class combCSV:
    def __init__(self,fileOut):
        self.outFile = fileOut
    
    def readCSV(self,file_name1,file_name2):
        print 'Running Class combCSV.. readCSV method'
        csvFileWrite = open(self.outFile, 'a')      #combinedNew.csv
        csvWriter = csv.writer(csvFileWrite)

        #file1
        csvfile1 = open(file_name1, 'rb')
        spamreader1 = csv.reader(csvfile1)
        for row in spamreader1:
            if len(row[5])>2:
                csvWriter.writerow([row[0],row[1],row[2],row[3],row[4],row[5].lower(),row[6]])

        #file2
        csvfile2 = open(file_name2, 'rb')
        spamreader2 = csv.reader(csvfile2)
        for row in spamreader2:
            if len(row[5])>2:
                csvWriter.writerow([row[0],row[1],row[2],row[3],row[4],row[5].lower(),row[6]])
        

        csvFileWrite.close()    
        return        


#readCSV('tokenDatanew.csv','tokenDatanew2.csv')
