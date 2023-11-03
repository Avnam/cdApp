import tkinter as tk


def update_small_scale(*args):
    big_number = big_number_scale.get()
    boxNum=int(num_entry.get())
    small_number_scale.config(from_=boxNum-maxBigNumbers, to=boxNum)
    smalls = boxNum - big_number
    small_number_scale.set(smalls)
    small_number_label.config(text="Small Number (" + str(boxNum-maxBigNumbers) +"-" + str(boxNum) +"):")
    
def update_big_scale(*args):
    small_number = small_number_scale.get()
    boxNum=int(num_entry.get())
    bigs = boxNum - small_number
    big_number_scale.set(bigs)
    
def update_num_entry(*args):
    if int(num_entry.get()) <= 5:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, str(defaultBoxNumber))
    update_small_scale()

def create_new_window():
    new_root = tk.Tk()
    new_root.title("New Window with Box")
    box_label = tk.Label(new_root, text="This is a new window with a box.")
    box_label.pack()
    new_root.mainloop()
    
def submit():
    num_of_numbers = num_entry.get()
    big_number = big_number_scale.get()
    small_number = small_number_scale.get()
    print(f"Number of Numbers: {num_of_numbers}, Big Number: {big_number}, Small Number: {small_number}")
    root.destroy()  # Destroy the old root window
    create_new_window()  # Create a new root window
    

defaultBoxNumber = 6
defaultBigNumbers = 1
maxBigNumbers = 4
defaultSmallNumbers = defaultBoxNumber - defaultBigNumbers

# Create the main application window
root = tk.Tk()
root.title("Simple GUI Application")

# Create a label for the number entry
num_label = tk.Label(root, text="Number of Numbers:")
num_label.pack()

# Create an entry box for the number
num_entry = tk.Entry(root)
num_entry.insert(0, str(defaultBoxNumber))  # Set the default value to 6
num_entry.pack()

# Create a label for the big number scale
big_number_label = tk.Label(root, text="Big Number (0-4):")
big_number_label.pack()

# Create a scale widget for selecting big numbers
big_number_scale = tk.Scale(root, from_=0, to=4, orient="horizontal")
big_number_scale.pack()
big_number_scale.set(defaultBigNumbers)

# Create a label for the small number scale
small_number_label = tk.Label(root, text="Small Number (2-6):")
small_number_label.pack()

# Create a scale widget for selecting small numbers
small_number_scale = tk.Scale(root, from_=defaultBoxNumber-maxBigNumbers, to=defaultBoxNumber, orient="horizontal")
small_number_scale.pack()
small_number_scale.set(defaultSmallNumbers)

# Bind the update_small_scale function to changes in the big_number_scale
big_number_scale.bind("<Motion>", update_small_scale)

# Bind the update_small_scale function to changes in the big_number_scale
small_number_scale.bind("<Motion>", update_big_scale)

# Bind the update_num_entry function to changes in the num_entry
num_entry.bind("<FocusOut>", update_num_entry)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Start the GUI application
root.mainloop()
