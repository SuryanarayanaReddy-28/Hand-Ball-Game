from tkinter import * #importing modules
import random
import os


def first_bat(): # defining function if we choose bat
    bat_button.destroy() #destroying the buttons so they wont interfere 
    bowl_button.destroy()    
    
    def Bowling_part(): #defining function for bowling
        target=player_score+1
        toss_label.config(text="computer's batting")
        toss_label.pack()
        bat_button.destroy() 
        
        def computer_round(player_choice):
            global player_score,computer_score,strikes_left# defining global variables
            computer_choice=random.randint(1,6) #computer choice
            if player_choice==(computer_choice+1) or player_choice==(computer_choice-1):#setting the conditions for playing
                strikes_left-=1
            elif player_choice==computer_choice:
                computer_score+=(2*computer_choice)
            else:
                computer_score+=computer_choice
    
            if strikes_left==0 and computer_score<player_score:
                update_scores()
                result_label.config(text=" YOU WON !")# modifying label for result
                buttonsL_frame.destroy()#destroying the buttons so they wont interfere 
                return
            if computer_score>=target:
                update_scores()
                result_label.config(text="COMPUTER won!")
                buttonsL_frame.destroy()
                return
            elif computer_score==target-1 and strikes_left==0:
                update_scores()
                buttonsL_frame.destroy()
                result_label.config(text="ITS A TIE!")
                return
            update_scores()
            result_label.config(text=f"computer chose: {computer_choice}")
        def update_scores():# function for updating scores
            player_score_label.config(text=f" target: {target}")
            computer_score_label.config(text=f"computer score: {computer_score}")
            attempts_left_label.config(text=f"attempts left: {strikes_left}")

        player_score_label=Label(win,text="",highlightthickness=0,fg="white",bg="black")#creating widgets with set of parameters
        player_score_label.pack()# packing the widgets
        computer_score_label=Label(win,text="",highlightthickness=0,fg="white",bg="black")
        computer_score_label.pack()  
        result_label=Label(win,text="",bg="grey",fg="white")  
        result_label.pack()
        attempts_left_label=Label(win,text="",bg="grey",fg="white")
        attempts_left_label.pack()
        

        buttonsL_frame=Frame(win) #creating frame for  buttons    
        buttonsL_frame.pack()

        for i in range(1,7): #buttons loop for player choice
            buttonL=Button(buttonsL_frame,text=str(i),bg="orange",fg="white",command=lambda i=i: computer_round(i))
            buttonL.pack(side="left")
    
#all the rest of the code goes with the similar commenting 



    def Batting():#  defining  function for batting part 
        

        def play_round(player_choice):
            global player_score,computer_score,strikes_left,toss_label
            computer_choice=random.randint(1,6)

            if player_choice==(computer_choice+1) or player_choice==(computer_choice-1):
                strikes_left-=1
            elif player_choice==computer_choice:
                player_score+=(2*player_choice)
            else:
                player_score+=player_choice
    
            if strikes_left==0:
                update_scores()
                result_label.config(text="Batting Over!")
                k=player_score
                buttons_frame.destroy()
                strikes_left=3
                Bowling_part()
                return 
            update_scores()
            result_label.config(text=f"computer chose: {computer_choice}")
    
        def update_scores():
            player_score_label.config(text=f"YOUR SCORE: {player_score}")
            attempts_left_label.config(text=f"attempts left: {strikes_left}")

        player_score_label=Label(win,text="",highlightthickness=0,fg="white",bg="black")
        player_score_label.pack()

        attempts_left_label=Label(win,text="",bg="grey",fg="white")
        attempts_left_label.pack()

        result_label=Label(win,text="",bg="grey",fg="white")
        result_label.pack()

        

        buttons_frame=Frame(win)    
        buttons_frame.pack()

        for i in range(1,7):
            button=Button(buttons_frame,text=str(i),bg="orange",fg="white",command=lambda i=i: play_round(i))
            button.pack(side="left")
    Batting()

