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
                mae = open("./storage/bin/config.txt", "r")
            except:
                mae = open("./storage/bin/config.txt", "w")
            nao = False
            mae.close()
            mae = open("./storage/bin/config.txt", "r")

            b = entrada1.get().upper()
            lista = mae.readlines()
            cont = 0
            for u in lista:
                linha = u.split('###')
                if Vegenere(linha[0]).decript() == b:
                    nao = True
                    break
                cont += 1
            if not nao:
                resultado["text"] = "Usuário não cadastrado!"
                resultado["fg"] = "red"
            else:
                b = entrada2.get().upper()
                if b != Vegenere(linha[1]).decript():
                    resultado["text"] = "Senha Incorreta!"
                else:
                    l.append(Vegenere(entrada1.get()).encript())
                    l.append(Vegenere(entrada2.get()).encript())
                    l.append(cont)
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
            resultado["text"] = "Digite um Login"
        elif entrada2.get() == "":
            resultado["text"] = "Digite uma senha"
        else:
            try:
                mae = open("./storage/bin/config.txt", "r")
            except:
                mae = open("./storage/bin/config.txt", "w")
            mae.close()
            mae = open("./storage/bin/config.txt", "r")
            linha = ''
            b = entrada1.get().upper()
            cadastro = True
            for i in mae.readlines():
                i = i.split("###")
                if b == Vegenere(i[0]).decript():
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
                mae = open("./storage/bin/config.txt", "a")
                linha += "%s###" % Vegenere(entrada1.get()).encript()
                linha += Vegenere(entrada2.get()).encript() + "###" + "0"
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
                entrada1.delete(0, "end")
                entrada2.delete(0, "end")
            except:
                pass

    def ms(x):
        def mss():
            if ent1 == "" and ent2 == "":
                mens["text"] = "Entrada invalida"
            l = ""
            with open("./storage/bin/config.txt", "r") as f:
                h = f.readlines()
            print(h)
            for i in h:
                print(i, Vegenere(ent0.get()).encript())
                if (Vegenere(ent0.get()).encript()) in i:
                    l = i
                    j = h.index(i)
                    break
            l = l.split("###")
            if ent1.get() != Vegenere(l[1]).decript():
                mens["text"] = "Senha incorreta"
            else:
                with open("./storage/bin/config.txt", "r") as f:
                    k = f.readlines()
                with open("./storage/bin/config.txt", "w") as f:
                    for i in k:
                        if k.index(i) == j:
                            g = ("%s###%s###%s" % (l[0], Vegenere(ent2.get()).encript(), l[-1]))
                            f.write("%s" % g)
                        else:
                            f.write(i)
            jan.destroy()
            Autentica()

        x.destroy()
        jan = Tk()
        jan.geometry('{}x{}+{}+{}'.format(270, 200, 466, 227))
        jan.title('Autenticação')
        texto0 = Label(jan, text="Login")
        ent0 = Entry(jan)
        texto1 = Label(jan, text="Senha antiga")
        ent1 = Entry(jan)
        texto2 = Label(jan, text="Nova senha")
        ent2 = Entry(jan)
        ok = Button(jan, text="alterar", command=mss)
        mens = Label(jan)
        texto0.pack()
        ent0.pack(pady=5)
        texto1.pack()
        ent1.pack(pady=5)
        texto2.pack()
        ent2.pack(pady=5)
        mens.pack()
        ok.pack()
        jan.mainloop()

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
    janela.geometry('{}x{}+{}+{}'.format(270, 200, int(x), int(y)))
    janela.title("Jogo da Forca")
    janela.iconbitmap("./storage/imagens/icon.ico")
    texto2 = Label(janela, text='Senha')
    entrada2 = Entry(janela, show="*")
    botao1 = Button(janela, text='Logar', command=partial(autenticar, "x"))
    janela.bind("<Return>", autenticar)
    botao2 = Button(janela, text='Cadastrar', command=cadastrar)
    change = Button(janela, text="Mudar senha", command=partial(ms, janela))
    resultado = Label(janela, text='')
    texto1.pack(anchor=CENTER)
    entrada1.pack(anchor=CENTER)
    texto2.pack(anchor=CENTER)
    entrada2.pack(anchor=CENTER)
    botao1.pack(anchor=CENTER, pady=5)
    botao2.pack(anchor=CENTER)
    resultado.pack(anchor=CENTER)
    change.pack(anchor=CENTER, side=BOTTOM)
    janela.mainloop()
    return l


