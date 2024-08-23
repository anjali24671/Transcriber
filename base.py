def getContent(video_url, video_lang):
    print("Trying to preprocess")
    try:
        # Extract video_id based on URL format
        if 'youtube.com' in video_url:
            video_id = video_url.split('v=')[-1]
            print(f"Extracted video_id: {video_id}")
        else:
            video_id = video_url[17:28]
            print(f"Extracted video_id: {video_id}")

        try:
            # Import and call the API
            from youtube_transcript_api import YouTubeTranscriptApi
            print("Calling YouTubeTranscriptApi")
            content = YouTubeTranscriptApi.get_transcript(video_id, languages=[video_lang])
            print(f"Transcript content: {content}")

            # Format the transcript content
            beautyContent = ' '.join([elem['text'] for elem in content])
            return beautyContent

        except Exception as e:
            # Print detailed error message
            print(f"Error in YouTubeTranscriptApi: {e}")
            mssg = "-The subtitles may not be available for this video.\n-The video may no longer be available"
            return "Bad Request :( \n" + mssg

    except Exception as e:
        # Print detailed error message
        print(f"Error in preprocessing: {e}")
        mssg = "-The subtitles may not be available for this video.\n-The video may no longer be available"
        return "Bad Request :( \n" + mssg
