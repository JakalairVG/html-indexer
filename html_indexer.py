# to make one html file out of all the other ones.
from pathlib import Path
import os, time
import pyinputplus as pyip

os.system('cls')  # just clearing the screen
#  this will get the folder where the file is currently located at.
#  homeFolder = Path('c:/html_games')
#  easier to just put this file where the other files are.
currentFolder = Path.cwd()
print('\nProgram running in ', currentFolder)  # this is for user output
time.sleep(0.1)
print('\nIs this the folder you want to index? (Y/n)')
folderResponse = pyip.inputYesNo(default='Yes', blank=True)
if folderResponse == 'no':
    print('Please move file to the folder you want to index.')
    exit()
print('What do you want the file to be called?')
print('(Examples: index.html, html.txt, index_html.txt)')
outputFileName = pyip.inputStr(prompt='Enter filename: ')
#  outputFileName = 'test_index.html'
#  Putting the header information in the file.

print('Creating ', outputFileName)
time.sleep(0.1)
outputFile = open(outputFileName, "w")
outputFile.write('<!DOCType html>\n<html>\n<head>\n<center><h2>Links</h2></center>\n')
outputFile.write('</head>\n\n')
#  outputFile.write('<html>\n')
#  outputFile.write('<head>\n')
#  This is for the start of the body
#  modify the colors as you see fit.
outputFile.write('<body text="ffff00" style="background-color:teal;">\n')
#  starting a simple table
outputFile.write('<center><table border ="1" class="center">\n<tr>\n')
#  outputFile.close()

print('\nHow many columns would you like in the html file?')
colNumber = pyip.inputInt(prompt='Enter a number:')
#  setting up some things for later on.
countNumber = int(0)  # this is a better name.
fileNumber = int(0)
beginningCode = '<td><a href="'
middleCode = '">'
endCode = '</a></td>\n'
print('Searching for HTML files.')
time.sleep(0.1)
#  this is the mess of code that makes it all work
for filename in os.listdir():

    # print(filename)  # here for debug
    subDirectory = (currentFolder / filename)
    # print(subDirectory)  # here for debug
    if Path(subDirectory).is_dir():
        # print(filename, 'is a directory')  # here for debug
        htmlFile = list(subDirectory.glob('*.html'))
        for i, digit in enumerate(htmlFile):
            #  print(htmlFile[i])  # here for debug for file name
            htmlRelPath = os.path.relpath(htmlFile[i], currentFolder)
            #  print(htmlRelPath)
            outputFile.write(beginningCode)  # part one of html
            outputFile.write(htmlRelPath)  # the html file relpath
            outputFile.write(middleCode)  # middle code of html
            outputFile.write(filename)  # dir of the htmlFile
            outputFile.write(endCode)  # the end of the html
            countNumber = countNumber + 1
            fileNumber = fileNumber + 1
            if countNumber >= colNumber:
                countNumber = 0
                outputFile.write('</tr><tr>\n')
#  find all the .html files in the folders
#  list(currentFolder.glob('*.html') this command finds them
#  import them into an html file.
#  outputFile = open('test_index.txt')
#  test = outputFile.read()
outputFile.close()
print(fileNumber, 'HTML files were found and added to', outputFileName)
time.sleep(0.1)
#  htmlFilePath = 'c:\\test\\game\\index.html'
#  print(htmlFilePath.split(os.sep))
print('Done.')
