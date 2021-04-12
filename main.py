import pyttsx3, PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))

#in my work her i added the pdf directly into the code but could be done by getting the url to do so

speaker = pyttsx3.init()
# Initialize the speaker

rate = speaker.getProperty('rate')   
print(rate)
speaker.setProperty('rate', 125)

voices = speaker.getProperty('voices')
print(voices)
#using voice 1.id for female
speaker.setProperty('voice', voices[1].id)




for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

engine.save_to_file(text, 'audio.mp3') #this grabs the audio and coverts it to mp3
engine.runAndWait()
