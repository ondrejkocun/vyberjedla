import tkinter  #nastavenie platna
canvas=tkinter.Canvas(width=500,height=200)
canvas.pack()
farby=['green','red','blue','orange']   #deklarovanie zoznamu
farby1=['z','c','m','o']    #deklarovanie zoznamu
subor=open('vyberjedla.txt','w')    #otvorenie textaku
x=30    #nastavenie premmenej na hodnotu 30
for i in range(4):  #cyklus na kreslenie stvorcov
    canvas.create_rectangle(x,50,x+100,150,fill=farby[i])
    x+=+110 #zvacsenie premmenej 
 
canvas.create_text(250,25,text='Výber jedla',font='Arial 25 ',fill='red')   #vypisanie textu 

def klik(event):    #funkcia spustena kliknutim
    subor=open('vyberjedla.txt','a')    #otvorenie suboru na pridavanie
    xy=30   #nastavenie premmenej
    x=event.x   #nastaevnie premmenej na aktualnu poziciu mysi
    y=event.y   #nastavenie premmenej na aktualnu poziciiu mysi
    text=entry1.get()   #nastavenie premmenej na vysledok z entry
    if text!='':    #podmienka ktora povoli zapisovanie az vtedy ak nieje prazdne entry
        for i in range(4):  #cyklus na zistenie kde sa nachadza mys
            if y>50 and y<150 and x>xy and x<xy+120:
                text+=' '+farby1[i]+'\n'    #pridanie farbu stvorca na ktorej bola mys do premmenej
                subor.write(text)   #zapis premmenej do textaku
            xy+=110 #zvacsenie premennej
        subor.close()   #zavretie suboru
entry1=tkinter.Entry()  #nastavenie entry
entry1.pack() 
canvas.bind('<Button-1>',klik) #nastavenie bindu 
