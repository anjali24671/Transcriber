
def getContent(video_url, video_lang):
    # Preprocess
    try:
        if video_url[29]=='?':
            video_id = video_url[32:]
        else:
            video_id = video_url[17:28]

        try:
            # Call the API
            from youtube_transcript_api import YouTubeTranscriptApi
            content = YouTubeTranscriptApi.get_transcript(video_id, languages=[video_lang])

            # Making it look like a paragraph and not a bunch of discrete lines
            beautyContent=''
            for elem in content:
                beautyContent += " "+ elem['text']
            return beautyContent
        except:
            mssg = "-The subtitles may not be available for this video.\n-The video may no longer be available"
            return "Bad Request :( \n"+mssg
    except:
        mssg = "-The subtitles may not be available for this video.\n-The video may no longer be available"
        return "Bad Request :( \n"+mssg
   
