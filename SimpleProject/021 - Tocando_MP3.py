from pygame import mixer, event

mixer.init()
mixer.music.load('021-music.mp3')
mixer.music.play()
#p = input('Para parar a música aperte Enter...')
event.wait()
#mixer.music.stop()
