import pygame
import os

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("Music Player")




MUSIC_FILE = r"C:\Users\Edik\Downloads"

songs = [song for song in os.listdir(MUSIC_FILE) if song.endswith(".mp3")]
if not songs :
    print("Not found MP3 file")
    exit()


current_song_index = 0
paused = False 

play_img = pygame.image.load(r"C:\Users\Edik\Downloads\play.png")
pause_img = pygame.image.load(r"C:\Users\Edik\Downloads\pause.png")
next_img = pygame.image.load(r"C:\Users\Edik\Downloads\next.png")
back_img = pygame.image.load(r"C:\Users\Edik\Downloads\back.png")

button_size =30
button_y = 300
play_rect = play_img.get_rect(center=(600 , button_y ))
pause_rect = pause_img.get_rect(center=(600, button_y))
next_rect = next_img.get_rect(center=(1100 , button_y))
back_rect = back_img.get_rect(center=(100 , button_y))



def play_music():
    pygame.mixer.music.load(os.path.join(MUSIC_FILE , songs[current_song_index]))
    pygame.mixer.music.play()
    print(f"Воспроизводится: {songs[current_song_index]}")

def stop_music():
    pygame.mixer.music.stop()
    print("⏹ Музыка остановлена")

def next_song():
    global current_song_index
    current_song_index = (current_song_index+1) % len(songs)
    play_music()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs) 
    play_music()

def pause_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        print("▶ Продолжение трека")  
    else:
        pygame.mixer.music.pause()
        print("⏸ Музыка на паузе")
    paused = not paused


running = True
while running:
    screen.fill((30,30,30))
    screen.blit(next_img,next_rect) 
    screen.blit(back_img,back_rect)

    if paused:
        screen.blit(play_img,play_rect)
    else:
        screen.blit(pause_img,pause_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos) and paused:
                pause_music()
            elif pause_rect.collidepoint(event.pos) and not paused:
                pause_music()
            elif next_rect.collidepoint(event.pos):
                next_song()
            elif back_rect.collidepoint(event.pos):
                prev_song()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause_music()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()
            elif event.key == pygame.K_s:
                stop_music()


                    
    pygame.display.flip()



pygame.quit()





