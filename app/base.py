from youtube_transcript_api import YouTubeTranscriptApi

ln = input("Enter the language")

try:
    lst = YouTubeTranscriptApi.get_transcript("j8U4Y_2-JzY", languages=[ln], preserve_formatting=True)
    text=''
    for i in lst:
        text += (' '+ i['text'])
        print(text)

except:
    print("ERROR: The transcript doesn't exist in this langauge")
