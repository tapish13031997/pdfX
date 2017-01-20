#using tag for fields in pdf for which information is to be extracted and value for information 

from lxml import html
import requests
import os
from urllib import url2pathname
import need
import universal
import file2
import convert
def reopen(filename):                           #open the html file for parasing
  requests_session = need.requests.session()
  requests_session.mount('file://', need.LocalFileAdapter())
  page = requests_session.get('file:///home/killerbee/Desktop/test2/'+universal.tag_folder+"/"+filename)   #file name
  universal.tree = html.fromstring(page.content)


def transform(tvalue,tremove): #remove tremove from tvalue and return string after tremove
  x=tvalue.find(tremove)      #example tvalue is the value of Application No. and tremove is Application No. 
  x+=len(tremove)
  return tvalue[x:]
  

def extract_multi_lines(tag,path):  #for tags with mulitple lines 
    temp=universal.tree.xpath(path)
    fans=""
    for x in temp :
       fans+=x
    fans=transform(fans,tag+" :")
    universal.data[tag]=fans  
def extract(path,tag):          #add value to tag in dictionary(data) using path 
    for value in universal.tree.xpath(path) :
      if value.find(tag) != -1 :
        break
    return transform(value,tag) 
       
#def extract_claims_pages(path):         #extract the value for No of Claims tag and No of pages tag
#    temp=extract(path,"No. of Pages : ")
#    pos=temp.find("No. of Pages : ")
#    y=len("No. of Pages : ");
#    temp[pos+y:]
#    y=0
#    tans=0
#    while temp[y].isdigit() :
#      tans*=10
#      tans+=int(temp[y])  
#      y=y+1
#    universal.data["No. of Pages"]=tans
#    tans=0 
#    temp=temp[y:]
#    pos=temp.find("No. of Claims : ")
#    y=len("No. of Claims : ");
#    temp=temp[pos+y:]
#    y=0
#    while temp[y].isdigit() and y<len(temp) :
#      tans*=10
#      tans+=int(temp[y])  
#      y=y+1
#    universal.data["No. of Claims"]=tans 
            


#def extract_names(path):     #for extracting information from name column
#    test=universal.tree.xpath(path)
#    x=0
#    while test[x].find("Name of Applicant : ")==-1:
#      #print(test[x])
#      x+=1
#    x+=1
#    tlist=[]
#    while test[x].find("Name of Inventor")==-1:
#      tlist.append(test[x])
#      x+=1
#    tlist=tlist[0:-1]  #for removing (*number*) Before Name of Inventor
#    universal.data["Name of Applicant"]=tlist
#    tlist=[]
#    while x<len(test):
#      tlist.append(test[x])
#      x+=1
#    universal.data["Name of Inventor"]=",".join(tlist)   

def locate(string, x="/html/body/page/p[",y="]/text()"):     #for locating xpath of column containing string
  #x="/html/body/div["
  #y="]/span/text()"
  
  i=0
  while i<100000 :
    s=universal.tree.xpath(x+str(i)+y)
    #print(s)
    for a in s:
      if a.find(string)!=-1 :
        return x+str(i)+y
    i+=1
  fappend=open("log.txt",'a')
  fappend.write(universal.filename+"->"+string+'\n')
  fappend.close()
  return  x+str(10)+y 
      
def begin():      
  reopen(universal.filename+universal.filename+".html") #html-tag filename converted from pdf
  #page = requests_session.get('file:///home/killerbee/Desktop/test2/'+filename)   #file name
  #universal.tree = html.fromstring(page.content)
  universal.data["Application No."]=extract(locate("Application No."),"Application No.")
  universal.data["Date of filing of Application"]=extract(locate("Date of filing of Application :"),"Date of filing of Application :")
  universal.data["Publication Date"]=extract(locate("Publication Date : "),"Publication Date : ")
  universal.data["No. of Pages"]=extract(locate("No. of Pages :"),"No. of Pages :")
  universal.data["No. of Claims"]=extract(locate("No. of Claims :"),"No. of Claims :")
  extract_multi_lines("Title of the invention",locate("Title of the invention"))
  extract_multi_lines("Name of Applicant",locate("Name of Applicant"))
  extract_multi_lines("Name of Inventor",locate("Name of Inventor"))
  extract_multi_lines("Abstract",locate("Abstract"))
  #try :
  #extract_names(locate("Name of Applicant"))
  #except :
  #  raise
  #  temp=input("Error occured in extracting names from file "+filename+" of year "+year+"\n"+"press 1 to continue")
  file2.extract_final_coloum()  
##  for z in universal.data :
##    print(z+":"+str(universal.data[z])+"\n")
#  #convert.remove()  
#    #print("\n")

