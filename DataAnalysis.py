#######NOTE###########:
### USE PYTHON VERSION 3.X to run the following program #####################
###### AUTHOR : ARPIT AGARWAL ###############################################
############ COPYRIGHTS RESERVED ############################################

 
import pandas as pd # Use for Data Analysis, removes the Noise from data, handles them appropriately.
from pandas.io.json import json_normalize # Used to create Panda DataFrames from JSON Object.
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt


def getAnonymousUsers(data):#Function which return a dictionary with the count of Public and Private 1st Degree Connections
  ndict={'Public':0,'Private':0}
  vdict=data.to_dict()
  for k,v in vdict.items():
    if v=='private':
      ndict['Private']+=1
    else:
      ndict['Public']+=1
  return ndict



def getStats(data,others=[]):#Function which return a dictionary describing the data distribution.
  meanVal=data.value_counts().mean()
  vdata=data.value_counts()
  vdict=vdata.to_dict()
  ndict={'others':0}
  for k,v in vdict.items(): # Using an iterator function to handle large data sets.
    if k not in others:
      if v>meanVal:
       ndict[k]=v
      else:
        ndict['others']+=v
    else:
      ndict['others']+=v
  return ndict


def setPieText(patches, texts, autotexts):#Minimal function to adjust the Pie Charts text size.
  for t in texts:
    t.set_size('smaller')
  for t in autotexts:
    t.set_size('x-small')
  autotexts[0].set_color('y')

def createChart(datalist,title="Analysis Chart",outfile='output.png'):#Function which create a Pic chart of the different data points under analysis.
  n=len(datalist)
  chartsPerLine=int((n+1)/2)
  the_grid = GridSpec(2, chartsPerLine)
  row,col=0,0
  for data1 in datalist:
    title=data1['title']
    data=data1['data']
    plt.subplot(the_grid[row, col], aspect=1)
    labels = data.keys()
    fracs = [x for x in data.values()]
    patches, texts, autotexts=plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True,startangle=90)
    setPieText(patches, texts, autotexts)
    plt.title(title)
    if col+1==chartsPerLine:
      row,col=row+1,0
    else:
      col=col+1
    
  plt.savefig(outfile)


def normalizeData(data):#Normalizes the data points between 0-100
  total=sum([x for x in data.values()])
  for k,v in data.items():
    data[k]=(v/total)*100
  return data

def main():#JSON specific code to exploit various data points 
  df=pd.read_json('connections.json',dtype=object)
  res=json_normalize(df['values'])
  data1=res['industry']
  data2=res['location.country.code']
  data3=res['location.name']
  data4=res['firstName']
  tempData=[]
  countrycode=getStats(data2)
  countrycode=normalizeData(countrycode)
  tempData.append({'title':"Country Codes",'data':countrycode})
  industrywise=getStats(data1)
  industrywise=normalizeData(industrywise)
  tempData.append({'title':"Industries ",'data':industrywise})
  anonymousUser=getAnonymousUsers(data4)
  anonymousUser=normalizeData(anonymousUser)
  tempData.append({'title':"Public/private User",'data':anonymousUser})
  others=['India'] #Values in others list are put to Others in function getStats
  locationcode=getStats(data3,others)
  locationcode=normalizeData(locationcode)
  tempData.append({'title':"Cities",'data':locationcode})
 

  createChart(tempData) #Creats a chart out of the data.





if __name__=="__main__":
  main()
