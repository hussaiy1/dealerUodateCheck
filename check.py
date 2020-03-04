# import files
import pandas as pd
import numpy as np

fileHeaders = ['UniqueDealerID', 'MaritzDealerCode', 'CountryCode', 'DealerType', 'DealerFac', 'BAC_Code', 'GMDealerCode', 'DealerName', 'DealerAddress1', 'DealerAddress2', 'DealerAddress3', 'DealerAddress4', 'DealerAddress5', 'DealerAddress6', 'Active','InActiveDate', 'Buick', 'Cadillac', 'Chevrolet', 'GMC', 'Holden', 'Isuzu', 'Opel', 'Vauxhall', 'HotAlertEmail1', 'HotAlertEmail2', 'HotAlertEmail3', 'HotAlertEmail4', 'HotAlertEmail5', 'Open1', 'Open2', 'Open3', 'Open4', 'Open5', 'DealerTimeZone', 'DealerLanguage']

file1 = pd.read_excel('20200219 - CA Live Dealer File.xlsx')
file2 = pd.read_excel('20200214 - CA Live Dealer File.xlsx')


def replaceNan():
    for i in range(0, len(fileHeaders)):
        file1[fileHeaders[i]] = file1[fileHeaders[i]].replace(np.nan, 0)
        file2[fileHeaders[i]] = file2[fileHeaders[i]].replace(np.nan, 0)


def compareColumns():
    for i in range(0, len(fileHeaders)):
        file1[fileHeaders[i]+'?'] = np.where(file1[fileHeaders[i]] == file2[fileHeaders[i]], 'True', 'False')

replaceNan()

compareColumns()

file1.to_csv(r'output.csv', index=False)

#or i in range(0, len(file1.index)):
#   for j in range(0, len(file1.columns)):
#       rowcompare=file2.values[i]==file1.values[i]
#       print(rowcompare)


#output to file and filter for false


#file1compare= file1.equals(file1)
#row1f1 = file1.iloc[0]['MaritzDealerCode']
#row1f2 = file2.iloc[0]['MaritzDealerCode']

#rowcompare = row1f1==row1f2
#print(np.isnan(row1f1))
#print(rowcompare)


#check the difference between two files
#highlight the differences
### OUTPUT to excel


