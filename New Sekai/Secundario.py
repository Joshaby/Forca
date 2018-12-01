from tkinter import *
from functools import partial
from tkinter import messagebox
import winsound
import string
import random
import os


def Autentica():
    def autenticar(x):
        if entrada1.get() == "" or entrada2.get() == "":
            resultado["text"] = "Entrada inválida"
        else:

            # VALIDAÇÃO DO ARQUIVO DO CADASTRO

            try:
                mae = open("./storage/bin/HTKFLAWH.txt", "r")
            except:
                mae = open("./storage/bin/HTKFLAWH.txt", "w")
            nao = False
            mae.close()
            mae = open("./storage/bin/HTKFLAWH.txt", "r")

            b = entrada1.get()
            lista = mae.readlines()
            for u in lista:
                linha = u.split('###')
                if linha[0] == b:
                    nao = True
                    break
            if not nao:
                resultado["text"] = "Usuário não cadastrado!"
                resultado["fg"] = "red"
            else:
                if entrada2.get() != linha[1][:-1]:
                    resultado["text"] = "Senha Incorreta!"
                else:
                    l.append(entrada1.get())
                    janela.destroy()
            mae.close()
            try:
                entrada1.delete(0, "end")
                entrada2.delete(0, "end")
            except:
                pass

    def cadastrar():
        texto1["text"] = "Novo Usuário"
        texto1["fg"] = "green"
        texto2["text"] = "Digite a Senha"
        texto2["fg"] = "green"
        texto1.pack()
        texto2.pack()
        if entrada1.get() == "":
            resultado["text"] = "Digite o nome de usuário"
        elif entrada2.get() == "":
            resultado["text"] = "Digite uma senha"
        else:
            try:
                mae = open("./storage/bin/HTKFLAWH.txt", "r")
            except:
                mae = open("./storage/bin/HTKFLAWH.txt", "w")
            mae.close()
            mae = open("./storage/bin/HTKFLAWH.txt", "r")
            linha = ''
            b = entrada1.get()
            cadastro = True
            for i in mae.readlines():
                i = i.split("###")
                if b == i[0]:
                    cadastro = False
                    break
            mae.close()
            if not cadastro:
                resultado["text"] = "Usuario já cadastrado"
                resultado["fg"] = "red"
                texto1["text"] = "Login"
                texto1["fg"] = "black"
                texto2["text"] = "Senha"
                texto2["fg"] = "black"
            else:
                mae = open("./storage/bin/HTKFLAWH.txt", "a")
                linha += "%s###" % entrada1.get()
                linha += entrada2.get()
                mae.write("%s\n" % linha)
                mae.close()
                resultado["text"] = "Cadastrado Com Sucesso!"
                texto1["text"] = "Login"
                texto1["fg"] = "black"
                texto2["text"] = "Senha"
                texto2["fg"] = "black"
                texto1.pack()
                texto2.pack()
                try:
                    lead = open("./storage/bin/QXHIUVFKK.txt", "a")
                except:
                    lead = open("./storage/bin/QXHIUVFKK.txt", "w")
                lead.write("%s###%d\n" % (b, 0))
                lead.close()
            try:
                entrada1.delete(0, "end")
                entrada2.delete(0, "end")
            except:
                pass

    l = []
    janela = Tk()
    janela.title('Autenticação')
    texto1 = Label(janela, text="Login")
    entrada1 = Entry(janela)
    janela.wm_resizable(0, 0)
    winsound.PlaySound("./storage/audios/menu.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    janela.update_idletasks()
    width = janela.winfo_width()
    height = janela.winfo_height()
    g = 2.5
    x = (janela.winfo_screenwidth() // g) - (width // g)
    y = (janela.winfo_screenheight() // g) - (height // g)
    janela.geometry('{}x{}+{}+{}'.format(240, 200, int(x), int(y)))
    janela.title("Jogo da Forca")
    janela.iconbitmap("./storage/imagens/icon.ico")
    texto2 = Label(janela, text='Senha')
    entrada2 = Entry(janela, show="*")
    botao1 = Button(janela, text='Logar', command=partial(autenticar, "x"))
    janela.bind("<Return>", autenticar)
    botao2 = Button(janela, text='Cadastrar', command=cadastrar)
    som = PhotoImage(file="./storage/imagens/soun.png")
    music = Button(janela, command=lambda: winsound.PlaySound("300", winsound.SND_ASYNC | winsound.SND_PURGE |
                                                              winsound.SND_NOWAIT))
    music.config(image=som, width="40", height="40", activebackground="white")
    resultado = Label(janela, text='')
    texto1.pack(anchor=CENTER)
    entrada1.pack(anchor=CENTER)
    texto2.pack(anchor=CENTER)
    entrada2.pack(anchor=CENTER)
    botao1.pack(anchor=CENTER, pady=5)
    botao2.pack(anchor=CENTER)
    resultado.pack(anchor=CENTER)
    music.pack(padx=100, pady=4)
    janela.mainloop()
    return l


# CIFRA DE VEGENRE


class Vegenere(object):
    def __init__(self, pal):
        self.Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.MenCripto = ""
        self.MenDescripto = ""
        self.Palavra = pal.upper()
        self.Chave = "FTH"
        self.lixo = ''
        self.A = len(self.Palavra)
        u = 0
        for i in range(self.A):
            try:
                self.lixo += self.Chave[u]
                u += 1
            except:
                u = 0
                self.lixo += self.Chave[u]
                u += 1

    def decript(self):
        l = ["Á", "É", "Í", "Ó", "Ú", "À", "È", "Ì", "Ò", "Ù", "Â", "Ê", "Î", "Ô", "Û", "Ã", "Õ", "Ç"]
        for i in range(self.A):
            if self.Palavra[i] in l:
                self.MenDescripto += self.Palavra[i]
            elif self.Palavra[i] == " " or self.Palavra[i] == "-":
                self.MenDescripto += "-"
            else:
                y = self.Alpha.find(self.Palavra[i])
                z = self.Alpha.find(self.lixo[i])
                c = (y - z) + 26
                self.MenDescripto += self.Alpha[c % 26]
        return "%s" % self.MenDescripto

    def encript(self):
        l = ["Á", "É", "Í", "Ó", "Ú", "À", "È", "Ì", "Ò", "Ù", "Â", "Ê", "Î", "Ô", "Û", "Ã", "Õ", "Ç"]
        for i in range(self.A):
            if self.Palavra[i] in l:
                self.MenCripto += self.Palavra[i]
            elif self.Palavra[i] == " " or self.Palavra[i] == "-":
                self.MenCripto += "-"
            else:
                y = self.Alpha.find(self.Palavra[i])
                z = self.Alpha.find(self.lixo[i])
                b = y + z
                self.MenCripto += self.Alpha[b % 26]
        return "%s" % self.MenCripto


def Forca_main():
    class Forca(object):
        def __init__(self, master):
            self.condmusic = True
            if self.condmusic:
                winsound.PlaySound("./storage/audios/TTD.wav",
                                   winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            self.tentadas = []
            self.dificuldade = 5
            self.score = 0
            try:
                ini = open("./storage/.int.txt", "r")
                self.inii = (ini.readline()).split("#")
                ini.close()
                self.score = int(self.inii[0])
                self.dificuldade = int(self.inii[1])
                os.remove("./storage/.int.txt")
            except:
                pass
            self.falhas = 0
            self.resultados = []
            self.palavra = ''
            self.test = 0
            self.palavra_raw = ''
            while len(self.palavra_raw) != self.dificuldade:
                self.v = open("./storage/bin/palavras.txt", "r")
                self.palavra_raw = random.choice(self.v.readlines()).upper()
                self.v.close()
                self.palavra_raw = self.palavra_raw[:-1]
                f = self.palavra_raw.rfind("#")
                self.dica = self.palavra_raw[f + 1:]
                self.palavra_raw = self.palavra_raw[:f - 2]
                self.palavra_raw = Vegenere(self.palavra_raw).decript()
            for i in self.palavra_raw:
                if i == "-" or i == " ":
                    self.resultados.append("-")
                else:
                    self.resultados.append("_")
                self.test += 1
                if i == "À" or i == "Á" or i == "Â" or i == "Ã":
                    self.palavra += "A"
                elif i == "Ç":
                    self.palavra += "C"
                elif i == "Í" or i == "Ì" or i == "Î":
                    self.palavra += "I"
                elif i == " ":
                    self.palavra += "-"
                elif i == "Ó" or i == "Ò" or i == "Ô" or i == "Õ":
                    self.palavra += "O"
                elif i == "É" or i == "È" or i == "Ê":
                    self.palavra += "E"
                elif i == "Ú" or i == "Ù" or i == "Û":
                    self.palavra += "U"
                else:
                    self.palavra += i
            print(self.palavra_raw, self.palavra)

            # CONSTRUÇÃO DA INTERFACE

            # FRAME DO BONECO
            self.frame1 = Frame(master, borderwidth=10, width=300)
            # FRAME LETRAS TENTADAS
            self.frame2 = Frame(master, bg="light gray")
            # FRAME PALAVRA AOVIVO
            self.frame3 = Frame(master, bg="light gray")
            # FRAME DO TECLADO
            self.frame4 = Frame(master, bg="light gray")

            self.frame1.pack(side=LEFT)
            self.frame2.pack()
            self.frame3.pack()
            self.frame4.pack(side=BOTTOM, pady=10)
            self.letras = string.ascii_uppercase

            def botao(x):
                self.tent["bg"] = "light gray"
                self.jogo["fg"] = "Green"
                if x in self.tentadas:
                    self.tent["bg"] = "red"
                    pass
                else:
                    self.tentadas.append(x)
                    self.tent["text"] += x
                    cond = False
                    for i in range(len(self.palavra)):
                        if x == self.palavra[i]:
                            self.resultados[i] = self.palavra_raw[i]
                            self.score += len(self.palavra)
                            self.scoreF["text"] = "Score:\n%d" % self.score
                            self.scoreF.pack()
                            cond = True
                    if not cond:
                        self.falhas += 1
                        self.jogo["fg"] = "red"
                        self.boneco.pack_forget()
                        faus = PhotoImage(file=("./storage/imagens/fim%d.png" % self.falhas))
                        self.boneco.update_idletasks()
                        self.boneco.configure(image=faus)
                        self.boneco.pack()
                        janela.update_idletasks()
                        winsound.PlaySound("./storage/audios/Errou.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    self.jogo["text"] = self.resultados
                    if self.falhas == 5:
                        messagebox.showinfo("Perdeu", "\nVOCÊ PERDEU!!!!!!!!!!            \n")
                        messagebox.showinfo("Perdeu", "A palavra secreta era:\n%s" % self.palavra_raw)
                        try:
                            self.score = self.inii[0]
                        except:
                            self.score = 0
                        if self.dificuldade > 5:
                            self.dificuldade -= 1
                        v = open("./storage/.int.txt", "w")
                        v.close()
                        v = open("./storage/.int.txt", "a")
                        v.write("{}#{}".format(self.score, self.dificuldade))
                        v.close()
                        self.forget()
                if self.resultados.count("_") == 0:
                    self.dificuldade += 2
                    winsound.PlaySound("./storage/audios/acertou.wav", winsound.SND_FILENAME | winsound.SND_ASYNC |
                                       winsound.SND_PURGE)
                    messagebox.showinfo("Você achou o ovo", "Parabéns você acertou a palavra secreta\n")
                    self.forget()

            framepd = Frame(self.frame3, bg="light gray")
            framepd.pack(pady=20)
            defal = PhotoImage(file="./storage/imagens/fim5.png")
            self.boneco = Label(self.frame1, bg="light gray")
            self.boneco.configure(image=defal)
            self.frame1.update_idletasks()
            self.boneco.pack()

            self.tent = Label(self.frame2, text="Tentadas  \n", borderwidth=3, font=("consolas", 20, "bold"),
                              bg="light gray")
            self.tent.pack(side=LEFT)

            self.subframe2 = Frame(self.frame2)
            self.subframe2.pack()

            self.scoreF = Label(self.subframe2, text="Score:%s" % self.score, borderwidth=3,
                                font=("consolas", 20, "bold"), bg="light gray")
            self.scoreF.pack(side=RIGHT)

            self.jogo = Label(framepd, text=self.resultados, borderwidth=3, bg="light gray",
                              font=("verdana", 20, "bold"), fg="Green")
            self.jogo.pack()

            self.dica = Label(framepd, text="%s" % Vegenere(self.dica).decript(), width=30, height=1, bg="light gray",
                              font=("verdana", 16, "bold"))
            self.dica.pack(pady=30)
            self.lista_de_botao = list(string.ascii_uppercase)
            for i in range(len(self.lista_de_botao)):
                if i % 7 == 0:
                    subframe = Frame(self.frame4, bg="black")
                    subframe.pack()
                a = Button(subframe, text=self.lista_de_botao[i], borderwidth=1, width=5, font=("bold", 10),
                           command=partial(botao, self.lista_de_botao[i]))
                a.pack(side=LEFT, pady=1.5, padx=1.5)

            restart = Button(subframe, text="sair", borderwidth=1, width=5, font=("bold", 10),
                             command=self.sair)
            restart.pack(side=LEFT, padx=1.5)

        def sair(self):
            janela.destroy()
            Menu()
            try:
                return self.inii[0]
            except:
                return self.score
        def music(self):
            if self.condmusic:
                self.condmusic = False
                winsound.PlaySound("300", winsound.SND_ASYNC | winsound.SND_PURGE)
            else:
                self.condmusic = True
                winsound.PlaySound("./storage/audios/TTD.wav",
                                   winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

        def forget(self):
            self.frame1.pack_forget()
            self.frame2.pack_forget()
            self.frame3.pack_forget()
            self.frame4.pack_forget()
            v = open("./storage/.int.txt", "w")
            v.write("%d#%d" % (self.score, self.dificuldade))
            v.close()
            teste = Forca(janela)

    janela = Tk()
    janela.wm_resizable(0, 0)
    janela.update_idletasks()
    width = janela.winfo_width()
    height = janela.winfo_height()
    g = 4
    x = (janela.winfo_screenwidth() // g) - (width // g)
    y = (janela.winfo_screenheight() // g) - (height // g)
    janela.geometry('{}x{}+{}+{}'.format(810, 400, int(x), int(y)))
    janela.configure(background="light gray")
    winsound.PlaySound("./storage/audios/TTD.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    janela.title("Forca")
    janela.iconbitmap("./storage/imagens/icon.ico")
    main = Forca(janela)
    janela.mainloop()
