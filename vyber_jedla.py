import tkinter
canvas=tkinter.Canvas(width=500,height=200)
canvas.pack()
farby=['green','red','blue','orange']
farby1=['z','c','m','o']
subor=open('vyberjedla.txt','w')
x=30
for i in range(4):
    canvas.create_rectangle(x,50,x+100,150,fill=farby[i])
    x+=+110
 
canvas.create_text(250,25,text='Výber jedla',font='Arial 25 ',fill='red')

def klik(event):
    subor=open('vyberjedla.txt','a')
    xy=30
    x=event.x
    y=event.y
    text=entry1.get()
    print(x,y)
    if text!='':
        for i in range(4):
            if y>50 and y<150 and x>xy and x<xy+120:
                text+=' '+farby1[i]+'\n'
                subor.write(text)
            xy+=110
        subor.close()
entry1=tkinter.Entry()
entry1.pack()
canvas.bind('<Button-1>',klik)
