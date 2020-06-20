from tkinter import *
import threading
import time
import random

global listEnemys1
global listEnemys2
global level


level = 1
listEnemys1 = []
listEnemys2 = []


# Frames

class GameFrame:
    def __init__(self):
        self.window = Tk()
        self.window.title("BulletHead")
        self.window.geometry("700x600+300+70")
        self.window.minsize(800, 600)
        self.window.resizable(width="NO", height="NO")
        self.window.config(bg="black")
        self.canvas = Canvas(self.window, width=700, height=600, bg="black")
        self.canvas.place(x=100, y=0)
        self.root = "resources/"
        # self.object = self.canvas.create_rectangle(200, 200, 200 + 50, 200 + 50,fill="white")

        # background_image = PhotoImage(file = self.root+"fondoenlaluna.png")
        # background_label = Label(self.canvas, image=background_image)
        # dbackground_label.place(x=0, y=0)

        self.player = Object("PLAYER", self)

        self.flag = True
        # mainthread = threading.Thread(target=self.loop, args=())
        # mainthread.start()

        rainThread = threading.Thread(target=self.rainEnemy, args=())
        rainThread.start()

        self.window.mainloop()

    def getCanvas(self):
        return self.canvas

    def getWindow(self):
        return self.window

    def loop(self):
        # for i in range(300):
        # self.canvas.move(self.object,i,0)
        # time.sleep(0.5)
        while self.flag:
            self.player.update()

    def rainEnemy(self):
        global listEnemys1, listEnemys2
        for i in range(level + 10):
            # e1 = Eenemy1(self.canvas)
            e2 = Eenemy2(self.canvas)
            listEnemys2 += [e2]

            # listEnemys2 += [e2]

            time.sleep(1.5)

        # while 1:
        # Eenemy1(self.canvas)
        # Eenemy2(self.canvas)
        # time.sleep(1.2)


class PlayFrame:
    def __init__(self):
        self.window = Tk()
        self.window.title("BulletHead")
        self.window.geometry("700x600+400+70")
        self.window.minsize(700, 600)
        self.window.resizable(width="NO", height="NO")
        self.window.config(bg="black")

        btn1Player = Button(self.window, width=10, text="ONE PLAYER", height=2, bg="white", fg="black",
                            activebackground="blue", command=self.openGame1Player)
        btn1Player.place(x=175, y=130)

        btn2Player = Button(self.window, width=10, text="TWO PLAYERS", height=2, bg="white", fg="black",
                            activebackground="blue", command=self.openGame2Player)
        btn2Player.place(x=475, y=130)

        btnMenu = Button(self.window, width=10, text="Back", height=2, bg="white", fg="black", activebackground="blue",
                         command=self.openMenuFrame)
        btnMenu.place(x=300, y=430)

        self.window.mainloop()

    def openMenuFrame(self):
        self.window.destroy()
        MenuFrame()

    def openGame1Player(self):
        self.window.destroy()
        GameFrame()

    def openGame2Player(self):
        self.window.destroy()
        GameFrame()


class ScoreFrame:
    def __init__(self):
        self.window = Tk()
        self.window.title("BulletHead")
        self.window.geometry("700x600+400+70")
        self.window.minsize(700, 600)
        self.window.resizable(width="NO", height="NO")
        self.window.config(bg="black")

        btnMenu = Button(self.window, width=10, text="Menu", height=2, bg="white", fg="black", activebackground="blue",
                         command=self.openMenuFrame)
        btnMenu.place(x=300, y=430)

        self.window.mainloop()

    def openMenuFrame(self):
        self.window.destroy()
        MenuFrame()


class HelpFrame:
    def __init__(self):
        self.window = Tk()
        self.window.title("BulletHead")
        self.window.geometry("700x600+400+70")
        self.window.minsize(700, 600)
        self.window.resizable(width="NO", height="NO")
        self.window.config(bg="black")

        btnMenu = Button(self.window, width=10, text="Menu", height=2, bg="white", fg="black", activebackground="blue",
                         command=self.openMenuFrame)
        btnMenu.place(x=300, y=430)

        self.window.mainloop()

    def openMenuFrame(self):
        self.window.destroy()
        MenuFrame()


class CreditsFrame:
    def __init__(self):
        self.window = Tk()
        self.window.title("BulletHead")
        self.window.geometry("700x600+400+70")
        self.window.minsize(700, 600)
        self.window.resizable(width="NO", height="NO")
        self.window.config(bg="black")

        btnMenu = Button(self.window, width=10, text="Menu", height=2, bg="white", fg="black", activebackground="blue",
                         command=self.openMenuFrame)
        btnMenu.place(x=300, y=430)

        self.window.mainloop()

    def openMenuFrame(self):
        self.window.destroy()
        MenuFrame()


