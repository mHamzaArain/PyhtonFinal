from pygame import mixer

# mixer.init()                                     -> To init file to play
# mixer.music.load("music.mp3")     -> This load file
# mixer.music.play()                          -> This play music 
# mixer.music.stop()                          -> This stop music

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break