class Vegenere(object):
    def __init__(self, pal):
        self.Alpha = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
                c = (y - z) + 36
                self.MenDescripto += self.Alpha[c % 36]
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
                self.MenCripto += self.Alpha[b % 36]
        return "%s" % self.MenCripto


def Forca_main():
    global score
    global a
    global mus2
    global dif

    class Forca(object):
        def __init__(self, master):
            self.condmusic = mus2
            master.protocol("WM_DELETE_WINDOW", self.sair)
            if self.condmusic:
                winsound.PlaySound("./storage/audios/TTD.wav", winsound.SND_FILENAME | winsound.SND_ASYNC |
                                   winsound.SND_LOOP)
            self.tentadas = []
            self.dificuldade = 3
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
            score = self.score
            self.falhas = 0
            self.resultados = []
            self.palavra = ''
            self.test = 0
            self.palavra_raw = ''
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
                global score
                global dif
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
                            self.score += len(self.palavra) * dif
                            self.scoreF["text"] = "Score:\n%d" % self.score
                            self.scoreF.pack()
                            cond = True
                    if not cond:
                        self.falhas += 1
                        if dif == 2 and self.falhas > 2:
                            self.dicas["text"] = Vegenere(self.dica).decript()
                        self.jogo["fg"] = "red"
                        faus = PhotoImage(file=("./storage/imagens/fim%d.png" % self.falhas))
                        # "GARBAGE COLLECTION DELETA A IMAGEM SE NAO DECLARAR O .IMAGE"
                        self.boneco.image = faus
                        self.boneco.update_idletasks()
                        self.boneco.configure(image=faus)
                        self.boneco.pack()
                        janela.update_idletasks()
                    self.jogo["text"] = self.resultados
                    if self.falhas == 6:
                        winsound.PlaySound("./storage/audios/Errou.wav",
                                           winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_PURGE)
                        messagebox.showinfo("Perdeu", "\nVOCÊ PERDEU!!!!!!!!!!            \n")
                        messagebox.showinfo("Perdeu", "A palavra secreta era:\n%s" % self.palavra_raw)
                        try:
                            self.score = self.inii[0]
                        except:
                            self.score = 0
                        if int(self.score) >= 100:
                            score = int(self.score) - 100
                        else:
                            score = self.score
                        v = open("./storage/.int.txt", "w")
                        v.close()
                        v = open("./storage/.int.txt", "a")
                        v.write("{}#{}".format(self.score, self.dificuldade))
                        v.close()
                        self.forget()
                if self.resultados.count("_") == 0:
                    if self.falhas == 0:
                        self.score += len(self.palavra) * 2
                    winsound.PlaySound("./storage/audios/acertou.wav", winsound.SND_FILENAME | winsound.SND_ASYNC |
                                       winsound.SND_PURGE)
                    messagebox.showinfo("Você achou o ovo", "Parabéns você acertou a palavra\n")
                    score = self.score
                    self.forget()

            framepd = Frame(self.frame3, bg="light gray")
            framepd.pack(pady=20)
            defal = PhotoImage(file="./storage/imagens/fim0.png")
            # defal = defal.subsample(2)
            self.boneco = Label(self.frame1, bg="light gray", image=defal)
            self.boneco.image = defal
            # self.boneco.configure(image=defal)
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

            self.dicas = Label(framepd, text="   ", width=30, height=1, bg="light gray",
                               font=("verdana", 16, "bold"))
            self.dicas.pack(pady=30)
            if dif == 1:
                self.dicas["text"] = Vegenere(self.dica).decript()
            self.lista_de_botao = list(string.ascii_uppercase)
            for i in range(len(self.lista_de_botao)):
                if i % 7 == 0:
                    subframe = Frame(self.frame4, bg="black")
                    subframe.pack()
                a = Button(subframe, text=self.lista_de_botao[i], borderwidth=1, width=5, font=("bold", 10),
                           command=partial(botao, self.lista_de_botao[i]))
                a.pack(side=LEFT, pady=1.5, padx=1.5)

            restart = Button(subframe, text="Voltar", borderwidth=1, width=8, font=("bold", 10),
                             command=self.sair)
            restart.pack(side=LEFT, padx=1.5)

        def sair(self):
            global score
            janela.destroy()
            with open("./storage/bin/config.txt", "r") as jonata:
                fe = jonata.readlines()
                for i in fe:
                    if a[2] == fe.index(i):
                        g = i
                        break
                g = g.split("###")
                if int(g[2]) > int(score):
                    score = int(g[2])

            g = "%s###%s###%s\n" % (a[0], a[1], score)
            with open("./storage/bin/config.txt", "r") as v:
                cad = v.readlines()
            with open("./storage/bin/config.txt", "w") as n:
                for i in cad:
                    if a[2] == cad.index(i):
                        n.write("%s" % g)
                    else:
                        n.write("%s" % i)
            Menu()

        def forget(self):
            self.frame1.pack_forget()
            self.frame2.pack_forget()
            self.frame3.pack_forget()
            self.frame4.pack_forget()
            v = open("./storage/.int.txt", "w")
            v.write("%s#%s" % (str(self.score), str(self.dificuldade)))
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
    if mus2:
        winsound.PlaySound("./storage/audios/TTD.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    else:
        winsound.PlaySound("300",
                           winsound.SND_ASYNC | winsound.SND_PURGE | winsound.SND_NOWAIT | winsound.SND_NODEFAULT)
    janela.title("Forca")
    janela.iconbitmap("./storage/imagens/icon.ico")
    main = Forca(janela)
    janela.mainloop()

    return score


def Score():
    Window3 = Tk()
    Window3.iconbitmap("./storage/imagens/icon.ico")
    Window3.title("Jogo da Forca")
    Window3["bg"] = "white"

    Lb3_1 = Label(Window3, text="Recordes")
    Lb3_1["bg"] = "white"
    Lb3_1.pack(anchor=CENTER)

    Bt3_1 = Button(Window3, text="Sair", command=lambda: Window3.destroy())
    Bt3_1["bg"] = "white"
    Bt3_1.pack(side=BOTTOM, anchor=CENTER)

    asd = open("./storage/bin/config.txt", "r")
    subframe = Frame(Window3)
    subframe.pack(side=RIGHT, ipady=65, anchor=CENTER)
    barra = Scrollbar(subframe)
    barra.pack(side=RIGHT, ipady=65)
    list1 = Listbox(subframe, yscrollcommand=barra.set, font=("verdana", 8, "bold"))
    list2 = Listbox(subframe, yscrollcommand=barra.set, font=("verdana", 8, "bold"))
    fa = asd.readlines()
    while True:
        cond = True
        for i in range(len(fa) - 1):
            le1 = fa[i + 1].split("###")
            le1 = int(le1[2][:-1])
            le2 = fa[i].split("###")
            le2 = int(le2[2][:-1])
            if le1 > le2:
                entry = fa[i + 1]
                del fa[i + 1]
                fa.insert(i, entry)
                cond = False
        if cond:
            break

    for i in fa:
        i = i.split("###")
        list1.insert(END, "%s" % (Vegenere(i[0]).decript()))
        list2.insert(END, "%s" % (i[2]))
    list1.pack(fill=BOTH, side=LEFT)
    list2.pack(fill=BOTH, side=RIGHT)
    barra.update_idletasks()
    barra.config(command=list1.yview)
    asd.close()
    Window3.update_idletasks()
    width = 300
    height = 220
    x = (Window3.winfo_screenwidth() // 2) - (width // 2)
    y = (Window3.winfo_screenheight() // 2) - (height // 2)
    Window3.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    Window3.resizable(False, False)
    Window3.mainloop()


class Config(object):
    def __init__(self):
        global mus1
        global mus2
        global a
        self.Window1 = Tk()
        self.Window1.iconbitmap("./storage/imagens/icon.ico")
        self.Window1.title("Jogo da Forca")
        self.Window1["bg"] = "white"
        self.frame_ch = Frame(self.Window1)
        self.frame_ch.pack(side=TOP, pady=10)
        self.ch11 = mus1
        self.ch21 = mus2
        self.botao()

    def Exit(self):
        self.Window1.destroy()

    def music1(self):
        global mus1
        self.ch11 = not self.ch11
        if not self.ch11:
            winsound.PlaySound("300", winsound.SND_ASYNC | winsound.SND_PURGE | winsound.SND_NOWAIT)
            mus1 = self.ch11
        else:
            winsound.PlaySound("./storage/audios/menu.wav",
                               winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            mus1 = self.ch11

    def music2(self):
        global mus2
        self.ch21 = not self.ch21
        if not self.ch21:
            mus2 = False
        else:
            mus2 = True

    def Reset(self):
        self.Window2 = Tk()
        self.Window2.iconbitmap("./storage/imagens/icon.ico")
        self.Window2.title("Jogo da Forca")
        self.Window2["bg"] = "white"

        def sim():
            self.Window2.destroy()
            with open("./storage/bin/config.txt", "r") as p:
                listt = p.readlines()
            with open("./storage/bin/config.txt", "w") as p:
                for i in range(len(listt)):
                    if i == a[2]:
                        s = ("%s###%s###0" % (a[0], a[1]))
                        p.write("%s\n" % s)
                    else:
                        p.write(listt[i])

        def Exit():
            self.Window2.destroy()

        Lb2_1 = Label(self.Window2, text="Deseja apagar todos os dados do jogo?")
        Lb2_1["bg"] = "white"
        Lb2_1.pack()

        subf_reset = Frame(self.Window2, bg="white")
        subf_reset.pack(pady=10)
        Bt2_1 = Button(subf_reset, text="Sim", width=10, command=sim)
        Bt2_1["bg"] = "white"
        Bt2_1.pack(side=LEFT)

        Bt2_2 = Button(subf_reset, text="Não", width=10, command=Exit)
        Bt2_2["bg"] = "white"
        Bt2_2.pack(side=RIGHT, padx=20)
        self.Window2.update_idletasks()
        width = 240
        height = 80
        x = (self.Window2.winfo_screenwidth() // 2) - (width // 2)
        y = (self.Window2.winfo_screenheight() // 2) - (height // 2)
        self.Window2.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.Window2.resizable(False, False)
        self.Window2.mainloop()

    def addp(self):
        def ad():
            a = "%s###%s" % (Vegenere(en1.get()).encript(), Vegenere(en2.get()).encript())
            cond = True
            with open("./storage/bin/palavras.txt", "r") as f:
                for i in f:
                    if a == i[:-1]:
                        cond = False
            if cond:
                with open("./storage/bin/palavras.txt", "a") as f:
                    f.write("%s\n" % a)
                self.Window2.destroy()

        self.Window2 = Tk()
        self.Window2.iconbitmap("./storage/imagens/icon.ico")
        self.Window2.title("Jogo da Forca")
        self.Window2["bg"] = "white"

        Lb2_1 = Label(self.Window2, text="Digite a palavra e a dica respectivamente:")
        Lb2_1.pack()

        subf_reset = Frame(self.Window2, bg="white")
        subf_reset.pack(pady=10)
        en1 = Entry(self.Window2)
        en1["bg"] = "white"
        en1.pack(pady=2.5)

        en2 = Entry(self.Window2)
        en2.pack(pady=2.5)

        self.b1 = Button(self.Window2, text="Ok", bg="white", command=ad)
        self.b1.pack()
        self.Window2.update_idletasks()
        width = 240
        height = 130
        x = (self.Window2.winfo_screenwidth() // 2) - (width // 2)
        y = (self.Window2.winfo_screenheight() // 2) - (height // 2)
        self.Window2.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.Window2.resizable(False, False)

        self.Window2.mainloop()

    def botao(self):
        self.CH1 = Checkbutton(self.frame_ch, text="Remover musica no jogo", state=ACTIVE, command=self.music2).pack()
        self.CH2 = Checkbutton(self.frame_ch, text="Remover musica no menu", state=ACTIVE, command=self.music1).pack()
        self.Bt1_1 = Button(self.Window1, text="Apagar Dados", command=self.Reset)
        self.Bt1_1["bg"] = "white"
        self.Bt1_1.pack()

        self.bt3 = Button(self.Window1, text="Adicionar Palavra", command=self.addp)
        self.bt3["bg"] = "white"
        self.bt3.pack()

        self.Bt2_1 = Button(self.Window1, text="Sair", command=self.Exit)
        self.Bt2_1["bg"] = "white"
        self.Bt2_1.pack(side=BOTTOM)

        self.Window1.update_idletasks()
        width = 200
        height = 180
        x = (self.Window1.winfo_screenwidth() // 2) - (width // 2)
        y = (self.Window1.winfo_screenheight() // 2) - (height // 2)
        self.Window1.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.Window1.resizable(False, False)
        self.Window1.mainloop()


def Creditos():
    creditos = Tk()
    creditos.iconbitmap("./storage/imagens/icon.ico")
    creditos.title("Créditos")
    width = 300
    height = 180
    x = (creditos.winfo_screenwidth() // 2) - (width // 2)
    y = (creditos.winfo_screenheight() // 2) - (height // 2)
    creditos.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    creditos.resizable(False, False)
    cred = Label(creditos,
                 text="Criadores e Desenvolvedores:\n   Talison Kennedy\n\n   José Henrique\n\n\n   Obrigado por Jogar",
                 font=("Verdana", 13, "bold"))
    cred.pack(anchor=CENTER)
    creditos.mainloop()


def inicializar(x):
    x.update_idletasks()
    x.destroy()
    global mus1
    global dif
    Window = Tk()
    Window.iconbitmap("./storage/imagens/icon.ico")
    Window.title("Forca do Fausto")
    back_ground = PhotoImage(file="./storage/imagens/back.png")
    background = Label(Window, image=back_ground)
    background.place(x=0, y=0)
    Window["bg"] = "white"

    def facil(x):
        global dif
        dif = 1
        Window.destroy()
        main = Forca_main()

    def medio(x):
        global dif
        dif = 2
        Window.destroy()
        main = Forca_main()

    def dificil(x):
        global dif
        dif = 3
        Window.destroy()
        main = Forca_main()

    def Voltar(x):
        x.update_idletasks()
        x.destroy()
        Menu()
    Bt1 = Button(Window, text="Fácil", command=partial(facil, Window))
    Bt1["bg"] = "white"
    Bt1.place(x=110, y=230, width=90)

    Bt2 = Button(Window, text="Médio", command=partial(medio, Window))
    Bt2["bg"] = "white"
    Bt2.place(x=230, y=230, width=90)

    Bt3 = Button(Window, text="Dificil", command=partial(dificil, Window))
    Bt3["bg"] = "white"
    Bt3.place(x=350, y=230, width=90)

    voltar = Button(Window, text="Voltar", command=partial(Voltar, Window))
    voltar["bg"] = "white"
    voltar.place(x=550, y=340, width=40)
    Window.update_idletasks()
    width = 600
    height = 400
    g = 2
    x = (Window.winfo_screenwidth() // g) - (width // g)
    y = (Window.winfo_screenheight() // g) - (height // g)
    Window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    Window.resizable(False, False)
    Window.mainloop()
    # main = Forca_main()


def Menu():
    global mus1
    Window = Tk()
    if mus1:
        winsound.PlaySound("./storage/audios/menu.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    else:
        winsound.PlaySound("300", winsound.SND_ASYNC | winsound.SND_PURGE | winsound.SND_NOWAIT)
    Window.iconbitmap("./storage/imagens/icon.ico")
    Window.title("Jogo da Forca")
    back_ground = PhotoImage(file="./storage/imagens/back.png")
    background = Label(Window, image=back_ground)
    background.place(x=0, y=0)
    Window["bg"] = "white"

    Bt1 = Button(Window, text="Iniciar jogo", command=partial(inicializar, Window))
    Bt1["bg"] = "white"
    Bt1.place(x=120, y=220, width=90)

    Bt2 = Button(Window, text="Pontuações", command=Score)
    Bt2["bg"] = "white"
    Bt2.place(x=260, y=220, width=90)

    Bt3 = Button(Window, text="Configurações", command=Config)
    Bt3["bg"] = "white"
    Bt3.place(x=120, y=280, width=90)

    Bt4 = Button(Window, text="Créditos", command=Creditos)
    Bt4["bg"] = "white"
    Bt4.place(x=260, y=280, width=90)

    Bt5 = Button(Window, text="Sair", command=lambda: Window.destroy())
    Bt5["bg"] = "white"
    Bt5.place(x=190, y=330, width=90)

    Window.update_idletasks()
    width = 600
    height = 400
    g = 2
    x = (Window.winfo_screenwidth() // g) - (width // g)
    y = (Window.winfo_screenheight() // g) - (height // g)
    Window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    Window.resizable(False, False)
    Window.mainloop()


dif = 1
mus1 = True
mus2 = True

score = 0
a = Autentica()
if len(a) == 3:
    Menu()
