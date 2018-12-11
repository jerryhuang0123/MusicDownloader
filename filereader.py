def ReadMusicFile():
	musicFile = open("music.txt", "r")
	songsToSearch = musicFile.readlines()
	arr = []
	for song in songsToSearch:
		arr.append(song)
	return arr