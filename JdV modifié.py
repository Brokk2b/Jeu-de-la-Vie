from tkinter import *

def damier(): #fonction dessinant le tableau
    ligne_vert()
    ligne_hor()
        
def ligne_vert():
    c_x = 0
    while c_x != width:
        can1.create_line(c_x,0,c_x,height,width=1,fill='black')
        c_x+=c
        
def ligne_hor():
    c_y = 0
    while c_y != height:
        can1.create_line(0,c_y,width,c_y,width=1,fill='black')
        c_y+=c

def click_gauche(event): #fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au dico_case
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='black')
    dico_case[x,y]=1

def click_droit(event): #fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au dico_case
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='white')
    dico_case[x,y]=0

def change_vit(event): #fonction pour changer la vitesse(l'attente entre chaque étape)
    global vitesse
    vitesse = int(eval(entree.get()))
    print(vitesse)

def prepa():
    dico_case[2*c,2*c]=1
    can1.create_rectangle(2*c, 2*c, 2*c+c, 2*c+c, fill='black')
    dico_case[2*c,3*c]=1
    can1.create_rectangle(2*c, 3*c, 2*c+c, 3*c+c, fill='black')
    dico_case[2*c,4*c]=1
    can1.create_rectangle(2*c, 4*c, 2*c+c, 4*c+c, fill='black')
    dico_case[2*c,5*c]=1
    can1.create_rectangle(2*c, 5*c, 2*c+c, 5*c+c, fill='black')
    dico_case[2*c,6*c]=1
    can1.create_rectangle(2*c, 6*c, 2*c+c, 6*c+c, fill='black')
    dico_case[3*c,2*c]=1
    can1.create_rectangle(3*c, 2*c, 3*c+c, 2*c+c, fill='black')
    dico_case[4*c,2*c]=1
    can1.create_rectangle(4*c, 2*c, 4*c+c, 2*c+c, fill='black')
    dico_case[4*c,3*c]=1
    can1.create_rectangle(4*c, 3*c, 4*c+c, 3*c+c, fill='black')
    dico_case[4*c,4*c]=1
    can1.create_rectangle(4*c, 4*c, 4*c+c, 4*c+c, fill='black')
    dico_case[3*c,4*c]=1
    can1.create_rectangle(3*c, 4*c, 3*c+c, 4*c+c, fill='black')
    #P
    dico_case[6*c,2*c]=1
    can1.create_rectangle(6*c, 2*c, 6*c+c, 2*c+c, fill='black')
    dico_case[6*c,3*c]=1
    can1.create_rectangle(6*c, 3*c, 6*c+c, 3*c+c, fill='black')
    dico_case[6*c,4*c]=1
    can1.create_rectangle(6*c, 4*c, 6*c+c, 4*c+c, fill='black')
    dico_case[6*c,5*c]=1
    can1.create_rectangle(6*c, 5*c, 6*c+c, 5*c+c, fill='black')
    dico_case[6*c,6*c]=1
    can1.create_rectangle(6*c, 6*c, 6*c+c, 6*c+c, fill='black')
    dico_case[7*c,2*c]=1
    can1.create_rectangle(7*c, 2*c, 7*c+c, 2*c+c, fill='black')
    dico_case[8*c,2*c]=1
    can1.create_rectangle(8*c, 2*c, 8*c+c, 2*c+c, fill='black')
    dico_case[8*c,3*c]=1
    can1.create_rectangle(8*c, 3*c, 8*c+c, 3*c+c, fill='black')
    dico_case[7*c,4*c]=1
    can1.create_rectangle(7*c, 4*c, 7*c+c, 4*c+c, fill='black')
    dico_case[8*c,5*c]=1
    can1.create_rectangle(8*c, 5*c, 8*c+c, 5*c+c, fill='black')
    dico_case[8*c,6*c]=1
    can1.create_rectangle(8*c, 6*c, 8*c+c, 6*c+c, fill='black')
    #R
    dico_case[10*c,2*c]=1
    can1.create_rectangle(10*c, 2*c, 10*c+c, 2*c+c, fill='black')
    dico_case[10*c,3*c]=1
    can1.create_rectangle(10*c, 3*c, 10*c+c, 3*c+c, fill='black')
    dico_case[10*c,4*c]=1
    can1.create_rectangle(10*c, 4*c, 10*c+c, 4*c+c, fill='black')
    dico_case[10*c,5*c]=1
    can1.create_rectangle(10*c, 5*c, 10*c+c, 5*c+c, fill='black')
    dico_case[10*c,6*c]=1
    can1.create_rectangle(10*c, 6*c, 10*c+c, 6*c+c, fill='black')
    dico_case[11*c,2*c]=1
    can1.create_rectangle(11*c, 2*c, 11*c+c, 2*c+c, fill='black')
    dico_case[12*c,2*c]=1
    can1.create_rectangle(12*c, 2*c, 12*c+c, 2*c+c, fill='black')
    dico_case[11*c,4*c]=1
    can1.create_rectangle(11*c, 4*c, 11*c+c, 4*c+c, fill='black')
    dico_case[11*c,6*c]=1
    can1.create_rectangle(11*c, 6*c, 11*c+c, 6*c+c, fill='black')
    dico_case[12*c,6*c]=1
    can1.create_rectangle(12*c, 6*c, 12*c+c, 6*c+c, fill='black')
    #E
    dico_case[14*c,2*c]=1
    can1.create_rectangle(14*c, 2*c, 14*c+c, 2*c+c, fill='black')
    dico_case[14*c,3*c]=1
    can1.create_rectangle(14*c, 3*c, 14*c+c, 3*c+c, fill='black')
    dico_case[14*c,4*c]=1
    can1.create_rectangle(14*c, 4*c, 14*c+c, 4*c+c, fill='black')
    dico_case[14*c,5*c]=1
    can1.create_rectangle(14*c, 5*c, 14*c+c, 5*c+c, fill='black')
    dico_case[14*c,6*c]=1
    can1.create_rectangle(14*c, 6*c, 14*c+c, 6*c+c, fill='black')
    dico_case[15*c,2*c]=1
    can1.create_rectangle(15*c, 2*c, 15*c+c, 2*c+c, fill='black')
    dico_case[16*c,2*c]=1
    can1.create_rectangle(16*c, 2*c, 16*c+c, 2*c+c, fill='black')
    dico_case[16*c,3*c]=1
    can1.create_rectangle(16*c, 3*c, 16*c+c, 3*c+c, fill='black')
    dico_case[16*c,4*c]=1
    can1.create_rectangle(16*c, 4*c, 16*c+c, 4*c+c, fill='black')
    dico_case[15*c,4*c]=1
    can1.create_rectangle(15*c, 4*c, 15*c+c, 4*c+c, fill='black')
    #P
    dico_case[18*c,3*c]=1
    can1.create_rectangle(18*c, 3*c, 18*c+c, 3*c+c, fill='black')
    dico_case[18*c,4*c]=1
    can1.create_rectangle(18*c, 4*c, 18*c+c, 4*c+c, fill='black')
    dico_case[18*c,5*c]=1
    can1.create_rectangle(18*c, 5*c, 18*c+c, 5*c+c, fill='black')
    dico_case[18*c,6*c]=1
    can1.create_rectangle(18*c, 6*c, 18*c+c, 6*c+c, fill='black')
    dico_case[19*c,2*c]=1
    can1.create_rectangle(19*c, 2*c, 19*c+c, 2*c+c, fill='black')
    dico_case[19*c,4*c]=1
    can1.create_rectangle(19*c, 4*c, 19*c+c, 4*c+c, fill='black')
    dico_case[20*c,3*c]=1
    can1.create_rectangle(20*c, 3*c, 20*c+c, 3*c+c, fill='black')
    dico_case[20*c,4*c]=1
    can1.create_rectangle(20*c, 4*c, 20*c+c, 4*c+c, fill='black')
    dico_case[20*c,5*c]=1
    can1.create_rectangle(20*c, 5*c, 20*c+c, 5*c+c, fill='black')
    dico_case[20*c,6*c]=1
    can1.create_rectangle(20*c, 6*c, 20*c+c, 6*c+c, fill='black')
    #A

