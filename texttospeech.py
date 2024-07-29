from gtts import gTTS
import os

# Text to be converted to speech
text = "Hello, how are you doing today?"

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine
speech = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file
speech.save("text_to_speech.mp3")

# Playing the converted file
os.system("start text_to_speech.mp3")  # For Windows
# os.system("mpg321 text_to_speech.mp3")  # For Linux
