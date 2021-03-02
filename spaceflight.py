#--------------------------------------------------------------------------
# Simple animation using Canvas with Tkinter
# by Sebastian Schiwietz
#--------------------------------------------------------------------------

from tkinter import *
import random

class Application(Frame):
    """Spaceflight animation using primitives on a Canvas"""

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.c = Canvas(master, width=500, height=500, bg="gray5")
        self.c.pack()

        # Planet
        self.planet = []
        self.planet.append(self.c.create_oval(50, 50, 150, 150, fill="turquoise3", width=0))
        self.planet.append(self.c.create_oval(60, 60, 145, 145, fill="turquoise2", width=0))
        self.planet.append(self.c.create_oval(70, 70, 140, 140, fill="turquoise1", width=0))
        self.planet.append(self.c.create_oval(80, 80, 135, 135, fill="cyan", width=0))
        self.planet.append(self.c.create_line(
            48, 100, 10, 120, 90, 130, 110, 125, 130, 120, 190, 90, 150, 85,
            smooth=1, fill="lightgrey", width=4))

        # Particles
        self.p_nr = 40
        self.p = []

        for i in range(self.p_nr):
            start_x = random.randrange(1, 500)
            start_y = random.randrange(1, 500)
            temp = self.c.create_line(start_x, start_y, start_x, start_y+3, fill="white")
            self.p.append(temp)

        # Ship
        self.c.create_polygon(250, 400, 280, 450, 220, 450, fill="red")
        self.c.create_line(270, 415, 270, 440, width=3, fill="lightgrey")
        self.c.create_line(230, 415, 230, 440, width=3, fill="lightgrey")
        self.c.create_polygon(265, 425, 330, 460, 270, 450, fill="grey")
        self.c.create_polygon(235, 425, 230, 450, 170, 460, fill="grey")
        self.c.create_polygon(250, 410, 255, 420, 250, 430, 245, 420, fill="lightblue")
        # Exhaust
        self.flame_state = 0
        self.flame = self.c.create_polygon(245, 455, 255, 455, 250, 470, fill="orange")

        # Text
        self.c.create_text(250, 50, text="Spaceflight", font=("Fixedsys", 48), fill="springgreen")

        # Start
        self.ani_init()

    def ani_init(self):
        """Start animation"""
        self.ani_particle()
        self.ani_planet()
        self.ani_flame()

    def ani_particle(self):
        """Move particles from top to bottom"""
        for i in range(self.p_nr):
            # Change speed of particles for parallax effect
            if i < 20:
                self.c.move(self.p[i], 0, 2)
            else:
                self.c.move(self.p[i], 0, 3)
            # Reset particles when they leave the canvas
            if self.c.coords(self.p[i])[1] > 500:
                temp = random.randrange(1, 500)
                self.c.coords(self.p[i], temp, -10, temp, -7)

        self.c.after(10, self.ani_particle)

    def ani_planet(self):
        """Slowly move the planet downwards"""
        for x in self.planet:
            self.c.move(x, 0, 1)
        self.c.after(10, self.ani_planet)

    def ani_flame(self):
        """Animate the ship's exhaust"""
        if self.flame_state == 0:
            self.c.delete(self.flame)
            self.flame = self.c.create_polygon(245, 455, 255, 455, 250, 480, fill="orange")
            self.flame_state = 1
        else:
            self.c.delete(self.flame)
            self.flame = self.c.create_polygon(245, 455, 255, 455, 250, 470, fill="orange")
            self.flame_state = 0
        self.c.after(100, self.ani_flame)

        

if __name__ == "__main__":
    root = Tk()
    root.title("Spaceflight")
    app = Application(master=root)
    app.mainloop()
