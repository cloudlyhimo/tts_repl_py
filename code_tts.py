from gtts import gTTS
from playsound import playsound

string = input(str("Enter: "))
defa = input(str("T: "))
repl = input(str("Replace?: "))
string_edited = string.replace(defa, repl)

print(string_edited) 

tts = gTTS(string_edited)
tts.save("tts.mp3")
playsound("tts.mp3")
