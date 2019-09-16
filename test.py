# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:21:20 2019

@author: Bopaki
"""
import kivy
kivy.require('1.9.0')
import time
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label 
from kivy.uix.button import Button
from random import randrange
from random import randint
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.config import Config
from kivy.uix.popup import Popup
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False) 
Config.write()

#========================================================================================================================================
#========================================================================================================================================
class Test(FloatLayout):
    '''Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from the kv lang file.
    '''
    # Answer
    b1 = ObjectProperty()
    b2 = ObjectProperty()
    b3 = ObjectProperty()
    b4 = ObjectProperty()
    b5 = ObjectProperty()
    b6 = ObjectProperty()
    # Question
    d1 = ObjectProperty()
    d2 = ObjectProperty()
    d3 = ObjectProperty()
    d4 = ObjectProperty()
    d5 = ObjectProperty()
    # Question
    que1 = StringProperty()
    que2 = StringProperty()
    que3 = StringProperty()
    que4 = StringProperty()
    que5 = StringProperty()
    # Score
    que6 = StringProperty()
    # Timer
    b7 = StringProperty()
    # Answer
    ans1 = StringProperty()
    ans2 = StringProperty()
    ans3 = StringProperty()
    ans4 = StringProperty()
    ans5 = StringProperty()
    a = NumericProperty(60)  # seconds
#========================================================================================================================================   
    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)
        #===================================================================
        def finish_callback(animation, incr_crude_clock):
            #self.anim = Animation(a=0, duration=self.a)
            self.submit()
            self.pop_up()
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self) 
#========================================================================================================================================
    def pop_up(self):
        layout = GridLayout(cols = 1, padding = 10) 
        pop_label = Label(text=self.calculate_score())
        close_button = Button(text='Try again!')
        layout.add_widget(pop_label) 
        layout.add_widget(close_button)  
        popup = Popup(title ='Tiriso Ya Mafoko', 
                    content = layout, 
                    size_hint =(None, None), size =(500, 200),
                    auto_dismiss = False) 
        popup.open() 
        close_button.bind(on_press = self.callback)
#========================================================================================================================================
    def callback(self, event):
        self.try_again()
#========================================================================================================================================
    def try_again(self):
        App.get_running_app().stop()
        Animation.cancel_all(self)
        App.get_running_app().run()
#========================================================================================================================================
    def do_action(self,Button):
            Button.background_color = 1, 1, 1, 0
            data = open("switch.txt","rb+")
            test = data.read().decode('utf8', 'ignore')
            data.close()
            line = str(test)
            
            if line != '':
                update = line.split(' ')
                if (update[1] == '1'):
                    if Button.text != self.que1:
                        self.que1 = Button.text  
                        Button.text = update[0]    
                        Button.background_color = .5, 1, 1, 1                                
                        self.b1.background_color = .5, 1, 1, 1
                        open("switch.txt", "w").close()
                        return
                    else:
                        print(Button.text,self.que1)
                        self.b1.background_color = .5, 1, 1, 1       
                        Button.background_color = .5, 1, 1, 1 
                        open("switch.txt", "w").close()                 
                        return self.do_action(Button)
                elif (update[1] == '2'):
                    if Button.text != self.que2:
                        self.que2 = Button.text   
                        Button.text = update[0]  
                        Button.background_color = .5, 1, 1, 1                   
                        self.b2.background_color = .5, 1, 1, 1
                        open("switch.txt", "w").close()
                        return
                    else:
                        print(Button.text,self.que2)
                        self.b2.background_color = .5, 1, 1, 1  
                        Button.background_color = .5, 1, 1, 1 
                        open("switch.txt", "w").close()                      
                        return self.do_action(Button)
                elif (update[1] == '3'):
                    if Button.text != self.que3:
                        self.que3 = Button.text  
                        Button.text = update[0]      
                        Button.background_color = .5, 1, 1, 1              
                        self.b3.background_color = .5, 1, 1, 1
                        open("switch.txt", "w").close()
                        return
                    else:
                        print(Button.text,self.que3)
                        self.b3.background_color = .5, 1, 1, 1  
                        Button.background_color = .5, 1, 1, 1  
                        open("switch.txt", "w").close()                    
                        return self.do_action(Button)
                elif (update[1] == '4'):
                    if Button.text != self.que4:
                        self.que4 = Button.text  
                        Button.text = update[0]    
                        Button.background_color = .5, 1, 1, 1               
                        self.b4.background_color = .5, 1, 1, 1 
                        open("switch.txt", "w").close()
                        return
                    else:
                        print(Button.text,self.que4)
                        self.b4.background_color = .5, 1, 1, 1 
                        Button.background_color = .5, 1, 1, 1 
                        open("switch.txt", "w").close()                         
                        return self.do_action(Button)
                elif (update[1] ==  '5'):
                    if Button.text != self.que5:
                        self.que5 = Button.text
                        Button.text = update[0]
                        self.b5.background_color = .5, 1, 1, 1
                        Button.background_color = .5, 1, 1, 1 
                        open("switch.txt", "w").close()
                        return
                    else:
                        print(Button.text,self.que5)
                        self.b5.background_color = .5, 1, 1, 1
                        Button.background_color = .5, 1, 1, 1 
                        open("switch.txt", "w").close()                  
                        return self.do_action(Button)
                else:
                    print('game is broken')
                #print(Button.text,' update with ', update[0])
                #Button.text = update[0]
                Button.background_color = .5, 1, 1, 1              
                open("switch.txt", "w").close()
            else:
                open("switch.txt", "w").close()
                Button.background_color = 1,0,0,1
                file = open("switch.txt","w+")
                file.write(Button.text+' '+Button.value)
                file.close()
                return
            return None
#========================================================================================================================================
    def submit(self):
        # Get the user answers
        res1 = self.b1.text
        res2 = self.b2.text
        res3 = self.b3.text
        res4 = self.b4.text
        res5 = self.b5.text
        # Get the questions
        potso1 = self.d1.text
        potso2 = self.d2.text
        potso3 = self.d3.text
        potso4 = self.d4.text
        potso5 = self.d5.text  
 
        d_mark = self.createHashMap()
        # End
        qns = [potso5,potso4,potso3,potso2,potso1]
        ans = [res5,res4,res3,res2,res1]
        d_ans = self.createDic(ans, qns)
        file = open("mark_key.txt","r+")
        a_key = file.read()
        file.close()

        m_key = a_key.split(' ')

        wrong = self.score(m_key,ans)
        mark = 5 - wrong
        score = 'Score: '+str(mark)
        self.que6 = score
        self.pop_up()
        return score
#========================================================================================================================================
    def calculate_score(self):
        # Get the user answers
        res1 = self.b1.text
        res2 = self.b2.text
        res3 = self.b3.text
        res4 = self.b4.text
        res5 = self.b5.text
        # Get the questions
        potso1 = self.d1.text
        potso2 = self.d2.text
        potso3 = self.d3.text
        potso4 = self.d4.text
        potso5 = self.d5.text  
        d_mark = self.createHashMap()
        # End
        qns = [potso5,potso4,potso3,potso2,potso1]
        ans = [res5,res4,res3,res2,res1]
        d_ans = self.createDic(ans, qns)
        file = open("mark_key.txt","r+")
        a_key = file.read()
        file.close()
        #print(a_key)
        m_key = a_key.split(' ')
        #wrong = self.scoreHs(d_mark, d_ans)
        wrong = self.score(m_key,ans)
        #wrong = 3
        mark = 5 - wrong
        score = 'Score: '+str(mark)

        file = open("history.txt","w+")
        file.write(str(mark)+'\n')
        file.close()

        return score
#========================================================================================================================================
    def score(self, m_key, a_sheet):
        incorrect = 0
        for key_no, key in enumerate(m_key):
            if(m_key[key_no] != a_sheet[key_no]):
                incorrect += 1
        return incorrect        
#========================================================================================================================================
    def createDic(self,arr1, arr2):
        dic = {}
        for ar_no, ar in enumerate(arr1):
            if ar in dic:
                pass
            else:
                dic[arr1[ar_no]] = arr2[ar_no]
        return dic
#========================================================================================================================================
    def createHashMap(self):
        """
        Advanced hashMap create
        """
        dic1 = {}
        with open("marking_key.txt","r+") as input_file:
            lines = input_file.readlines()
            for line in lines:
                line = self.cleanData(line)
                dic1.update(self.hashMap(self.cleanDataG(self.get_word(line.strip("\n")))))     
        return dic1
#========================================================================================================================================
    def cleanDataG(self,arr):
        for i in range(len(arr)):
            if(arr[i] == '\n'):
                del arr[i]
        return arr
#========================================================================================================================================        
    def hashMap(self,arr):
        n = len(arr)
        dict1 = {}
        i = 1
        for i in range(n):  
            if(i > 0):                
                key=arr[i]
                value=arr[0]
                dict1[key] = value
        return dict1
#========================================================================================================================================        
    def cleanData(self,data):
        data = data.replace(",)",".")
        data = data.replace("(",".")
        data = data.replace(")",".")
        data = data.replace(",",".") 
        data = data.replace("1. ","") 
        data = data.replace("2. ","")
        data = data.replace("3. ","")
        data = data.replace("4. ","")
        data = data.replace("5. ","")      
        return data
#========================================================================================================================================        
    def get_word(self,line):
        return line.split('.')
#========================================================================================================================================
#========================================================================================================================================
class TestApp(App):
    def cleanData(self,data):
        #data = data.replace("",".")
        data = data.replace(",)",".")
        data = data.replace("(",".")
        data = data.replace(")",".")
        data = data.replace(",",".")        
        return data
#========================================================================================================================================
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
#========================================================================================================================================        
    def get_word(self,line):
        """
        Split a line from a text file into tokens, whenever there is a fullstop/period.
        """
        return line.split('.')
#========================================================================================================================================
    def createHashMap(self):
        """
        Advanced hashMap create
        """
        dic1 = []
        with open("marking_key.txt","r+") as input_file:
            lines = input_file.readlines()
            for line in lines:
                line = self.cleanData(line)
                dic1.update(self.hashMap(self.cleanDataG(self.get_word(line.strip("\n")))))     
        print(dic1) 
        return dic1
#========================================================================================================================================
    def create2dArray(self):   
        arr = []    
        with open("work.txt","r+") as input_file:
            lines = input_file.readlines()
            for line_no, line in enumerate(lines):
                tokens = self.cleanDataG(self.get_word(self.cleanData(line)))
                arr.append([])
                arr[line_no].append(tokens)           
        return arr 
#========================================================================================================================================
    def get_random_cols(self,matrix):
    	list = []
    	list_size = 5
    	current_size = 0
    	while current_size < list_size:
    		r = randrange(len(matrix))
    		if r not in list:
    			current_size += 1
    			list.append(r)
    	return list
#========================================================================================================================================
    def cleanDataG(self,arr):
        for i in range(len(arr)):
            if(arr[i] == '\n'):
                del arr[i]
        return arr
#========================================================================================================================================
    def history(self):
        history = 'Prev-Score: None'
        with open("history.txt","r+") as input_file:
            lines = input_file.readlines()
            if lines != '':
                history = ''
            for line in lines:
                history = history +"\n"+"Prev-Score: "+self.cleanData(line)   
        if history == '':
            history ='Prev-Score: None' 
        input_file.close()
        return history
#========================================================================================================================================
    def build(self):
        """
        Articially Intelligent Quiz Creation.
        >>> a=[[1,5,6,8],[1,2,5,9],[7,5,6,2]]
        >>> len(a)
        3
        >>> len(a[0])
        4
        a[row][column]
        """
        matrix = self.create2dArray()
        cols = self.get_random_cols(matrix)
        # Question 1
        #ques = randrange(len(matrix)) 
        ques = cols[0]
        answer = randint(1,(len(matrix[ques][0])-1))
        answer1 = matrix[ques][0][0]
        ques1 = matrix[ques][0][answer]
        # Question 2
        #ques = randrange(len(matrix))
        ques = cols[1] 
        answer = randint(1,(len(matrix[ques][0])-1))
        answer2 = matrix[ques][0][0]
        ques2 = matrix[ques][0][answer]
        # Question 3
        #ques = randrange(len(matrix))
        ques = cols[2] 
        answer = randint(1,(len(matrix[ques][0])-1))
        answer3 = matrix[ques][0][0]
        ques3 = matrix[ques][0][answer]
        # Question 4
        #ques = randrange(len(matrix))
        ques = cols[3] 
        answer = randint(1,(len(matrix[ques][0])-1))
        answer4 = matrix[ques][0][0]
        ques4 = matrix[ques][0][answer]
        # Question 5
        #ques = randrange(len(matrix))
        ques = cols[4] 
        answer = randint(1,(len(matrix[ques][0])-1))
        answer5 = matrix[ques][0][0]
        ques5 = matrix[ques][0][answer]

        open("marking_key.txt","w+").close()
        file = open("marking_key.txt","w+")
        file.write(answer5+'.'+ques5+'\n'+answer4+'.'+ques4+'\n'+answer3+'.'+ques3+'\n'+answer2+'.'+ques2+'\n'+answer1+'.'+ques1)
        file.close()

        open("mark_key.txt","w+").close()
        file = open("mark_key.txt","w+")
        file.write(ques5+' '+ques4+' '+ques3+' '+ques2+' '+ques1)
        file.close()

        history = self.history()

        oshima = Test(que5=ques4,que4=ques5,que3=ques1,que2=ques3,que1=ques2,
                    ans1=('5. '+answer1),ans2=('4. '+answer2),ans3=('3. '+answer3),
                    ans4=('2. '+answer4),ans5=('1. '+answer5),que6=history)
        oshima.start()
        return oshima
#========================================================================================================================================
#========================================================================================================================================
if __name__== '__main__':
    open("switch.txt", "w").close()
    open("history.txt", "w").close()
    TestApp().run()