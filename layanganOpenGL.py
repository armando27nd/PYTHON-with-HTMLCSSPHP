import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Fungsi untuk menggambar layang-layang
def layangan():
    glBegin(GL_POLYGON)
    
    # Layang-layang memiliki 4 titik: atas, kanan, bawah, kiri
    glColor3f(0.0, 1.0, 0.0)  # Warna hijau untuk layang-layang
    glVertex2f(0, 0.7)          # Titik atas
    glVertex2f(0.5, 0)        # Titik kanan
    glVertex2f(0, -1)         # Titik bawah
    glVertex2f(-0.5, 0)   
    glEnd()

# Fungsi untuk menampilkan teks
def draw_text(x, y, text, font_size=48):
    font = pygame.font.SysFont("Arial", font_size)  # Menggunakan font Arial
    text_surface = font.render(text, True, (255, 255, 255), (0, 0, 0))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    
    glWindowPos2f(x, y)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

# Inisialisasi Pygame dan OpenGL
pygame.init()
pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)

# Atur tampilan OpenGL
glClearColor(0.0, 0.0, 0.0, 1.0)  # Latar belakang hitam
gluOrtho2D(-1, 1, -1, 1)          # Koordinat ortografis 2D

# Inisialisasi Pygame Font
pygame.font.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)
    
    # Gambar layang-layang
    # draw_kite()
    layangan()
    # Tambahkan teks "HARRY" di tengah layang-layang (koordinat sekitar layar)
    draw_text(370, 290, "HARRY")  # Letak teks (370, 290) pada layar
    
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
