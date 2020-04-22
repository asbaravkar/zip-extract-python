# importing required modules 
from zipfile import ZipFile 

# take zipfile name
name=input("Enter zip-file name: ")

  
# opening the zip file in READ mode 
with ZipFile(name, 'r') as zip: 
    # printing all the contents of the zip file 
    zip.printdir() 
  
    # extracting all the files 
    print('Extracting all the files now...') 
    zip.extractall() 
    print('Done!')
