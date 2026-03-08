from gtts import gTTS
import os

def text_to_speech(text, filename):
    folder = "audio"
    if not os.path.exists(folder):
        os.makedirs(folder)
    output_path = os.path.join(folder, f"{filename}.mp3")
    tts = gTTS(text)
    tts.save(output_path)
    return output_path