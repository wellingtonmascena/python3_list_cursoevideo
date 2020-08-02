import pygame
import os
fileMp3 = os.path.join(os.path.dirname(__file__),'hero.mp3')
pygame.mixer.init()
pygame.mixer.music.load(fileMp3)
pygame.mixer.music.play()
input()
pygame.event.wait()