import pyglet

def pl_sound(pl):
	if pl == True:
	    song = pyglet.media.load('videoplayback.wav')
        song.play()
    else:
        song.play()

pyglet.app.run()