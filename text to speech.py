import tkinter as tk
import pyttsx3

# Create the tkinter GUI window
window = tk.Tk()
window.title("Text to Speech Converter")

# Create the text entry field
text_entry = tk.Entry(window, width=40)
text_entry.pack()

# Create the button and function for converting text to speech
def convert_to_speech():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Get the text from the entry field
    text = text_entry.get()

    # Set the properties of the voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)

    # Convert the text to speech
    engine.say(text)
    engine.runAndWait()

# Create the button for converting text to speech
convert_button = tk.Button(window, text="Convert to Speech", command=convert_to_speech)
convert_button.pack()

# Create the button and function for clearing the text entry field
def clear_text():
    text_entry.delete(0, tk.END)

# Create the button for clearing the text entry field
clear_button = tk.Button(window, text="Clear Text", command=clear_text)
clear_button.pack()

# Start the GUI event loop
window.mainloop()
