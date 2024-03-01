# Text to Morse Code Translator

Short script to translate a string of letters and/or numbers into Morse code 'words' consisting of dots '.' and dashes '-'.  Can also produce audio of the translation.

Module was created to drive some functionality in a future raspi project and is being used as an opportunity to attempt to learn more detailed, 'proper' practices in Python and github.

## Description

morse.py consists of two commands:

- ```translate(in_string)``` takes a string as input and returns a string consisting of dots, dashes and spaces.  
  - one space is created between letter groups
  - three spaces are created between word groups
- ```sound(in_string)``` sounds out the conversion using the included dot.mp3 and dash.mp3 files
  - audio isn't great on my test system, possibly letting mp3 files run over each other

## Getting Started

### Dependencies

* Written on Windows 10 using VS Code and a WSL environment
* Requires the playsound module

### Installing
* ```from playsound import playsound```
* Clone repository, or just copy morse.py, dash.mp3 and dot.mp3

### Executing program

* ```print(morse.translate("This is a test"))``` will return ```- .... .. ...   .. ...   .-   - . ... -```
* ```morse_code = morse.translate("This is a test"))``` stores the string to a variable
* ```morse.sound("This is a test"))``` will play the morse translation over system speakers


## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
