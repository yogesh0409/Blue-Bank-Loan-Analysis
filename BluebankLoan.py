import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

json_file=open('loan_data_json.json')
data=json.load(json_file)


#working with the json file to extract the fields
#transforming lists data into dataframe
loan=pd.DataFrame(data)

#checking info
loan.info()

#unique values
loan['purpose'].unique()


#summarzing the data
loan.describe()
loan['int.rate'].describe()
loan['fico'].describe()
loan['dti'].describe()
loan['installment'].describe()


#expotentialing the log.annual field to get the actual anuual income
loan['annualincome']=np.exp(loan['log.annual.inc'])



#getting the cibil score(fico)
#cibil score check

#Conditions to check cibil score 
#fico >= 300 and < 400:'Very Poor'
#fico >= 400 and ficoscore < 600:'Poor'
#fico >= 601 and ficoscore < 660:'Fair'
#fico >= 660 and ficoscore < 780:'Good'
#fico >=780:'Excellent

#appling for loop for loan data
length =len(loan)
ficocat = []
for x in range(0,length):
    category = loan['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >=400 and category < 600:
            cat = 'Poor'
        elif category >=601 and category < 660:
            cat = 'Fair'
        elif category >=660 and category < 700:
            cat = 'Good'
        elif category >700:
            cat ='Excellent'
        else:
            cat ='Unknown'
    except:
        cat ='Error-Unknown'
    ficocat.append(cat)
#converting into series



ficocat = pd.Series(ficocat)

loan['fico.category'] =ficocat



#df.loc as conditional statement

loan.loc[loan['int.rate'] >0.12, 'int.rate.type'] = 'High'
loan.loc[loan['int.rate'] <=0.12, 'int.rate.type'] = 'Low'


#visualization
#1.Grouping the data
catplot= loan.groupby(['fico.category']).size()
purplot= loan.groupby(['purpose']).size()

#category plot
catplot.plot.bar(color='green')
plt.show()


#purpose plot
purplot.plot.bar()
plt.show()


#DTI
ypoint=loan['annualincome']
xpoint=loan['dti']

plt.scatter(xpoint,ypoint,color='red')
plt.show()

#exporting the dataset

loan.to_csv('loan_cleaned.csv',index=True)
 
    
    
        
    











