import tkinter as tk
from conf import configuration
import random

def create_second_window():
    second_window = tk.Toplevel(root)
    second_window.title("numbers game!")

    def generate_and_display_big_number(count):
        if count <= 0:
            return
        big_number = random.randint(100, 1000)
        big_number_label.config(text=f"Big Number: {big_number}")
        second_window.after(200, generate_and_display_big_number, count - 1)

# Create a label for the big number
    big_number_label = tk.Label(second_window, text="", font=("Helvetica", 24))
    big_number_label.pack()

    # Start generating and displaying the big number three times
    generate_and_display_big_number(3)

    # Create a frame for the horizontally aligned numbers
    numbers_frame = tk.Frame(second_window)
    numbers_frame.pack()

    def create_number_label(number):
        label = tk.Label(numbers_frame, text=str(number), font=("Helvetica", 18))
        label.grid(row=0, column=number - 1, padx=10)

    def create_numbers_with_delay(start, end, delay):
        if start <= end:
            create_number_label(start)
            start += 1
            second_window.after(delay, create_numbers_with_delay, start, end, delay)

    # Start creating numbers with a delay of 1/3 second
    create_numbers_with_delay(1, 5, 333)

root = tk.Tk()
root.title("First Window")

# Create a button to open the second window
open_second_button = tk.Button(root, text="Open Second Window", command=create_second_window)
open_second_button.pack()

root.mainloop()