def ecam():
    dico_case[2*c,2*c]=1
    can1.create_rectangle(2*c, 2*c, 2*c+c, 2*c+c, fill='black')
    dico_case[2*c,3*c]=1
    can1.create_rectangle(2*c, 3*c, 2*c+c, 3*c+c, fill='black')
    dico_case[2*c,4*c]=1
    can1.create_rectangle(2*c, 4*c, 2*c+c, 4*c+c, fill='black')
    dico_case[2*c,5*c]=1
    can1.create_rectangle(2*c, 5*c, 2*c+c, 5*c+c, fill='black')
    dico_case[2*c,6*c]=1
    can1.create_rectangle(2*c, 6*c, 2*c+c, 6*c+c, fill='black')
    dico_case[3*c,2*c]=1
    can1.create_rectangle(3*c, 2*c, 3*c+c, 2*c+c, fill='black')
    dico_case[4*c,2*c]=1
    can1.create_rectangle(4*c, 2*c, 4*c+c, 2*c+c, fill='black')
    dico_case[4*c,6*c]=1
    can1.create_rectangle(4*c, 6*c, 4*c+c, 6*c+c, fill='black')
    dico_case[3*c,4*c]=1
    can1.create_rectangle(3*c, 4*c, 3*c+c, 4*c+c, fill='black')
    dico_case[3*c,6*c]=1
    can1.create_rectangle(3*c, 6*c, 3*c+c, 6*c+c, fill='black')
    #E
    dico_case[6*c,2*c]=1
    can1.create_rectangle(6*c, 2*c, 6*c+c, 2*c+c, fill='black')
    dico_case[6*c,3*c]=1
    can1.create_rectangle(6*c, 3*c, 6*c+c, 3*c+c, fill='black')
    dico_case[6*c,4*c]=1
    can1.create_rectangle(6*c, 4*c, 6*c+c, 4*c+c, fill='black')
    dico_case[6*c,5*c]=1
    can1.create_rectangle(6*c, 5*c, 6*c+c, 5*c+c, fill='black')
    dico_case[6*c,6*c]=1
    can1.create_rectangle(6*c, 6*c, 6*c+c, 6*c+c, fill='black')
    dico_case[7*c,2*c]=1
    can1.create_rectangle(7*c, 2*c, 7*c+c, 2*c+c, fill='black')
    dico_case[8*c,2*c]=1
    can1.create_rectangle(8*c, 2*c, 8*c+c, 2*c+c, fill='black')
    dico_case[7*c,6*c]=1
    can1.create_rectangle(7*c, 6*c, 7*c+c, 6*c+c, fill='black')
    dico_case[8*c,6*c]=1
    can1.create_rectangle(8*c, 6*c, 8*c+c, 6*c+c, fill='black')
    #C
    dico_case[12*c,5*c]=1
    can1.create_rectangle(12*c, 5*c, 12*c+c, 5*c+c, fill='black')
    dico_case[10*c,3*c]=1
    can1.create_rectangle(10*c, 3*c, 10*c+c, 3*c+c, fill='black')
    dico_case[10*c,4*c]=1
    can1.create_rectangle(10*c, 4*c, 10*c+c, 4*c+c, fill='black')
    dico_case[10*c,5*c]=1
    can1.create_rectangle(10*c, 5*c, 10*c+c, 5*c+c, fill='black')
    dico_case[10*c,6*c]=1
    can1.create_rectangle(10*c, 6*c, 10*c+c, 6*c+c, fill='black')
    dico_case[11*c,2*c]=1
    can1.create_rectangle(11*c, 2*c, 11*c+c, 2*c+c, fill='black')
    dico_case[12*c,6*c]=1
    can1.create_rectangle(12*c, 6*c, 12*c+c, 6*c+c, fill='black')
    dico_case[12*c,3*c]=1
    can1.create_rectangle(12*c, 3*c, 12*c+c, 3*c+c, fill='black')
    dico_case[12*c,4*c]=1
    can1.create_rectangle(12*c, 4*c, 12*c+c, 4*c+c, fill='black')
    dico_case[11*c,4*c]=1
    can1.create_rectangle(11*c, 4*c, 11*c+c, 4*c+c, fill='black')
    #A
    dico_case[14*c,2*c]=1
    can1.create_rectangle(14*c, 2*c, 14*c+c, 2*c+c, fill='black')
    dico_case[14*c,3*c]=1
    can1.create_rectangle(14*c, 3*c, 14*c+c, 3*c+c, fill='black')
    dico_case[14*c,4*c]=1
    can1.create_rectangle(14*c, 4*c, 14*c+c, 4*c+c, fill='black')
    dico_case[14*c,5*c]=1
    can1.create_rectangle(14*c, 5*c, 14*c+c, 5*c+c, fill='black')
    dico_case[14*c,6*c]=1
    can1.create_rectangle(14*c, 6*c, 14*c+c, 6*c+c, fill='black')
    dico_case[15*c,3*c]=1
    can1.create_rectangle(15*c, 3*c, 15*c+c, 3*c+c, fill='black')
    dico_case[16*c,4*c]=1
    can1.create_rectangle(16*c, 4*c, 16*c+c, 4*c+c, fill='black')
    dico_case[17*c,3*c]=1
    can1.create_rectangle(17*c, 3*c, 17*c+c, 3*c+c, fill='black')
    dico_case[18*c,2*c]=1
    can1.create_rectangle(18*c, 2*c, 18*c+c, 2*c+c, fill='black')
    dico_case[18*c,3*c]=1
    can1.create_rectangle(18*c, 3*c, 18*c+c, 3*c+c, fill='black')
    dico_case[18*c,4*c]=1
    can1.create_rectangle(18*c, 4*c, 18*c+c, 4*c+c, fill='black')
    dico_case[18*c,5*c]=1
    can1.create_rectangle(18*c, 5*c, 18*c+c, 5*c+c, fill='black')
    dico_case[18*c,6*c]=1
    can1.create_rectangle(18*c, 6*c, 18*c+c, 6*c+c, fill='black')
    #M
    dico_case[20*c,2*c]=1
    can1.create_rectangle(20*c, 2*c, 20*c+c, 2*c+c, fill='black')
    dico_case[20*c,3*c]=1
    can1.create_rectangle(20*c, 3*c, 20*c+c, 3*c+c, fill='black')
    dico_case[20*c,4*c]=1
    can1.create_rectangle(20*c, 4*c, 20*c+c, 4*c+c, fill='black')
    dico_case[20*c,6*c]=1
    can1.create_rectangle(20*c, 6*c, 20*c+c, 6*c+c, fill='black')
    #!

