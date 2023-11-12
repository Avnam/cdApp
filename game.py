from queue import Empty
import tkinter as tk
from conf import configuration
import random
import re

class gameGui():   
    
    def __init__(self, configuration):
        self.config = configuration
        self.geo = None
        self.cheats = False
        pass
    
    def getGeo(self):
        self.geo=self.root.geometry()

    def generate_and_display_target(self, count, delay):
        if count <= 0:
            return
        self.target = random.randint(100, 1000)
        self.target_label.config(text=f"Target: {self.target}")
        self.root.after(delay, self.generate_and_display_target, count - 1, delay)

    def create_number_label(self, index):
        self.label = tk.Label(self.numbers_frame, text=str(self.listOfNumbers[index]), font=("Helvetica", 18))
        self.label.grid(row=0, column=index, padx=10)

    def create_numbers_with_delay(self, index, delay):
        if index < len(self.listOfNumbers):
            self.create_number_label(index)
            index += 1
            self.root.after(delay, self.create_numbers_with_delay, index, delay)
            
    def set_comment(self, str):
        self.comment.config(text=f"{str}")
    
    def is_valid_calc(s):
        pattern = re.compile("^[0-9\(\)\+\*-\/]+$")

        # Use the pattern to match the string
        match = pattern.match(s)

        # If there is a match, the string is valid; otherwise, it's not
        return bool(match)

    def assert_numbers(self, str):
        
        if not str:
            self.set_comment("try giving me an actuall calculation")
        elif str == "cheat":
            self.cheats = True
            self.set_comment("cheating are you..")
            return False
        
        # Use regular expression to find all numbers in the string
        numbers = re.findall(r'\d+', str)

        # Convert the list of strings to a list of integers
        numbers = list(map(int, numbers))
        
        origNumbers = self.listOfNumbers.copy()
        for num in numbers:
            if num in origNumbers:
                origNumbers.remove(num)
            else:
                if numbers.count(num) == 1:
                    self.set_comment(f"oh really - where did you get {num} from??")
                else:
                    self.set_comment(f"oh really - where did you get the other {num} from??")
                return False
        
        self.set_comment(f"")
        
        return True

    def closeWindow(self):
        self.getGeo()
        self.root.destroy()
    
    def check(self, *args):
        calc = self.calc.get()

        areTheNumbersValid = self.assert_numbers(calc)
        
        #cheat
        if calc == "cheat" or (not self.cheats and not areTheNumbersValid):
            return

        if not gameGui.is_valid_calc(calc):
            self.set_comment("the expression should be consistent of 0-9 /+*- (). thats it")
            return
        
        evaled = eval(calc)
        if self.cheats == True:
            print (evaled)

        if (self.cheats and not areTheNumbersValid):
            return
        
        self.retValue = "again"
        if evaled==self.target:
            self.closeWindow()

    def giveUp(self, *args):
        self.closeWindow()
        self.retValue = "again"

    def conf(self, *args):
        self.closeWindow()
        self.retValue = "conf"

    def done(self, *args):
        self.closeWindow()
        self.retValue = "done"

    def __create_widgets__(self):       
        self.root = tk.Tk()
        self.root.title("numbers game!")
        
        if self.geo != None:
            self.root.geometry(self.geo)
        
        self.retValue = "done"
        
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        # Create a label for the big number
        self.target_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.target_label.pack()

        # Start generating and displaying the big number three times
        self.generate_and_display_target(7, 200)
        
        # Create a frame for the horizontally aligned numbers
        self.numbers_frame = tk.Frame(self.root)
        self.numbers_frame.pack()
        
        bigNumbersList=[25, 50, 75, 100]
        smallNumberslist = [num for num in range(1, 11) for _ in range(2)]
        
        self.listOfNumbers = random.sample(bigNumbersList, self.config.big_numbers)
        self.listOfNumbers.extend(random.sample(smallNumberslist, self.config.small_numbers))

        # Start creating numbers with a delay of 1/3 second
        self.create_numbers_with_delay(0, 333)
        
        # Create a label for the number entry
        self.calc_label = tk.Label(self.root, text="your calc here:", font=("Helvetica", 24))
        self.calc_label.pack()

        # Create an entry box for the number
        self.calc = tk.Entry(self.root, font=("Helvetica", 24))
        self.calc.pack()
        
        self.comment = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.comment.pack()
        
        w = 11
        h = 2
        
        # Create a submit button
        self.submit_button = tk.Button(self.root, text="check", command=self.check,
                                       width=w, height=h)
        self.submit_button.pack(side=tk.LEFT, padx=10)
        
        # Create a submit button
        self.giveUp_button = tk.Button(self.root, text="pass", command=self.giveUp,
                                       width=w, height=h)
        self.giveUp_button.pack(side=tk.LEFT, padx=10)

        # Create a conf button
        self.conf_button = tk.Button(self.root, text="conf", command=self.conf,
                                       width=w, height=h)
        self.conf_button.pack(side=tk.LEFT, padx=10)

        # Create a done button
        self.done_button = tk.Button(self.root, text="done", command=self.done,
                                       width=w, height=h)
        self.done_button.pack(side=tk.LEFT, padx=10)
    
        self.root.bind("<Return>", self.check)
        self.root.bind("<Escape>", self.done)
        
    def runGame(self):
        self.__create_widgets__()
        
        print("widgets created")
        self.root.mainloop()
        
        return self.retValue