class MenuFrame:
    def __init__(self):
        self.window = Tk()
        self.window.title("BulletHead")
        self.window.geometry("700x600+400+70")
        self.window.minsize(700, 600)
        self.window.resizable(width="NO", height="NO")
        self.window.config(bg="black")

        lblTitle = Label(text="BulletHead", bg="black", fg="white")
        lblTitle.place(x=300, y=150)

        # playImage = PhotoImage(file = "resources/start.png")
        btnPlay = Button(self.window, width=10, text="Play", height=2, bg="white", fg="black", activebackground="blue",
                         command=self.openPlayFrame)  # , image = playImage)
        btnPlay.place(x=300, y=280)

        # scoresImage = PhotoImage(file = "resources/score.png")
        btnScores = Button(self.window, width=10, text="Scores", height=2, bg="white", fg="black",
                           activebackground="blue", command=self.openScoreFrame)  # , image = scoresImage)
        btnScores.place(x=300, y=330)

        # helpImage = PhotoImage(file = "resources/bypss.png")
        btnHelp = Button(self.window, width=10, text="Help", height=2, bg="white", fg="black", activebackground="blue",
                         command=self.openHelpFrame)  # , image = helpImage)
        btnHelp.place(x=300, y=380)

        # creditsImgae = PhotoImage(file = "resources/credits.png")
        btnCredits = Button(self.window, width=10, text="Credits", height=2, bg="white", fg="black",
                            activebackground="blue", command=self.openCreditsFrame)  # , image = creditsImgae)
        btnCredits.place(x=300, y=430)

        self.window.mainloop()

    def openPlayFrame(self):
        self.window.destroy()
        PlayFrame()

    def openScoreFrame(self):
        self.window.destroy()
        ScoreFrame()

    def openHelpFrame(self):
        self.window.destroy()
        HelpFrame()

    def openCreditsFrame(self):
        self.window.destroy()
        CreditsFrame()


# Objects

class Object:
    def __init__(self, name="PLAYER", frame=None):
        self.life = 3
        self.name = name
        self.frame = frame
        self.window = frame.getWindow()
        self.canvas = self.frame.getCanvas()
        self.posx = 350
        self.posy = 500
        self.flagL = False
        self.flagR = False

        self.playerImage = PhotoImage(file='resources/spaceship.png')

        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.object = self.canvas.create_image(325, 500, image=self.playerImage, anchor=NW)
        # self.object2 = self.canvas.create_rectangle(self.posx, self.posy, self.posx + 50, self.posy + 50, fill="white")
        self.window.bind('<KeyPress>', lambda a: self.move(a))
        self.window.bind('<KeyRelease>', lambda a: self.shoot(a))
        self.window.bind("<space>", self.tjump)

    def update(self):
        if self.flagL:
            self.canvas.move(self.object, -20, 0)
            self.flagL = False
        elif self.flagR:
            self.canvas.move(self.object, 20, 0)
            self.flagR = False

    def move(self, event):
        key = event.char
        print(key, 'is pressed')

        if key == "a":
            t = threading.Thread(target=self.moveLeft, args=())
            t.start()

        elif key == "d":
            t = threading.Thread(target=self.moveRight, args=())
            t.start()

    def shoot(self, event):
        key = event.char
        if key == "w":
            self.shot()

    def moveLeft(self):
        for i in range(10):
            self.canvas.move(self.object, -3, 0)
            self.posx -= 3
            time.sleep(0.01)

    def moveRight(self):
        for i in range(10):
            self.canvas.move(self.object, 3, 0)
            self.posx += 3
            time.sleep(0.01)

    def tjump(self, event):
        t = threading.Thread(target=self.jump, args=())
        t.start()

    def jump(self):
        for i in range(6):
            self.posy -= 10
            self.canvas.move(self.object, 0, -10)
            time.sleep(0.03)
        for i in range(6):
            self.posy += 10
            self.canvas.move(self.object, 0, 10)
            time.sleep(0.03)

    def shot(self):
        Bullet(self.canvas, self.posx, self.posy)


class Bullet:
    def __init__(self, canvas, posx, posy):
        self.image = PhotoImage(file="resources/bullet.png")
        self.posx = posx-5
        self.posy = posy
        self.canvas = canvas
        self.object = self.canvas.create_image(self.posx , self.posy, image=self.image, anchor=NW)
        t = threading.Thread(target=self.init, args=())
        t.start()

    def init(self):
        global listEnemys1, listEnemys2
        for i in range(100):
            self.canvas.move(self.object, 0, -10)
            self.posy-=10
            for i in listEnemys2:
                if (self.posx > i.posx-32) and (self.posx < i.posx+50) and (self.posy< i.posy+50) and (self.posy > i.posy-50):
                    i.destroy()
                    print("colision")

            time.sleep(0.02)
        self.destroy()

    def destroy(self):
        self.canvas.delete(self.object)


class Eenemy1:
    def __init__(self, canvas):
        self.life = 1
        self.posx = random.randint(10, 650)

        self.posy = 0
        self.velocity = 0.05
        self.canvas = canvas
        self.image = PhotoImage(file="resources/granade.png")
        self.object = self.canvas.create_image(self.posx, self.posy, image=self.image, anchor=NW)

        t = threading.Thread(target=self.init, args=())
        t.start()

    def init(self):
        for i in range(60):
            self.canvas.move(self.object, 0, 10)
            self.posy += 10
            time.sleep(self.velocity)
        self.destroy()

    def destroy(self):
        self.canvas.delete(self.object)


class Eenemy2:
    def __init__(self, canvas):
        self.life = 1
        self.velocity = 0.05
        self.canvas = canvas
        self.posy = 0
        self.posx = 50
        self.image = PhotoImage(file="resources/satellite.png")
        self.object = self.canvas.create_image(self.posx, self.posy, image=self.image, anchor=NW)
        print("COORDS",self.canvas.coords(self.object))
        t = threading.Thread(target=self.init, args=())
        t.start()

    def init(self):
        move = 10
        while self.posy != 700:

            self.canvas.move(self.object, move, 0)
            self.posx += move

            if self.posx >= 650 or self.posx <= 10:
                move = -move
                self.posy += 65
                self.canvas.move(self.object, 0, 65)

            time.sleep(self.velocity)

        self.destroy()

    def destroy(self):
        self.canvas.delete(self.object)


frame = MenuFrame()
