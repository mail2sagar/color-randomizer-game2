from tkinter import *
import random

root = Tk()

root.title("Color Randomizer Game")
root.geometry("800x600")
root.config(background="lavender")

label_name = Label(root)

class Game:
    def __init__(self):
        self.__score = 0
    
    def updateGame(self):
        self.text = ["BLACK","PINK","GREEN","BLUE","YELLOW","RED"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["black","pink","green","blue","yellow","red"]
        label_name["text"] = self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]
        
obj1 = Game#(random_number_for_color,random_number_for_text)
obj1.updateGame()


btn = Button(root,text="START",command=obj1.updateGame,bg="dark olive green",fg="white",relief=FLAT,padx=10,pady=1,font=("Arial",15))



root.mainloop()