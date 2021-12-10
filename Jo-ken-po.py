from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random


def desabilitar():
    b_pedra["state"] = DISABLED
    b_papel["state"] = DISABLED
    b_tesoura["state"] = DISABLED


def pedra_player():
    image_x = Image.open(
        "directory/icons"
    )
    icon_x = ImageTk.PhotoImage(image_x)

    image_pedra = Image.open(
        "directory/icons"
    )
    icon_pedra = ImageTk.PhotoImage(image_pedra)

    image_papel = Image.open(
        "directory/icons"
    )
    icon_papel = ImageTk.PhotoImage(image_papel)

    image_tesoura = Image.open(
        "directory/icons"
    )
    icon_tesoura = ImageTk.PhotoImage(image_tesoura)

    l_pedra = Label(root_play, image=icon_pedra, bg="light yellow")
    l_pedra.image = icon_pedra
    l_pedra.place(x=50, y=80)
    l_x = Label(root_play, image=icon_x, bg="light yellow")
    l_x.image = icon_x
    l_x.place(x=217, y=130)
    escolha = ["pedra", "papel", "tesoura"]
    computador = random.choice(escolha)
    if computador == "pedra":
        l_pedra1 = Label(root_play, image=icon_pedra, bg="light yellow")
        l_pedra1.image = icon_pedra
        l_pedra1.place(x=300, y=80)
        l_initial.configure(text="Empate!", fg="black", font=("Fira Code", 30))
        l_initial.place(x=160, y=10)
    elif computador == "papel":
        l_papel1 = Label(root_play, image=icon_papel, bg="light yellow")
        l_papel1.image = icon_papel
        l_papel1.place(x=300, y=80)
        l_initial.configure(text="Você perdeu!", fg="red", font=("Fira Code", 30))
        l_initial.place(x=100, y=10)
    elif computador == "tesoura":
        l_tesoura1 = Label(root_play, image=icon_tesoura, bg="light yellow")
        l_tesoura1.image = icon_tesoura
        l_tesoura1.place(x=300, y=80)
        l_initial.configure(text="Você ganhou!", fg="blue", font=("Fira Code", 30))
        l_initial.place(x=100, y=10)

    desabilitar()


def papel_player():
    image_x = Image.open(
        "directory/icons"
    )
    icon_x = ImageTk.PhotoImage(image_x)

    image_pedra = Image.open(
        "directory/icons"
    )
    icon_pedra = ImageTk.PhotoImage(image_pedra)

    image_papel = Image.open(
        "directory/icons"
    )
    icon_papel = ImageTk.PhotoImage(image_papel)

    image_tesoura = Image.open(
        "directory/icons"
    )
    icon_tesoura = ImageTk.PhotoImage(image_tesoura)
    l_papel = Label(root_play, image=icon_papel, bg="light yellow")
    l_papel.image = icon_papel
    l_papel.place(x=50, y=80)
    l_x = Label(root_play, image=icon_x, bg="light yellow")
    l_x.image = icon_x
    l_x.place(x=217, y=130)
    escolha = ["pedra", "papel", "tesoura"]
    computador = random.choice(escolha)
    if computador == "pedra":
        l_pedra1 = Label(root_play, image=icon_pedra, bg="light yellow")
        l_pedra1.image = icon_pedra
        l_pedra1.place(x=300, y=80)
        l_initial.configure(text="Você ganhou!", fg="blue", font=("Fira Code", 30))
        l_initial.place(x=100, y=10)
    elif computador == "papel":
        l_papel1 = Label(root_play, image=icon_papel, bg="light yellow")
        l_papel1.image = icon_papel
        l_papel1.place(x=300, y=80)
        l_initial.configure(text="Empate!", fg="black", font=("Fira Code", 30))
        l_initial.place(x=160, y=10)
    elif computador == "tesoura":
        l_tesoura1 = Label(root_play, image=icon_tesoura, bg="light yellow")
        l_tesoura1.image = icon_tesoura
        l_tesoura1.place(x=300, y=80)
        l_initial.configure(text="Você perdeu!", fg="red", font=("Fira Code", 30))
        l_initial.place(x=100, y=10)

    desabilitar()


