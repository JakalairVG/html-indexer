#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import os, time
currentFolder = Path.cwd()
outputFileName = 'index.html'
outputFile = open(outputFileName, "w")
outputFile.write('<!DOCType html>\n<html>\n<head>\n<center><h2>Links</h2></center>\n')
outputFile.write('</head>\n\n')
outputFile.write('<body text="ffff00" style="background-color:teal;">\n')
outputFile.write('<center><table border ="1" class="center">\n<tr>\n')
colNumber = 4
countNumber = int(0)
fileNumber = int(0)
beginningCode = '<td><a href="'
middleCode = '">'
endCode = '</a></td>\n'
for filename in sorted(os.listdir()):
    subDirectory = (currentFolder / filename)
    if Path(subDirectory).is_dir():
        htmlFile = list(subDirectory.glob('*.html'))
        for i, digit in enumerate(htmlFile):
            htmlRelPath = os.path.relpath(htmlFile[i], currentFolder)
            outputFile.write(beginningCode) 
            outputFile.write(htmlRelPath)
            outputFile.write(middleCode)
            outputFile.write(filename)
            outputFile.write(endCode)
            countNumber = countNumber + 1
            fileNumber = fileNumber + 1
            if countNumber >= colNumber:
                countNumber = 0
                outputFile.write('</tr><tr>\n')
outputFile.close()