def first_bowl():
    bat_button.destroy()
    bowl_button.destroy()
    
    
    def Bowling_part():
        toss_label.config(text="computer's batting")
        toss_label.pack()
        bat_button.destroy() 
        
        def computer_round(player_choice):
            global player_score,computer_score,strikes_left
            computer_choice=random.randint(1,6)
            if player_choice==(computer_choice+1) or player_choice==(computer_choice-1):
                strikes_left-=1
            elif player_choice==computer_choice:
                computer_score+=(2*computer_choice)
            else:
                computer_score+=computer_choice
    
            if strikes_left==0:
                update_scores()
                result_label.config(text=f"  Batting Over !, Target: {computer_score+1}")
                strikes_left=3
                Batting()
                buttonsL_frame.destroy()
                return
            
            update_scores()
            result_label.config(text=f"computer chose: {computer_choice}")
        def update_scores():
        
            computer_score_label.config(text=f"computer score: {computer_score}")
            attempts_left_label.config(text=f"attempts left: {strikes_left}")

        


        player_score_label=Label(win,text="",highlightthickness=0,fg="white",bg="black")
        player_score_label.pack()
        computer_score_label=Label(win,text="",highlightthickness=0,fg="white",bg="black")
        computer_score_label.pack()  
        result_label=Label(win,text="",bg="grey",fg="white")  
        result_label.pack()
        attempts_left_label=Label(win,text="",bg="grey",fg="white")
        attempts_left_label.pack()
        

        buttonsL_frame=Frame(win)    
        buttonsL_frame.pack()

        for i in range(1,7):
            buttonL=Button(buttonsL_frame,text=str(i),bg="orange",fg="white",command=lambda i=i: computer_round(i))
            buttonL.pack(side="left")
    

    def Batting():
        
        
        def play_round(player_choice):
            global player_score,computer_score,strikes_left,toss_label
            computer_choice=random.randint(1,6)

            if player_choice==(computer_choice+1) or player_choice==(computer_choice-1):
                strikes_left-=1
            elif player_choice==computer_choice:
                player_score+=(2*player_choice)
            else:
                player_score+=player_choice
    
            if strikes_left==0 and player_score<computer_score:
                update_scores()
                result_label.config(text="YOU LOST!")
                buttons_frame.destroy()
                return 
            if player_score>computer_score and strikes_left>0:
                update_scores()
                result_label.config(text="You Won!")
                buttons_frame.destroy()
            elif player_score==computer_score and strikes_left==0:
                update_scores()
                result_label.config(text="It's a tie!")
                buttons_frame.destroy()
                return 
    
            update_scores()
            result_label.config(text=f"computer chose: {computer_choice}")
    
        def update_scores():
            player_score_label.config(text=f"YOUR SCORE: {player_score}")
            attempts_left_label.config(text=f"attempts left: {strikes_left}")

        player_score_label=Label(win,text="",highlightthickness=0,fg="white",bg="black")
        player_score_label.pack()

        attempts_left_label=Label(win,text="",bg="grey",fg="white")
        attempts_left_label.pack()

        result_label=Label(win,text="",bg="grey",fg="white")
        result_label.pack()

        

        buttons_frame=Frame(win)    
        buttons_frame.pack()

        for i in range(1,7):
            button=Button(buttons_frame,text=str(i),bg="orange",fg="white",command=lambda i=i: play_round(i))
            button.pack(side="left")
    Bowling_part()



player_score=0 #initial figures
computer_score=0
strikes_left=3

win=Tk() #creating window
win.geometry("400x400") #setting window size

win.configure(bg="black") #setting window background color
win.title("Base Ball") #setting window title

win.resizable(width= False, height=False) #setting window size to fixed
current_dir=os.getcwd() #getting current directory
print(current_dir)
image=PhotoImage(file=r"C:\Users\Arun Shyam\pro\project\croc.png")
win.iconphoto(True,image) #setting window icon
lat=PhotoImage(file=r"C:\Users\Arun Shyam\pro\project\cricketp.png")
canvas=Canvas(win,width=400,height=400) #creating canvas
canvas.place(relwidth=1,relheight=1)
canvas.create_image(200,200,anchor=CENTER,image=lat) #setting bg image
toss_label=Label(win,text="You wanna choose bat or ball",font=("georgia",16),bg="dark orange", fg="white")
toss_label.pack()# creating label for toss
bat_button=Button(win,text="BAT",font=("georgia",16),bg="dark orange", fg="white",command=first_bat)
bat_button.pack() # creating button for bat
bowl_button=Button(win,text="BOWL",font=("georgia",16),bg="dark orange", fg="white",command=first_bowl)
bowl_button.pack() #creating button for bowl

win.mainloop() #looping the window