def canon(): #fonction dessinant le célèbre canon à planeur de Bill Gosper
    dico_case[0*c,5*c]=1
    dico_case[0*c,6*c]=1
    dico_case[1*c,5*c]=1
    dico_case[1*c,6*c]=1
    dico_case[10*c,5*c]=1
    dico_case[10*c,6*c]=1
    dico_case[10*c,7*c]=1
    dico_case[11*c,4*c]=1
    dico_case[11*c,8*c]=1
    dico_case[12*c,3*c]=1
    dico_case[12*c,9*c]=1
    dico_case[13*c,3*c]=1
    dico_case[13*c,9*c]=1
    dico_case[14*c,6*c]=1
    dico_case[15*c,4*c]=1
    dico_case[15*c,8*c]=1
    dico_case[16*c,5*c]=1
    dico_case[16*c,6*c]=1
    dico_case[16*c,7*c]=1
    dico_case[17*c,6*c]=1
    dico_case[20*c,3*c]=1
    dico_case[20*c,4*c]=1
    dico_case[20*c,5*c]=1
    dico_case[21*c,3*c]=1
    dico_case[21*c,4*c]=1
    dico_case[21*c,5*c]=1
    dico_case[22*c,2*c]=1
    dico_case[22*c,6*c]=1
    dico_case[24*c,1*c]=1
    dico_case[24*c,2*c]=1
    dico_case[24*c,6*c]=1
    dico_case[24*c,7*c]=1
    dico_case[34*c,3*c]=1
    dico_case[34*c,4*c]=1
    dico_case[35*c,3*c]=1
    dico_case[35*c,4*c]=1    
    go()

