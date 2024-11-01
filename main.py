from tkinter import *
from tkinter import ttk

# Colors
co0 = "grey"  # Background color for the display
co1 = "yellow"  # Background color for the frame
col2 = "black"    # Color for the buttons
col3 = "black"     # Color for the equals button
text_color = "black"  # Text color for buttons and display

# Create the main window
window = Tk()
window.title('Simple Calculator')
window.geometry('235x318')  # Set the window size
window.configure(bg=co0)    # Set the background color

# Style configuration
style = ttk.Style(window)
style.theme_use("clam")

# Create a separator
ttk.Separator(window, orient=HORIZONTAL).grid(row=0, column=0, ipadx=280)


frame_score = Frame(window, width=300, height=56, bg=co1)
frame_score.grid(row=1, column=0, sticky=NW)

# Frame for the buttons
frame_buttons = Frame(window, width=300, height=340, bg=co0)
frame_buttons.grid(row=2, column=0, sticky=NW)

# Display label
app_screen = Label(frame_score, width=16, height=2, anchor="e", bg=co1, justify=RIGHT, font=("Ivy", 18), fg=text_color)
app_screen.place(x=0, y=0)

# Function to clear the display
def clear_display():
    app_screen.config(text='')

# Function to append to the display
def append_to_display(value):
    current_text = app_screen.cget("text")
    app_screen.config(text=current_text + str(value))

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(app_screen.cget("text"))
        app_screen.config(text=str(result))
    except Exception:
        app_screen.config(text="Error")

# Buttons layout
buttons = [
    ('C', 0, 0), ('%', 118, 0), ('/', 177, 0),
    ('7', 0, 50), ('8', 59, 50), ('9', 118, 50), ('*', 177, 50),
    ('4', 0, 100), ('5', 59, 100), ('6', 118, 100), ('-', 177, 100),
    ('1', 0, 150), ('2', 59, 150), ('3', 118, 150), ('+', 177, 150),
    ('0', 0, 200), ('.', 59, 200), ('=', 118, 200)
]

# Create buttons
for (text, x, y) in buttons:
    if text == 'C':
        btn = Button(frame_buttons, text=text, width=5, height=2, bg=col2, fg=text_color, font=("Ivy", 13, "bold"),
                     relief=RAISED, overrelief=RIDGE, command=clear_display, activebackground="blue", activeforeground="white")
    elif text == '=':
        btn = Button(frame_buttons, text=text, width=5, height=2, bg=col3, fg=text_color, font=("Ivy", 13, "bold"),
                     relief=RAISED, overrelief=RIDGE, command=evaluate, activebackground="blue", activeforeground="white")
    else:
        btn = Button(frame_buttons, text=text, width=5, height=2, bg=col2, fg=text_color, font=("Ivy", 13, "bold"),
                     relief=RAISED, overrelief=RIDGE, command=lambda value=text: append_to_display(value),
                     activebackground="blue", activeforeground="white")

    btn.place(x=x, y=y)

window.mainloop()
