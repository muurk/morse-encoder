from pydub import AudioSegment
from pydub.generators import Sine
import os

MESSAGE=os.environ.get('MESSAGE', 'TEST MESSAGE')

def text_to_morse_code(text, dot_length=100):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
        '9': '----.', ' ': ' '
    }
    
    morse_code = ''
    for char in text.upper():
        morse_code += morse_code_dict.get(char, '') + ' '

    # Create audio for morse code
    dot = Sine(800).to_audio_segment(duration=dot_length)
    dash = Sine(800).to_audio_segment(duration=dot_length * 3)
    gap = AudioSegment.silent(duration=dot_length)

    morse_audio = AudioSegment.silent(duration=0)
    for char in morse_code:
        if char == '.':
            morse_audio += dot + gap
        elif char == '-':
            morse_audio += dash + gap
        elif char == ' ':
            morse_audio += AudioSegment.silent(duration=dot_length * 3)

    return morse_audio

# Replace 'YOUR_MESSAGE' with your message
#message = "YOUR_MESSAGE"
audio = text_to_morse_code(MESSAGE)
audio.export("/output/output_morse.wav", format="wav")

