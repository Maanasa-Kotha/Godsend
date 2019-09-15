from TexttoSpeech.textspc import text_to_speech
from ImageHandler.opencvim import image_to_text


image_text = "images/poster.png"
text = image_to_text(image_text, "thresh")
text_to_speech(text)


