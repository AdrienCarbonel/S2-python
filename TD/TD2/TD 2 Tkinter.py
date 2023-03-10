import tkinter as tk
import random as rd
fen = tk.Tk()
fen.title("Mon Dessin")
cote = 500

fen.state('zoomed')
def creation_cercle():
    global cercle
    x, y = rd.randint(0,cote-100), rd.randint(0,cote-100)
    cercle = canevas.create_oval((x,y,x+100,y+100),fill="blue")

def creation_carre():
    global carre
    x1, y1 = rd.randint(0,cote-100), rd.randint(0,cote-100)
    carre = canevas.create_rectangle((x1,y1,x1+100,y1+100),fill="green")

def creation_croix():
    global croix
    x2, y2 = rd.randint(0,cote-100), rd.randint(0,cote-100)
    longueur = 50
    length = longueur / 2
    croix = canevas.create_polygon((x2,y2), (x2+length,y2), (x2+length,y2+longueur), (x2+length+longueur,y2+longueur), (x2+length+longueur,y2+longueur+length), (x2+length,y2+longueur+length),(x2+length,y2+longueur*2+length), (x2,y2+longueur*2+length),(x2,y2+longueur+length),(x2-longueur,y2+longueur+length),(x2-longueur,y2+longueur),(x2,y2+longueur), outline="white",fill="yellow")
    

def update():
    count = len(canevas.find_all())
    label.config(text="Nombre d'éléments  :" + str(count))
    fen.after(func=update,ms=10)

# Boutons

bouton1 = tk.Button(fen,text="Choisir une couleur",width=20,bg="purple",fg="cyan",font=("Arial New Roman","20","italic"))
bouton2 = tk.Button(fen,text="Cercle",command= creation_cercle,width=10,height=5,font=("Arial New Roman","20","italic"),bg="red",fg="cyan")
bouton3 = tk.Button(fen,text="Carré",width=10,height=5,font=("Arial New Roman","20","italic"),bg="red",fg="cyan",command=creation_carre)
bouton4 = tk.Button(fen,text="Croix",width=10,height=5,font=("Arial New Roman","20","italic"),bg="red",fg="cyan",command=creation_croix)

# Labels 



# Canevas 
canevas = tk.Canvas(fen,bg="black",width=500,height=500)
label = tk.Label(canevas,text="Nombre d'éléments :")
# Placement des Widgets 
bouton1.place(x=400,y=10)
bouton2.place(x=50,y=100)
bouton3.place(x=50,y=300)
bouton4.place(x=50,y=500)
label.place(x=350,y=0)
canevas.place(x=300,y=100)




update()

fen.mainloop()