def go():
    "démarrage de l'animation"
    global flag
    if flag ==0:
        flag =1
        play()
        
def stop():
    "arrêt de l'animation"
    global flag    
    flag =0

def clear():
    for i in range(int(height/c)):
        for j in range(int(width/c)):
            dico_case[j*c,i*c]=0
            can1.create_rectangle(j*c, i*c, j*c+c, i*c+c, fill='white')
            

def play(): #fonction comptant le nombre de cellules vivantes autour de chaque cellule
    global flag, vitesse
    v=0
    while v!= width/c:
        w=0
        while w!= height/c:
            x=v*c
            y=w*c
            
            # cas spéciaux:
            # les coins
            if x==0 and y==0: #coin en haut à gauche
                compt_viv=0
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==0 and y==int(height-c): #coin en bas à gauche
                compt_viv=0
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==int(width-c) and y==0: #coin en haut à droite
                compt_viv=0
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==int(width-c) and y==int(height-c): #coin en bas à droite
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
                
            # cas spéciaux:
            # les bords du tableau (sans les coins)    
            elif x==0 and 0<y<int(height-c): # bord de gauche
                compt_viv=0
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==int(width-c) and 0<y<int(height-c): # bord de droite
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif 0<x<int(width-c) and y==0: # bord du haut
                compt_viv=0
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif 0<x<int(width-c) and y==int(height-c): # bord du bas
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv

            #cas généraux
            #les cellules qui ne sont pas dans les bords du tableau
            else:
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
                
            w+=1
        v+=1
    redessiner()
    if flag >0: 
        fen1.after(vitesse,play)

        

