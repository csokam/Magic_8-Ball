import random
import os

answered = False
question=" "
answers=["It is Certain.","It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.",
"As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.",
"Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.",
"Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]

while answered==False:    
    print("Ask your question.")
    question=input()
    if question[-1] != "?":
        os.system("cls")
        print("Questions end with question marks.")    
    else:
        os.system("cls")       
        print("Question:\n"+question)
        print("Answer:\n"+answers[random.randint(0,19)])
        answered=True
