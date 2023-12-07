# Counter Application

## Overview

This application is a simple counter developed in Python using the tkinter library. It provides a graphical user interface (GUI) for increasing, decreasing, and resetting a count, which is persisted in a text file.

## Features

- **Simple GUI:** A user-friendly interface to interact with the counter.
- **Persistent Storage:** The count is saved to a file, allowing it to be retained between sessions.

## Installation

To set up the Counter application, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Flick404/Counter
   ```
2. **Navigate to the Application Directory:**
   ```bash
   cd Counter
   ```
3. **(Optional) Set up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```
4. **Run the Application:**
   ```bash
   python main.py
   ```

## Usage

Launch the application by running `main.py`. The GUI will appear with buttons to increment, decrement, and reset the counter. The current count will be displayed and saved to `counter_value.txt`.

## Contributing

If you would like to contribute to the Counter application, please follow the standard fork-and-pull request workflow.

## License

This project is licensed under the [License Name] - see the LICENSE.md file for details.

# Code Documentation

Below is a brief explanation of the `main.py` script in the Counter application:

```python
import tkinter as tk
from tkinter.font import Font
import os.path

# Function to get the path of the counter value file
def get_file_path():
    # ... code ...

# Function to save the counter value to a file
def save_counter_value():
    # ... code ...

# Function to load the counter value from a file
def load_counter_value():
    # ... code ...

# ... additional code and tkinter setup ...

if __name__ == '__main__':
    # Main execution point of the script
    # Set up the tkinter window and widgets
    # ... tkinter setup code ...
```