def tesoura_player():
    image_x = Image.open(
        "directory/icons"
    )
    icon_x = ImageTk.PhotoImage(image_x)

    image_pedra = Image.open(
        "directory/icons"
    )
    icon_pedra = ImageTk.PhotoImage(image_pedra)

    image_papel = Image.open(
        "directory/icons"
    )
    icon_papel = ImageTk.PhotoImage(image_papel)

    image_tesoura = Image.open(
        "directory/icons"
    )
    icon_tesoura = ImageTk.PhotoImage(image_tesoura)
    l_tesoura = Label(root_play, image=icon_tesoura, bg="light yellow")
    l_tesoura.image = icon_tesoura
    l_tesoura.place(x=50, y=80)
    l_x = Label(root_play, image=icon_x, bg="light yellow")
    l_x.image = icon_x
    l_x.place(x=217, y=130)
    escolha = ["pedra", "papel", "tesoura"]
    computador = random.choice(escolha)
    if computador == "pedra":
        l_pedra1 = Label(root_play, image=icon_pedra, bg="light yellow")
        l_pedra1.image = icon_pedra
        l_pedra1.place(x=300, y=80)
        l_initial.configure(text="Você perdeu!", fg="red", font=("Fira Code", 30))
        l_initial.place(x=100, y=10)
    elif computador == "papel":
        l_papel1 = Label(root_play, image=icon_papel, bg="light yellow")
        l_papel1.image = icon_papel
        l_papel1.place(x=300, y=80)
        l_initial.configure(text="Você ganhou!", fg="blue", font=("Fira Code", 30))
        l_initial.place(x=100, y=10)
    elif computador == "tesoura":
        l_tesoura1 = Label(root_play, image=icon_tesoura, bg="light yellow")
        l_tesoura1.image = icon_tesoura
        l_tesoura1.place(x=300, y=80)
        l_initial.configure(text="Empate!", fg="black", font=("Fira Code", 30))
        l_initial.place(x=160, y=10)

    desabilitar()


def refresh():
    root_play.destroy()
    jogar()


def voltar():
    root_play.destroy()


def sair():
    messagebox.showinfo(title="Sucesso!", message="Você saiu do jogo com sucesso!")
    root.destroy()
    exit()


def player_botoes():
    global b_pedra
    global b_papel
    global b_tesoura

    b_pedra = Button(
        root_play,
        text="Pedra",
        font=("Fira Code", 20),
        width=7,
        height=1,
        bg="#eba205",
        command=pedra_player,
    )
    b_pedra.place(x=20, y=300)

    b_papel = Button(
        root_play,
        text="Papel",
        font=("Fira Code", 20),
        width=7,
        height=1,
        bg="#eba205",
        command=papel_player,
    )
    b_papel.place(x=187, y=300)

    b_tesoura = Button(
        root_play,
        text="Tesoura",
        font=("Fira Code", 20),
        width=7,
        height=1,
        bg="#eba205",
        command=tesoura_player,
    )
    b_tesoura.place(x=350, y=300)

    b_voltar = Button(
        root_play,
        text="Resetar",
        font=("Fira Code", 20),
        width=7,
        height=1,
        bg="#eba205",
        command=refresh,
    )
    b_voltar.place(x=110, y=380)
    b_voltar = Button(
        root_play,
        text="Sair",
        font=("Fira Code", 20),
        width=7,
        height=1,
        bg="#eba205",
        command=voltar,
    )
    b_voltar.place(x=260, y=380)


def status():
    global l_initial
    l_initial = Label(
        root_play,
        text="Escolha uma ação!",
        bg="light yellow",
        fg="black",
        font=("Fira Code", 30),
    )
    l_initial.place(x=42, y=10)


def jogar():
    global root_play
    root_play = Toplevel(root)
    root_play.title("Sessão")
    root_play.geometry("500x450")
    root_play.config(bg="light yellow")
    icone_jkp = PhotoImage(
        file="directory/icons"
    )
    root_play.iconphoto(True, icone_jkp)
    status()
    player_botoes()


def mainscreen():
    global icone_i
    global root
    root = Tk()
    root.title("Início")
    root.geometry("350x220")
    root.config(bg="#3297a8")
    icone_i = PhotoImage(
        file="directory/icons"
    )
    root.iconphoto(False, icone_i)
    l_main = Label(root, text="Bem vindo!", bg="#3297a8", font=("Courier New", 30))
    l_main.place(x=55, y=5)
    l_root = Label(
        root, text="Made by:", bg="#3297a8", font=("Courier New", 15), fg="black"
    )
    l_root.place(x=120, y=50)
    l_root1 = Label(root, text="Teti", bg="#3297a8", font=("Courier New", 15), fg="red")
    l_root1.place(x=140, y=75)
    b_root_play = Button(
        root,
        text="Jogar",
        font=("Fira Code", 20),
        bg="#00daff",
        command=jogar,
        width=7,
        height=1,
    )
    b_root_play.place(x=25, y=140)
    b_root_exit = Button(
        root,
        text="Sair",
        font=("Fira Code", 20),
        bg="#00daff",
        command=sair,
        width=7,
        height=1,
    )
    b_root_exit.place(x=195, y=140)
    root.lift()
    root.attributes("-topmost", True)
    root.after_idle(root.attributes, "-topmost", False)
    root.mainloop()


mainscreen()
