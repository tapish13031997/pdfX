import xlsxwriter
import universal
import logwriter
import re
def init():       #for initializing the xlsx file
  universal.workbook = xlsxwriter.Workbook(universal.filename+".xlsx")
  universal.worksheet = universal.workbook.add_worksheet()
  headformat = universal.workbook.add_format()
  headformat.set_bold()
  headformat.set_text_wrap()
  universal.worksheet.set_row(0, 60)
  universal.worksheet.set_column(0,3,11)
  universal.worksheet.set_column(4,4,30)
  universal.worksheet.set_column(5,5,20)
  universal.worksheet.set_column(6,6,15)
  universal.worksheet.set_column(7,8,7)
  universal.worksheet.set_column(9,9,12)
  universal.worksheet.set_column(10,10,13)
  universal.worksheet.set_column(11,12,9)
  universal.worksheet.set_column(13,13,15)
  universal.worksheet.set_column(14,14,12)
  universal.worksheet.set_column(15,17,14)
  universal.worksheet.set_column(18,18,11)
  universal.worksheet.set_column(19,19,14)

  universal.worksheet.write('A1',"Application No.",headformat)
  universal.worksheet.write('B1',"Date of filling of Application",headformat)
  universal.worksheet.write('C1',"Publication Date",headformat)
  universal.worksheet.write('D1',"Name of Applicant",headformat)
  universal.worksheet.write('E1',"Title of Invention",headformat)
  universal.worksheet.write('F1',"Name of Inventor(s)",headformat)
  universal.worksheet.write('G1',"Abstract",headformat)
  universal.worksheet.write('H1',"No. of pages",headformat)
  universal.worksheet.write('I1',"No. of claims",headformat)
  universal.worksheet.write('J1',"International classification",headformat)
  universal.worksheet.write('K1',"Priority Document No.",headformat)
  universal.worksheet.write('L1',"Priority Date",headformat)
  universal.worksheet.write('M1',"Name of priority country",headformat)
  universal.worksheet.write('N1',"International Application No.",headformat)
  universal.worksheet.write('O1',"International Application Filling Date",headformat)
  universal.worksheet.write('P1',"International Publication No.",headformat)
  universal.worksheet.write('Q1',"Patent of addition to Application No.",headformat)
  universal.worksheet.write('R1',"Patent of addition to Application No. Filling Date",headformat)
  universal.worksheet.write('S1',"Divisional to Application No.",headformat)
  universal.worksheet.write('T1',"Divisional to Application No. Filling Date",headformat)
  universal.row = 1
  universal.date_format = universal.workbook.add_format({'num_format':'dd mm yyyy'})
  #universal.workbook.close()  


#inside for loop
def loop() :
  try:
    universal.worksheet.write(universal.row, 0, universal.data["Application No."].strip())
    universal.worksheet.write(universal.row, 1, universal.data["Date of filing of Application"].strip(), universal.date_format)
    universal.worksheet.write(universal.row, 2, universal.data["Publication Date"].strip(), universal.date_format)
    universal.worksheet.write(universal.row, 3, universal.data["Name of Applicant"].strip())
    universal.worksheet.write(universal.row, 4, universal.data["Title of the invention"].strip())
    universal.worksheet.write(universal.row, 5, universal.data["Name of Inventor"].strip())
    universal.worksheet.write(universal.row, 6, universal.data["Abstract"].strip())
    universal.worksheet.write(universal.row, 7, int(universal.data["No. of Pages"].strip()))
    universal.worksheet.write(universal.row, 8, int(universal.data["No. of Claims"].strip()))
    universal.worksheet.write(universal.row, 9, universal.data["International classification"].strip())
    universal.worksheet.write(universal.row, 10, universal.data["Priority Document No"].strip())
    if(universal.data["Priority Date"].strip() == "NA"):
        universal.worksheet.write(universal.row, 11, universal.data["Priority Date"].strip())
    else:
        universal.worksheet.write(universal.row, 11, universal.data["Priority Date"].strip(),universal.date_format)
    universal.worksheet.write(universal.row, 12, universal.data["Name of priority country"].strip())
    universal.worksheet.write(universal.row, 13, universal.data["International Application No"].strip())
    if(universal.data["IAFiling Date"].strip() == "NA"):
        universal.worksheet.write(universal.row, 14, universal.data["IAFiling Date"].strip())
    else:
        universal.worksheet.write(universal.row, 14, universal.data["IAFiling Date"].strip(),universal.date_format)
    universal.worksheet.write(universal.row, 15, universal.data["International Publication No"].strip())
    universal.worksheet.write(universal.row, 16, universal.data["Patent of Addition to Application Number"].strip())
    if(universal.data["IBFiling Date"].strip() == "NA"):
        universal.worksheet.write(universal.row, 17, universal.data["IBFiling Date"].strip())
    else:
        universal.worksheet.write(universal.row, 17, universal.data["IBFiling Date"].strip(),universal.date_format)
    universal.worksheet.write(universal.row, 18, universal.data["Divisional to Application Number"].strip())
    if(universal.data["ICFiling Date"].strip() == "NA"):
        universal.worksheet.write(universal.row, 19, universal.data["ICFiling Date"].strip())
    else:
        universal.worksheet.write(universal.row, 19, universal.data["ICFiling Date"].strip(),universal.date_format)
  except:
      logwriter.logwrite("ERROR : Incorrect patent values")
  universal.row = universal.row + 1
  
def checkpatentvalues() :
  if((bool(re.search(r'^\d{12}\s[A-Z]$',universal.data["Application No."].strip()))|bool(re.search(r'\/[A-Z]{3}\/\d{4}\s[A-Z]$',universal.data["Application No."].strip())))==False):
    return False;
  if(bool(re.search(r'^\d{2}\/\d{2}\/\d{4}$',universal.data["Date of filing of Application"].strip()))==False):
    return False;
  if(bool(re.search(r'^\d{2}\/\d{2}\/\d{4}$',universal.data["Publication Date"].strip()))==False):
    return False;
  if(bool(re.search(r'^1\)',universal.data["Name of Applicant"].strip()))==False):
    return False;
  if(bool(re.search(r'\D',universal.data["No. of Pages"].strip()))==False):
    return False;
  if(bool(re.search(r'\D',universal.data["No. of Claims"].strip()))==False):
    return False;
  if((bool(re.search(r'^[A-Z]\d\d[A-Z]',universal.data["International classification"].strip()))|(universal.data["International classification"].strip()=="NA"))==False):
    return False;
  if((bool(re.search(r'^[A-Z]\d\d[A-Z]',universal.data["International classification"].strip()))|(universal.data["International classification"].strip()=="NA"))==False):
    return False;
  if((bool(re.search(r'^\d{2}\/\d{2}\/\d{4}$',universal.data["Priority Date"].strip()))|(universal.data["Priority Date"].strip()=="NA"))==False):
    return False;
  if((bool(re.search(r'^PCT\/',universal.data["International Application No"].strip()))|(universal.data["International Application No"].strip()=="NA"))==False):
    return False;
  if((bool(re.search(r'^\d{2}\/\d{2}\/\d{4}$',universal.data["IAFiling Date"].strip()))|(universal.data["IAFiling Date"].strip()=="NA"))==False):
    return False;
  if((bool(re.search(r'^[A-Z][A-Z]\s\d{4}',universal.data["International Publication No"].strip()))|(universal.data["International Publication No"].strip()=="NA"))==False):
    return False;
  return True;


