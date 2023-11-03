import tkinter as tk

class configuration():
    def __init__(self, num_of_numbers, big_numbers, small_numbers) -> None:
        assert small_numbers + big_numbers == num_of_numbers
        self.small_numbers = small_numbers
        self.big_numbers = big_numbers
        pass   
    
    
class configurationGui():   
    defaultBoxNumber = 6
    defaultBigNumbers = 1
    maxBigNumbers = 4
    defaultSmallNumbers = defaultBoxNumber - defaultBigNumbers
    
    def __init__(self):
        pass
     
    def update_small_scale(self, *args):
        big_number = self.big_numbers_scale.get()
        boxNum=int(self.num_entry.get())
        self.small_numbers_scale.config(from_=boxNum-configurationGui.maxBigNumbers, to=boxNum)
        smalls = boxNum - big_number
        self.small_numbers_scale.set(smalls)
        self.small_number_label.config(text="Small Number (" + str(boxNum-configurationGui.maxBigNumbers) +"-" + str(boxNum) +"):")
        
    def update_big_scale(self, *args):
        small_number = self.small_numbers_scale.get()
        boxNum=int(self.num_entry.get())
        bigs = boxNum - small_number
        self.big_numbers_scale.set(bigs)
        
    def update_num_entry(self, *args):
        if int(self.num_entry.get()) < 5:
            self.num_entry.delete(0, tk.END)
            self.num_entry.insert(0, str(configurationGui.defaultBoxNumber))
        self.update_small_scale()
        
    def submit(self):
        num_of_numbers = self.num_entry.get()
        big_numbers = self.big_numbers_scale.get()
        small_numbers = self.small_numbers_scale.get()
        self.conf = configuration(int(num_of_numbers), big_numbers, small_numbers)
        print(f"Number of Numbers: {num_of_numbers}, Big Number: {big_numbers}, Small Number: {small_numbers}")
        self.root.destroy()  # Destroy the old root window
    
    def __create_widgets__(self):
        # Create the main application window
        self.root = tk.Tk()
        self.root.title("Simple GUI Application")

        # Create a label for the number entry
        self.num_label = tk.Label(self.root, text="Number of Numbers:")
        self.num_label.pack()

        # Create an entry box for the number
        self.num_entry = tk.Entry(self.root)
        self.num_entry.insert(0, str(configurationGui.defaultBoxNumber))  # Set the default value to 6
        self.num_entry.pack()

        # Create a label for the big number scale
        self.big_number_label = tk.Label(self.root, text="Big Number (0-4):")
        self.big_number_label.pack()

        # Create a scale widget for selecting big numbers
        self.big_numbers_scale = tk.Scale(self.root, from_=0, to=4, orient="horizontal")
        self.big_numbers_scale.pack()
        self.big_numbers_scale.set(configurationGui.defaultBigNumbers)

        # Create a label for the small number scale
        self.small_number_label = tk.Label(self.root, text="Small Number (2-6):")
        self.small_number_label.pack()

        # Create a scale widget for selecting small numbers
        self.small_numbers_scale = tk.Scale(self.root, from_=configurationGui.defaultBoxNumber-configurationGui.maxBigNumbers, 
                                           to=configurationGui.defaultBoxNumber, orient="horizontal")
        self.small_numbers_scale.pack()
        self.small_numbers_scale.set(configurationGui.defaultSmallNumbers)

        # Bind the update_small_scale function to changes in the self.big_number_scale
        self.big_numbers_scale.bind("<Motion>", self.update_small_scale)

        # Bind the update_small_scale function to changes in the self.big_number_scale
        self.small_numbers_scale.bind("<Motion>", self.update_big_scale)

        # Bind the update_num_entry function to changes in the num_entry
        self.num_entry.bind("<FocusOut>", self.update_num_entry)

        # Create a submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack()

    def createConfiguration(self):
        self.__create_widgets__()        
        # Start the GUI application
        self.root.mainloop()
        
        return self.conf
                

