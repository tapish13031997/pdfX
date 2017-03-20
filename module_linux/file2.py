#This file convert the last column (the one on the left with all the patent details)
#This is done in 3 steps, Firstly i find the start point of the column and then i make a string(temp) of text in the required column 
#And then i extract information from temp corresponding to each tag(which are stored in a list ->target)
#to extract information from tag i locate ":" and then extract text after ":" till i find the end of string or next ":"    
import universal #using universal.data and universal.tree from universal.py
def limit(s):     #funtion for finding the start of the column
  for x in s:
    if x.find("(51) International classif") !=-1:
      return 0
  return 1
def cal(s):       #for counting how many 
  cnt2=0
  for y in s:
    for x in y:
     if x==":":
      cnt2+=1
  return cnt2        
def extract_final_coloum():
  x="/html/body/page/p["
  y="]/text()"
  i=1
  target=["International classification","Priority Document No","Priority Date","Name of priority country","International Application No","IAFiling Date","International Publication No","Patent of Addition to Application Number","IBFiling Date","Divisional to Application Number","ICFiling Date"]
  path=x+str(i)+y
  s=universal.tree.xpath(path)
  while limit(s):
    #print(s)
    i+=1  
    path=x+str(i)+y
    s=universal.tree.xpath(path)
    if i>5000:
      fappend=open("log.txt",'a')
      fappend.write(universal.filename+"->"+"limit->function "+s+"\n")
      fappend.close()
      return -1
  cnt=0
  temp=""
  while cnt<10:
     if cal(s)>0:
      cnt+=cal(s)
      temp+="".join(s)
     i+=1  
     path=x+str(i)+y
     s=universal.tree.xpath(path) 
  i=0
  j=0
  pj=0   
  pj=temp.find(":",pj)
  while 1:
    j=temp.find(":",pj+1)
    if j!=-1:
      universal.data[target[i]]=temp[pj+1:j]
      i+=1
      if i>len(target):
        break
      pj=j
    else:
      universal.data[target[i]]=temp[pj+1:]
      i+=1
      break
  return 1      

