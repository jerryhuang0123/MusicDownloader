import filereader
import searchyoutube
from pytube import YouTube
import youtube_dl
import ffmpeg



ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
	'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        
    }],
}

songsToSearch = filereader.ReadMusicFile()
for song in songsToSearch:
	print(song)
	youtubeUrl = searchyoutube.SearchYoutube(song)
	print(youtubeUrl)
	ydl_opts['outtmpl'] = '/DownloadedMusic/' + song.replace('\n', '') + '.mp3',
	print(ydl_opts['outtmpl'])
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([youtubeUrl])
	#yt = YouTube(youtubeUrl)
	#yt = yt.get('mp4', '720p')

	#yt.download('/DownloadedMusic', song)
	#mp4 = "'%s'.mp4" % song
	#mp3 = "'%s'.mp3" % song
	#ffmpeg -i mp4 mp3
#yt = YouTube("https://www.youtube.com/watch?v=n06H7OcPd-g")
#yt = yt.get('mp3', '720p')
#yt.download('/DownloadedMusic')