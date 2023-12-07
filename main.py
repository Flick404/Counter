import tkinter as tk
from tkinter.font import Font
import os.path

# Function to get the full path of the counter value file
def get_file_path():
    directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(directory, "counter_value.txt")

# Function to save the counter value
def save_counter_value():
    with open(get_file_path(), "w") as file:
        file.write(str(counter.get()))

# Function to load the counter value
def load_counter_value():
    try:
        with open(get_file_path(), "r") as file:
            value = file.read().strip()
            if value.isdigit():
                return int(value)
            else:
                return 0  # If the file doesn't contain a valid integer
    except FileNotFoundError:
        return 0  # Return a default value if the file doesn't exist
    except Exception as e:
        print(f"Error reading counter value: {e}")
        return 0  # Return a default value in case of other errors


# Increment function
def increment():
    counter.set(counter.get() + 1)
    save_counter_value()

# Decrement function
def decrement():
    counter.set(counter.get() - 1)
    save_counter_value()

# Create the main application window
root = tk.Tk()
root.title("Counter")
root.geometry("300x200")

# Stay above other windows
root.attributes('-topmost', True)

# Define counter variable and set its initial value
counter = tk.IntVar(value=load_counter_value())

# Colors for the theme
background_color = "#1a1a1a"  # Dark black
text_color = "#d3b9ff"       # Light purple
button_color = "#33334d"     # Dark purple
button_text_color = "#ffffff" # White

# Create custom font for the label
custom_font = Font(size=24, weight="bold")  # Adjust size as needed

# Configure root window's background
root.configure(bg=background_color)

# Create widgets with customized colors
label = tk.Label(root, textvariable=counter, font=custom_font, fg=text_color, bg=background_color)
increment_button = tk.Button(root, text="+", command=increment, padx=20, pady=20, bg=button_color, fg=button_text_color)
decrement_button = tk.Button(root, text="-", command=decrement, padx=20, pady=20, bg=button_color, fg=button_text_color)

# Arrange widgets using grid layout
label.grid(row=0, column=1, padx=20, pady=20)
increment_button.grid(row=1, column=2)
decrement_button.grid(row=1, column=0)

# Make the layout responsive
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Start the GUI event loop
root.mainloop()