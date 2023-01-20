from gtts import gTTS

nombre = "audio.mp3"

audio = gTTS("Hola camaradas, este es un audio desde python", lang= "es", tld = "us")

audio.save(nombre)