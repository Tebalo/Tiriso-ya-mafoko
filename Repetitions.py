# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 08:20:05 2019

@author: Bopaki
"""
f = open("C:\\Users\\Bopaki\\Desktop\\trained.txt","w+")
def tester(word):
    word = "lesweusweu"
    print(word[:1])
    print(word[:2])
    print(word[:3])
    print(word[:4])
    print(word[:5])
    print(word[:7])
    print(word[:8])
    print(word[:9])
    print(word[:10])
    print(word[1:])
    print(word[2:])
    print(word[3:])
    print(word[4:])
    print(word[5:])
    print(word[6:])
    print(word[7:])
    print(word[8:])
    print(word[9:])
    print(word[10:])

#tester("lesweusweu")

def repetitions(word):
    substlist = []
    double_vw = ['mo',
                 'ba',
                 'bo',
                 'me',
                 'le',
                 'ma',
                 'se',
                 'di',
                 'lo',
                 'go']
    #for vw in double_vw:
        #if(word[:2] == vw):
            #print(vw+'-'+word[2:])
            #f.writelines(vw+'-'+word[2:] + '\n') # write new lines
        #if(word[2:] == 'ng'):
            #print(word[:len(word)-2]+'-'+'ng')
            #f.writelines(word[:len(word)-2]+'-'+'ng'+ '\n') # write new lines
    for i in range(len(word)):
        if(len(word[:i+1]) > 1):            
            substlist.append(word[:i+1]) 
    for i in range(len(word)):
        if(len(word[i+1:]) > 1):
            substlist.append(word[i+1:])            

    for substr in substlist:
        count = word.count(substr)        
        if(count > 1 and len(substr) > 3):
            #print(substr)
            rep = substr+substr
            #print(rep)
            if(rep in word):            
                print(substr+'-'+word)
                f.writelines(substr+'-'+word+ '\n') # write new lines

def traverse(wordlist):
    for word in wordlist:
        repetitions(word)
        
text2 = open("C:\\Users\\Bopaki\\Desktop\\Processing.txt","rb")
text = text2.read().decode("utf8","ignore")
text2.close()  
stri = ['ADJ.','NN.','NUM.','VRB.'] 

texts = text.split(".")

adjs = ["lesweusweu","botalatala","bantsintsi","setonatona","maswaana"]

def lemmatiser(word):
    
traverse(adjs)
f.close()
