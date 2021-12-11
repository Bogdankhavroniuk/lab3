
import pygame
import numpy as np
import math as m

class Viewer:
    def __init__(self, update_func, display_size):
        self.update_func = update_func
        pygame.init()
        self.display = pygame.display.set_mode(display_size)

    def set_title(self, title):
        pygame.display.set_caption(title)

    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            Z = create_image()
            surf = pygame.surfarray.make_surface(Z)
            self.display.blit(surf, (0, 0))




            pygame.display.update()

        pygame.quit()

def  buffering_line(line):
    buf = []
    b = ""
    for c in range(0, len(line)):


       if line[c] == " " :
           buf.append(int(b))
           b = ""
       if  c == len(line)-1:
           b = b + line[c]
           buf.append(int(b))
       else:
            b = b + line[c]

    return buf



def create_image():

   fi = float(0.349066)
   file1 = open('DS3.txt', 'r')
   start_list=[]
   while True:
           line = file1.readline()
           if buffering_line(line) != []:
             start_list.append(buffering_line(line))
           if not line:
               break
   for a in start_list:
       a[1] = a[1] - 480
       a[0] = a[0] - 480
       a[0] = round(a[0] * m.cos(fi) - a[1] * m.sin(fi))
       a[1] = round(a[0] * m.sin(fi) + a[1] * m.cos(fi))
       a[0] = a[0] + 480
       a[1] = a[1] + 480
   mas = np.zeros((960, 960, 3))

   for a in start_list:
       mas[a[0]][a[1]] = [0, 77, 255]


   return mas


def update():
   image = create_image()


   return image.astype('uint8')

viewer = Viewer(update(), (960, 960))
viewer.start()




