from youtube_dl import YoutubeDL

# Download video:
dl_video = YoutubeDL()
dl_video.download(['https://www.youtube.com/watch?v=aNLmz22WrOQ'])

# Download audio:
options1 = {'format': 'best audio/audio'}

dl_audio = YoutubeDL(options)

dl_audio.download(['https://www.youtube.com/watch?v=8sgycukafqQ'])

# Search and download video :
options2 = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options)

dl.download(['I know you know'])
