from Tkinter import *
import random, os, sys
from PIL import Image, ImageTk

class PicLearnerGUI (Frame):
    def __init__ (self):
        Frame.__init__(self)
        self.master.title('PicLearner')
        self.var_path= StringVar()
        self.path = StringVar()

        self.var_result = StringVar()
        self.resultsend = StringVar()
        pathname = os.path.dirname(sys.argv[0])
        self.var_path.set(str(pathname))  
        
        self.define_widgets()       
        self.grid()

    def define_widgets (self):
        
        self.toolbar = Frame(self, borderwidth=1, relief="raised")
        self.toolbar.pack(side="top", fill=X,expand=1)

        self.Bottom = Frame(self, width=800, height=800, bd=4, relief="ridge")
        self.Bottom.pack(side="bottom", fill="both", anchor=S,expand="yes")
               
        lblPath = Label(self.toolbar, text='Path:')
        lblPath.pack(side="left")
        
        lblEntry = Entry(self.toolbar)
        lblEntry['textvariable'] = self.var_path
        lblEntry.pack(side="left")

        btn_enter = Button(self.toolbar)
        btn_enter["text"] = "Enter/Next"
        btn_enter.pack(side="left")
        btn_enter["command"] = self.getpath  
        
        btn_Rev = Button(self.toolbar)
        btn_Rev["text"] = "Reveal"
        btn_Rev.pack(side="left")
        btn_Rev["command"] = self.give_result

        lbl_result = Label(self.toolbar)
        lbl_result['textvariable'] = self.resultsend
        lbl_result.pack(side="left")
        
    def give_result(self):
        result = self.var_result.get()
        self.resultsend.set(str(result))
        
    def getpath(self):
        path = self.var_path.get()
        self.path.set(str(path))


        random_filename = random.choice([
            x for x in os.listdir(path)
            if os.path.isfile(os.path.join(path, x))
        ])
        self.var_result.set(str(random_filename))
        self.extension_check(random_filename)

        
        random_filename =  self.var_result.get()
           
        pic = ImageTk.PhotoImage(file=random_filename)
        
        pic_label = Label (self.Bottom)
        pic_label.config(image = pic, height=800, width=800)
        pic_label.grid(row=0, column=0)
        
        
        blank = " "
        self.resultsend.set(str(blank))
        self.mainloop()
    def extension_check(self, a_file):
        if a_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            self.var_result.set(str(a_file))     
        else:
            path = self.var_path.get()
            self.path.set(str(path))
            b_file = random.choice([
                x for x in os.listdir(path)
                if os.path.isfile(os.path.join(path, x))
            ])
            
            self.extension_check(b_file)
        pass
    
if __name__ == '__main__':
    my_gui = PicLearnerGUI()
    my_gui.mainloop()
    