def redessiner(): #fonction redessinant le tableau à partir de dico_etat
    can1.delete(ALL)
    damier()
    t=0
    while t!= width/c:
        u=0
        while u!= height/c:
            x=t*c
            y=u*c
            if dico_case[x,y]==0:
                if dico_etat[x,y]==0 or dico_etat[x,y]==1 or dico_etat[x,y]==3 or dico_etat[x,y]==4 or dico_etat[x,y]==6 or dico_etat[x,y]==8:
                    dico_case[x,y]=1
                    can1.create_rectangle(x, y, x+c, y+c, fill='black')
                else:
                    can1.create_rectangle(x, y, x+c, y+c, fill='white')
            else:
                if dico_etat[x,y]==0 or dico_etat[x,y]==4 or dico_etat[x,y]==5 or dico_etat[x,y]==6:
                    can1.create_rectangle(x, y, x+c, y+c, fill='black')
                else:
                    dico_case[x,y]=0
                    can1.create_rectangle(x, y, x+c, y+c, fill='white')

            u+=1
        t+=1
        
#les différentes variables:

#taille de la grille
height = 70
width = 50

#taille des cellules
c = 10

#vitesse de l'animation (en réalité c'est l'attente entre chaque étapes en ms)
vitesse=50

flag=0
dico_etat = {} #dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
dico_case = {} #dictionnaire contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes
i=0
while i!= width/c: #assigne une valeur 0(morte) a chaque coordonnées(cellules)
    j=0
    while j!= height/c:
        x=i*c
        y=j*c
        dico_case[x,y]=0
        j+=1
    i+=1

#programme "principal" 
fen1 = Tk()

can1 = Canvas(fen1, width =width, height =height, bg ='white')
can1.bind("<Button-1>", click_gauche)
can1.bind("<Button-3>", click_droit)
can1.pack(side =TOP, padx =5, pady =5)

damier()

b1 = Button(fen1, text ='Go!', command =go)
b2 = Button(fen1, text ='Stop', command =stop)
b1.pack(side =LEFT, padx =3, pady =3)
b2.pack(side =LEFT, padx =3, pady =3)
b3 = Button(fen1, text ='Canon planeur', command =canon)
b3.pack(side =LEFT, padx =3, pady =3)
b4 = Button(fen1, text ='PREPA', command =prepa)
b4.pack(side =LEFT, padx =3, pady =3)
b5 = Button(fen1, text ='ECAM', command =ecam)
b5.pack(side =LEFT, padx =3, pady =3)
b6 = Button(fen1, text ='CLEAR', command =clear)
b6.pack(side =LEFT, padx =3, pady =3)

entree = Entry(fen1)
entree.bind("<Return>", change_vit)
entree.pack(side =RIGHT)
chaine = Label(fen1)
chaine.configure(text = "Attente entre chaque étape (ms) :")
chaine.pack(side =RIGHT)

fen1.mainloop()
