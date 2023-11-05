from logging import config
import tkinter as tk
from conf import configuration
import random

class gameGui():   
    
    def __init__(self, configuration):
        self.conf = configuration
        pass

    def generate_and_display_big_number(self, count, delay):
        if count <= 0:
            return
        self.big_number = random.randint(100, 1000)
        self.big_number_label.config(text=f"Big Number: {self.big_number}")
        self.root.after(delay, self.generate_and_display_big_number, count - 1, delay)

    def create_number_label(self, index):
        self.label = tk.Label(self.numbers_frame, text=str(self.listOfNumbers[index]), font=("Helvetica", 18))
        self.label.grid(row=0, column=index, padx=10)

    def create_numbers_with_delay(self, index, delay):
        if index < len(self.listOfNumbers):
            self.create_number_label(index)
            index += 1
            self.root.after(delay, self.create_numbers_with_delay, index, delay)
    
    def __create_widgets__(self):
        self.root = tk.Tk()
        self.root.title("numbers game!")

        # Create a label for the big number
        self.big_number_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.big_number_label.pack()

        # Start generating and displaying the big number three times
        self.generate_and_display_big_number(3, 400)

        # Create a frame for the horizontally aligned numbers
        self.numbers_frame = tk.Frame(self.root)
        self.numbers_frame.pack()
        
        bigNumbersList=[25, 50, 75, 100]
        smallNumberslist = [num for num in range(1, 11) for _ in range(2)]
        
        self.listOfNumbers = random.sample(bigNumbersList, self.conf.big_numbers)
        self.listOfNumbers.extend(random.sample(smallNumberslist, self.conf.small_numbers))

        # Start creating numbers with a delay of 1/3 second
        self.create_numbers_with_delay(0, 333)
    
    def runGame(self):
        self.__create_widgets__()
        print("widgets created")
        self.root.mainloop()

x = configuration(6, 2, 4)
y = gameGui(x)
y.runGame()