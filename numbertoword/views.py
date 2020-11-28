from django.shortcuts import render
from gtts import gTTS 
import os 



# Create your views here.

def number_to_word(request):
    word='please enter input'
   
  
    if request.method == 'POST':
        number=request.POST['number']
        word=num_to_word(number).upper()
       
        # mytext=word
        # language = 'en'
        # myobj = gTTS(text=mytext, lang=language, slow=False) 
        
        # myobj.save("welcome.mp3")
        # os.system("mpg321 welcome.mp3")

        
        
        
    context={'word':word}
    return render(request,'index.html',context)
        

    

def num_to_word(num):
    word_num = { "0": "zero", "00": "", "1" : "One" , "2" : "Two", "3" : "Three", "4" : "Four", "5" : "Five","6" : "Six", "7": "Seven", "8" : "eight", "9" : "Nine","01" : "One" , "02" : "Two", "03" : "Three", "04" : "Four", "05" : "Five","06" : "Six", "07": "Seven", "08" : "eight", "09" : "Nine", "10" : "Ten", "11": "Eleven", "12" :"Twelve", "13" : "Thirteen", "14" : "Fourteen", "15" : "Fifteen", "17":"Seventeen", "18" :"Eighteen", "19": "Nineteen", "20" : "Twenty", "30" : "Thirty", "40" : "Forty", "50" : "Fifty", "60" : "Sixty", "70": "seventy", "80" : "eighty", "90" : "ninety"}
    keys = []
    for k in word_num.keys():
        keys.append(k)

    if len(num) == 1:
        return(word_num[num[0]])
    elif len(num) == 2:
        c = 0
        for k in keys:
            if k == num[0] + num[1]:
                c += 1
        if c == 1:
            return(word_num[num[0] + num[1]])
        else:
            return(word_num[str(int(num[0]) * 10)] + " " + word_num[num[1]])
    elif len(num) == 3:
        c = 0
        for k in keys:
            if k == num[1] + num[2]:
                c += 1
        if c == 1:
            return(word_num[num[0]]+ " Hundred and " + word_num[num[1] + num[2]])
        else:
            return(word_num[num[0]]+ " Hundred and " + word_num[str(int(num[1]) * 10)] + " " + word_num[num[2]])
    elif len(num) == 4:
        c = 0
        for k in keys:
            if k == num[2] + num[3]:
                c += 1
        if c == 1:
            if num[1] == '0' :
                return(word_num[num[0]]+ " Thousand  " + word_num[num[2] + num[3]])
            else:
                return(word_num[num[0]]+ " Thousand " + word_num[num[1]]+ " Hundred and " + word_num[num[2] + num[3]])

        else:
            if num[1] == '0' :
                return(word_num[num[0]]+ " Thousand " + word_num[str(int(num[2]) * 10)] + " " + word_num[num[3]])
            else:
                return(word_num[num[0]]+ " Thousand " + word_num[num[1]]+ " Hundred and " + word_num[str(int(num[2]) * 10)] + " " + word_num[num[3]])
    elif len(num) == 5:
        c = 0
        d = 0
        for k in keys:
            if k == num[3] + num[4]:
                c += 1
        for k in keys:
            if k == num[0] + num[1]:
                d += 1
        if d == 1:
            val = word_num[num[0] + num[1]] 
        else:
            val = word_num[str(int(num[0]) * 10)] + " " + word_num[num[1]]

        if c == 1:
            if num[2] == '0' :
                return(val + " Thousand " + word_num[num[3] + num[4]])
            else:
                return(val + " Thousand " + word_num[num[2]]+ " Hundred and " + word_num[num[3] + num[4]])

        else:
            if num[2] == '0' :
                return(val + " Thousand " + word_num[str(int(num[3]) * 10)] + " " + word_num[num[4]])
            else:
                return(val + " Thousand " + word_num[num[2]]+ " Hundred and " + word_num[str(int(num[3]) * 10)] + " " + word_num[num[4]])
    elif len(num) == 6:
        c = 0
        d = 0
        e = 0
        for k in keys:
            if k == num[4] + num[5]:
                c += 1
        for k in keys:
            if k == num[1] + num[2]:
                d += 1
                
        if d == 1:
            val = word_num[num[1] + num[2]] 
            if val == "":
                e += 1
        else:
            val = word_num[str(int(num[1]) * 10)] + " " + word_num[num[2]]

        if c == 1:
            if e == 1:
                if num[3] == '0' :
                    return(word_num[num[0]]+" lakh " + word_num[num[4] + num[5]])
                else:
                    return(word_num[num[0]]+" lakh "+ word_num[num[3]]+ " Hundred and " + word_num[num[4] + num[5]])
            else:
                if num[3] == '0' :
                    return(word_num[num[0]]+" lakh "+ val + " Thousand " + word_num[num[4] + num[5]])
                else:
                    return(word_num[num[0]]+" lakh "+ val + " Thousand " + word_num[num[3]]+ " Hundred and " + word_num[num[4] + num[5]])
        else:
            if num[3] == '0' :
                return(word_num[num[0]]+" lakh "+ val + " Thousand " + word_num[str(int(num[4]) * 10)] + " " + word_num[num[5]])
            else:
                return(word_num[num[0]]+" lakh "+ val + " Thousand " + word_num[num[3]]+ " Hundred and " + word_num[str(int(num[4]) * 10)] + " " + word_num[num[5]])

    else:
        return("ten lakh")


