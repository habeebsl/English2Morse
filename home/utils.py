morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '"': '.-..-.', '@': '.--.-.',
    
    ' ': ' ',  "'": '.----.'
}

def to_morse_code(text):
    converted = []
    for char in text.upper():
        if char in morse_code_dict:
            converted.append(morse_code_dict[char])
        else:
            print(f"Character '{char}' not found in the Morse code dictionary.")
            converted.append(' ')
    return " ".join(converted)
    
def to_english(morse_code):
    converted = []
    separated_morse = morse_code.split(" ")
    for code in separated_morse:
        for key, value in morse_code_dict.items():
            if code == value:
                converted.append(key)
                break
        else:
            converted.append(' ')
    return "".join(converted)


def testrun():
    # Collect inputs from the user
    conversion_direction = input("Would you like to convert to Morse code (yes/no): ").lower()
    user_input = input("Enter the text or Morse code: ")

# Perform the conversion based on the user's choice
    if conversion_direction == 'yes':
        result = to_morse_code(user_input)
        print(result)
    elif conversion_direction == 'no':
        result = to_english(user_input)