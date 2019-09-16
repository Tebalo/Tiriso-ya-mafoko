# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:45:58 2019

@author: Bopaki Tebalo

Chunks: 'lerui' in a sentence.
        'letlhaodi' in a sentence.
        'lebadi' in a sentence.
        'leemedi' in a sentence.
        'leamanyi' in a sentence.
        'lesupi' in a sentence.
        'letlhalosi' in a sentence.
Dikarolo tsa puo:
    leina(noun)
    leemedi(pronoun)
    lediri(verb)
    ditlhaodi(qualificatives):
        lesupi(demostrative) e.g  Go nole kgomo ele fela-'ele' ke lesupi(a mangwe ke bo 'e' 'eo') o othe a supa gore selo se go buiwang ka sone 
        lebadi(enumerative)  e.g  Go nole kgomo ele nngwefela-'nngwe' ke lebadi
        letlhaodi(adjective) e.g Monna yo moleele o lobelo.
"""
import nltk
import time
from nltk.chunk import RegexpParser
from nltk import Tree
class DikaroloTsaPuo:
        
    def search(self,hashMap,key):
        """
        Searches a given value from a HashMap.
        Parameters:
            array: A HashMap containing a list of tagged strings.
            val(str): A search key
        Returns:
            str: Returns tag if it is tagged, otherwise it return 'X'
        """
        dic = {'mo':'ADJ1',
               'ba':'ADJ2',
               'me':'ADJ3',
               'le':'ADJ4',
               'ma':'ADJ5',
               'se':'ADJ6',
               'lo':'ADJ7',
               'bo':'ADJ8',
               'go':'ADJ9',
               'di':'ADJ9'}
        if(key in hashMap):
            if(hashMap[key] == 'ADJ'):
                if(key[:2] in dic and len(key) > 2):
                    return dic[key[:2]]
                else:
                    return hashMap[key]
            return hashMap[key]
        elif(key == '.' or key == ','):
            return key
        elif(key[:1].isupper()):
            return 'NN'
        elif(key[:4] == 'goo-' or key[:8] == 'goo-rra-'):
            return 'EE1'
        else:
            return 'XX'  
    def word_net_lemmatiser(self,word):
        """
        Transforms a word to its root form and returns an array of possible roots,
            1. Checks for repititions i.e. lesweusweu >> sweu.
            2. Determine the class of the word i.e. Verb, Noun, Adjective, Adverb.
        """
        substlist = []
        """Extract a list of substrings from a word, from left to right and from right to left."""
        for i in range(len(word)):
            if(len(word[:i+1]) > 1):            
                substlist.append(word[:i+1])
        for i in range(len(word)):
            if(len(word[i+1:]) > 1):
                substlist.append(word[i+1:]) 
                
        """Check for repititions."""
        for substr in substlist:
            count = word.count(substr)        
            if(count > 1 and len(substr) > 3):
                rep = substr+substr
                if(rep in word):            
                    print(substr+'-'+word)
                    #f.writelines(substr+'-'+word+ '\n') # write new lines
                    return substr
                else:
                    return 'XX'

 
    def hashMap(self,arr):
        """
        Create a hashMap given a arr, use the value at index 0(zero) as the value and the proceeding
        array indexes as the keys.
        Parameters:
            arr: list of strings.
        Return:
            dict1: hash of strings.
        """
        n = len(arr)
        dict1 = {}
        i = 1
        for i in range(n):  
            if(i > 0):                
                key=arr[i]
                value=arr[0]
                dict1[key] = value
        return dict1
    
    def createHashMap(self):
        """
        Advanced hashMap create
        """
        dic1 = {}
        with open("pos1.txt","r+") as input_file:
            lines = input_file.readlines()
            for line in lines:
                dic1.update(self.hashMap(self.get_word(line.strip("\n"))))      
        return dic1
    def get_word(self,line):
        """
        Split a line from a text file into tokens, whenever there is a fullstop/period.
        """
        return line.split('.')
    def pos_tag(self,tokens):
        """
        param tokens: Sequence of tokens to be tagged 
        type tokens: list(str)
        param tagset: the tagset to be used
        type tagset: str
        return: The tagged tokens
        rtype: list(tuple(str, str))
        """
  
        hashMap = self.createHashMap()
        tagged = [] # Create an empty list
        tup = ()
        for token in tokens:
            tag = self.search(hashMap,token) # Fetch the tag from the trained tagset. 
            ls = [token,tag]
            tup = tuple(ls) # Covert into a tuple. 
            tagged.append(tup) # Add the tuples to the list.
            #file.writelines(str(tup) + '\n')
            #print(tup)
        return tagged 
    def untagged(self, tagged):
        """
        Return a list of untagged words.
        param: List of tuples(string, string).
        param type: array of objects.
        return: untagged tuples(string,'XX').
        return type: List of tuples.
        """
        file = open("untagged.txt","a+")
        for tup in tagged:
            if(tup[1] == "XX"):               
                print(tup[0] +" "+tup[1])
                file.writelines(tup[0] +"\n")
    def generator(self,tokens):
        """
        Perform language analysis.
        param tokens: sentence tokens in an array.
        param type: array of string.
        return: chunk.
        return type: object.
        """
        text2 = open("regs.txt","rb")
        chunkGram = text2.read().decode("utf8","ignore")
        text2.close()
        f = open("chunked.txt","w+")
        for sentence in tokens:
            tokenized = nltk.word_tokenize(sentence)
            tagged = self.pos_tag(tokenized)
            #print(tagged)
            chunkParser = nltk.RegexpParser(chunkGram) 
 
            tree = chunkParser.parse(tagged)   
            f.writelines(str(tree))
            self.display_chunks(tree, "letlhaodi")
            self.display_chunks(tree, "lerui")
            self.display_chunks(tree, "lesoboki") 
            self.display_chunks(tree, "lebadi")
            self.display_chunks(tree, "leemedi")
            self.display_chunks(tree, "lesupi")
            self.display_chunks(tree, "letlhalosi_felo")
            self.display_chunks(tree, "leamanyi")
            #tree.draw()   
        f.close()
        return tree
    
    def regx_creator(self, tokens):
        """
        param: tokens
        param type: object, string
        return: chunk
        rtype: str
        """
        file = open("Leamanyi\\LEA.txt","w+")
        file.writelines("leamanyi : ")
        for sentence in tokens: 
            tagged = self.pos_tag(nltk.word_tokenize(sentence))
            start = "{<"
            end = ">}"
            separator = "><"
            regularExp = []
            for tup in tagged:
                regularExp.append(tup[1])
            regularExp1 = separator.join(regularExp)
            regularExp1 = regularExp1.strip("<.>")
            reg = start + regularExp1 + end
            file.writelines('                '+reg + '\n')
            print(reg)
        file.close()
    def regx_trainer(self, tree, chunk):
        """
        param: tree, chunk 
        param type: object, string
        return: chunk
        rtype: str
        """
        file = open("trained.txt","w+")
        for subtree in tree.subtrees(filter=lambda t: t.label() == chunk):
            start = "{<"
            end = ">}"
            separator = "><"
            regularExp = []
            for tup in subtree.leaves():
                regularExp.append(tup[1])                   
                regularExp1 = separator.join(regularExp)
                reg = start + regularExp1 + end
                file.writelines('                '+reg + '\n')
                print(reg)
            file.close()

    def display_chunks(self, tree, chunk):
        """
        Display to thescreen and Write the chunks to the text file.
        param: tree, chunk 
        param type: object, string
        return: chunk
        rtype: str
        """
        #open("C:\\Users\\Bopaki\\Desktop\\all_test_results.txt", 'w').close()
        f1 = open("all_test_results.txt","a+")
        for subtree in tree.subtrees(filter=lambda t: t.label() == chunk):
            chunked = ""
            for tup in subtree.leaves():                
                chunked += tup[0]+" " 
            print(chunked +">>> "+chunk)
            #f1.writelines(chunked +">>> "+chunk+ '\n')
        f1.close()
        
if __name__ == "__main__":
    start = time.time()

    text2 = open("testData.txt", "rb+")
    testData = text2.read().decode('utf8', 'ignore')
    text2.close()

    dtp = DikaroloTsaPuo()

    #dtp.regx_creator(nltk.sent_tokenize(testData))# Trainer/ Regular expression creator/ ML.
    
    #dtp.untagged(dtp.pos_tag(nltk.word_tokenize(testData)))# Check Untagged words.
    
    dtp.generator(nltk.sent_tokenize(testData))# Indentify the chunks i.e. Leamanyi, Lerui, Letlhaodi.
    
    end = time.time()
    print()
    print("Time Elapsed: ",end-start, " seconds")
    
    

        
        
    
        