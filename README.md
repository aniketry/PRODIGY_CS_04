**Educational Keylogger Tool**

**Project Purpose**

Develop a simple Educational Keylogger Tool using Python to record keyboard activity and log it in a file for educational purposes about cybersecurity.

This tool can be used to demonstrate how keyboard event listeners can be used in conjunction with keystrokes and how keystrokes are viewed by Python.

The Educational Keylogger Tool Project is a completion of Task-04 of my Cybersecurity Internship at Prodigy Info Tech.

---

**Key Features**

- Keyboard Keystroke Logging 
- Real-time Key Detection
- Special Key Support
- Automatic log generation
- Stop Logging with ESC Key
- Clean, Beginner-friendly Code
- Educational and Ethical Cybersecurity Project

---

**Technologies Used**

- Python
- Pynput Library
- File Handling
- Event Listeners

---

**Lessons Learned**

Through this project I gained experience with:

- Keyboard Event Handling
- Keystroke Monitoring
- Python Event Listeners
- File Handling & Logging
- Special Key Handling
- Real-time Input Monitoring
- Basics of Cybersecurity Monitoring
- Ethics of Keylogging

---

**How It Works**

This Keylogger will listen to all keyboard activity with use of the `pynput` library.
Every time a key is pressed, the Keylogger will:

- Capture the key
- Convert the key into a readable format
- Place the key in a log file

The logging process will also differentiate between Special Keys such as:

- Spacebar
- Enter
- Backspace
- Tab

to ensure cleaner logs.

The logging process stops once the ESC Key is pressed.

---

# Example Output

## Terminal Output

```text

 EDUCATIONAL KEYLOGGER TOOL

Keylogger is running...
Press ESC to stop.