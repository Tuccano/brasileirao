from tkinter import *

# Tupla de times
times = ('Santos', 'Palmeiras', 'Flamengo',
         'Internacional', 'Atlético MG', 'São Paulo',
         'Corinthians', 'Atlético PR', 'Botafogo',
         'Grêmio', 'Bahia', 'Goiás', 'Fortaleza',
         'Ceará', 'Vasco', 'Fluminense', 'Cruzeiro',
         'Chapecoense', 'CSA', 'Avaí')



def bt1_click():
    toptimes = Tk()
    toptimes.geometry("200x105")
    toptimes.title("5 Primeiros")
    lb1 = Label(toptimes, text=f"1. {times[1]}")
    lb2 = Label(toptimes, text=f"2. {times[2]}")
    lb3 = Label(toptimes, text=f"3. {times[3]}")
    lb4 = Label(toptimes, text=f"4. {times[4]}")
    lb5 = Label(toptimes, text=f"5. {times[5]}")
    lb1.pack()
    lb2.pack()
    lb3.pack()
    lb4.pack()
    lb5.pack()

def bt2_click():
    worstimes = Tk()
    worstimes.geometry("200x105")
    worstimes.title("5 Últimos")
    lb1 = Label(worstimes, text=f"20. {times[-1]}")
    lb2 = Label(worstimes, text=f"19. {times[-2]}")
    lb3 = Label(worstimes, text=f"18. {times[-3]}")
    lb4 = Label(worstimes, text=f"17. {times[-4]}")
    lb5 = Label(worstimes, text=f"16. {times[-5]}")
    lb1.pack()
    lb2.pack()
    lb3.pack()
    lb4.pack()
    lb5.pack()

def bt3_click():
    select = Tk()
    et = Entry(select)
    def time():
        if et.get() in times:
            lr["text"] = f"{et.get()} está na {times.index(et.get()) + 1}ª posição"
        else:
            lr["text"] = "Time inválido tente novamente"

    select.geometry("200x150")
    select.title("Colocação do time")
    txt = Label(select, text="Nome do time")
    bt = Button(select, width=10, text="OK", command=time)
    lr = Label(select, text="")
    txt.pack()
    et.pack()
    bt.pack()
    lr.pack()

# Propriedades da janela
# janela.geometry("375x200")

janela = Tk()

# Canvas
janela.title("VEM DE FUTEEEE")
canvas = Canvas(janela, width=375, height=200)
canvas.pack()

# Source
bgimg = PhotoImage(file = "fut.png")

# Background
canvas.create_image(0, 0, anchor='nw', image=bgimg)

# Layout
lb = Label(canvas, text="Brasileirão 2019", bg="white")
lb.pack(side=TOP, fill=X)
bt1 = Button(canvas, text="5 Primeiros colocados", command=bt1_click)
bt2 = Button(canvas, text="5 Últimos colocados", command=bt2_click)
bt3 = Button(canvas, text="Colocação de um time", command=bt3_click)
bt1.pack(side=LEFT, anchor=CENTER)
bt2.pack(side=LEFT, anchor=CENTER)
bt3.pack(side=LEFT, anchor=CENTER)

janela.mainloop()
