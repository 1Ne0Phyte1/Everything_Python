appendMe='even more Text'
saveFile= open('exampleFile.txt','a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()
