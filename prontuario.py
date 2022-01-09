import os
import webbrowser
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from textwrap import wrap



main_path = os.path.dirname(__file__)
space = '   '

janela = tix.Tk()
logo = PhotoImage(file=main_path+'\logor.png')


class Validacao:
    def null(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return value <=100000000000


class Relatorios(Event):
    def abrirPdf(self):
        self.id_p = self.cod_input.get()+"_paciente.pdf" 
        
        webbrowser.open(self.id_p)
    def geraRel(self):
        self.pacienteRel = canvas.Canvas(self.cod_input.get()+"_paciente.pdf")

        self.cpfRel = self.cod_input.get()        
        self.nomeRel = self.nome_input.get()   
        self.dataRel = self.data_input.get()   
        self.comoRel = self.comorbidades_input.get("1.0", "end-1c")   
        self.remRel = self.remedio_input.get("1.0", "end-1c")   
        self.alerRel = self.alergia_input.get("1.0", "end-1c")   
        self.sinRel = self.sinais_input.get()   
        self.evoRel = self.evolucao_input.get("1.0", "end-1c")   
        self.condRel = self.conduta_input.get("1.0", "end-1c")   
        self.recRel = self.receituario_input.get("1.0", "end-1c")
        
        self.pacienteRel.setFont("Helvetica-Bold", 24)
        self.pacienteRel.drawString(200, 790, 'Ficha do Paciente')

        self.pacienteRel.setFont("Helvetica-Bold", 14)
        self.pacienteRel.drawString(50, 700, 'CPF: ')
        self.pacienteRel.drawString(50, 670, 'Nome: ')
        self.pacienteRel.drawString(50, 640, 'Data de Nascimento: ')
        self.pacienteRel.drawString(50, 610, 'Comorbidades: ')
        self.pacienteRel.drawString(50, 580, 'Medicações de uso continúo: ')
        self.pacienteRel.drawString(50, 550, 'Alergia Medicamentosa: ')
        self.pacienteRel.drawString(50, 520, 'Sinais Vitais: ')
        self.pacienteRel.drawString(50, 490, 'Evolução Médica: ')
        self.pacienteRel.drawString(50, 400, 'Conduta: ')      
        self.pacienteRel.setFont("Helvetica-Bold", 8)
        self.pacienteRel.drawString(240, 60, 'Dr. Fabian Morais/CRM-PE 15 170')
        self.pacienteRel.drawString(150,45,'Rua Governador Dix Sept Rosado, Campo Grande, Recife - PE - CEP 52031010')
        self.pacienteRel.drawString(230, 250, 'Receituário Médico: ')
        

        self.pacienteRel.setFont("Helvetica", 11)
        self.pacienteRel.drawString(90, 701, self.cpfRel)
        self.pacienteRel.drawString(100, 670, self.nomeRel)
        self.pacienteRel.drawString(200, 640, self.dataRel)
        self.pacienteRel.drawString(160, 610, self.comoRel)
        self.pacienteRel.drawString(250, 580, self.remRel)
        self.pacienteRel.drawString(220, 550, self.alerRel)
        self.pacienteRel.drawString(150, 520, self.sinRel)
        self.pacienteRel.drawString(50, 470, self.evoRel)
        self.pacienteRel.drawString(50, 380, self.condRel)
        
        b = wrap(self.recRel, 90)
        print(b)
        text = self.pacienteRel.beginText(40, 200)
        for l in b:
            text.textLine(l)
        self.pacienteRel.drawText(text)

        self.pacienteRel.drawImage("logo.png",50,60,width=60, height=63, mask=[255,255,255])
        self.pacienteRel.rect(20, 30, 555, 270, fill= False, stroke=True)
        self.pacienteRel.line(220,70,400,70)

        self.pacienteRel.showPage()
        self.pacienteRel.save()
        self.abrirPdf()


class Funcoes():
    
    def limpar(self):

        self.cod_input.delete(0, END)
        self.nome_input.delete(0, END)
        self.data_input.delete(0, END)
        self.comorbidades_input.delete("1.0", END)
        self.remedio_input.delete("1.0", END)
        self.alergia_input.delete("1.0", END)
        self.sinais_input.delete(0, END)
        self.evolucao_input.delete("1.0", END)
        self.conduta_input.delete("1.0", END)
        self.receituario_input.delete("1.0", END)
        

    def conectarbd(self):
        self.conectar = sqlite3.connect("pacientes.db")
        self.cursor = self.conectar.cursor(); print("Conectando ao banco de dados")
    
    def desconectarbd(self):
        self.conectar.close(); print("Banco de dados desconectado")

    def criarPaciente(self):
        self.conectarbd()
        #criando tabelas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
                cpf INTERGER AUTO_INCREMENT PRIMARY KEY NOT NULL,
                nome_pacientes VARCHAR (40) NOT NULL,
                data_nascimento DATE,
                comorbidades VARCHAR (100),
                medicacoes VARCHAR (40),
                alergias VARCHAR (40),
                sinais VARCHAR (40),
                evolucao VARCHAR (300),
                conduta VARCHAR (200),
                receituario TEXT
            );
        """)

        self.conectar.commit(); print('Banco de dados criado')
        self.desconectarbd()

    def variaveis(self):
        self.cod_pac = self.cod_input.get()
        self.nome_pac = self.nome_input.get()
        self.data_pac = self.data_input.get()
        self.comorbidades_pac = self.comorbidades_input.get("1.0", "end-1c")
        self.remedio_pac = self.remedio_input.get("1.0", "end-1c")
        self.alergia_pac = self.alergia_input.get("1.0", "end-1c")
        self.sinais_pac = self.sinais_input.get()
        self.evolucao_pac = self.evolucao_input.get("1.0", "end-1c")
        self.conduta_pac = self.conduta_input.get("1.0", "end-1c")
        self.receituario_pac = self.receituario_input.get("1.0", "end-1c")

    def adicionar(self):
        
        self.variaveis()
        #condição de preenchimento do cpf e nome do paciente com mensagem de erro
        if self.nome_pac == "" or self.cod_pac == "":
            msg = "O cadastro de paciente só irá ser realizado\n"
            msg+= "com o preenchimento do campo nome e CPF."
            messagebox.showinfo("Erro de cadastro!", msg)
            
        else:
            self.parametros = (self.cod_pac, self.nome_pac, self.data_pac, self.comorbidades_pac, self.remedio_pac, self.alergia_pac, self.sinais_pac, self.evolucao_pac, self.conduta_pac, self.receituario_pac)

            self.conectarbd()
            self.cursor.execute(""" INSERT INTO pacientes (cpf, nome_pacientes, data_nascimento, comorbidades, medicacoes,  alergias, sinais, evolucao, conduta, receituario)            
                VALUES (?,?,?, ?, ?, ?, ?, ?, ?, ?)""", (self.parametros))
            self.conectar.commit()

            msg3 = "O cadastro de paciente foi adicionado."
            messagebox.showinfo("Cadastro!", msg3)

            self.desconectarbd()
            self.select_lista()
            self.limpar()

    def select_lista(self):
        self.lista_Clientes.delete(*self.lista_Clientes.get_children())
        self.conectarbd()

        lista = self.cursor.execute(""" SELECT cpf, nome_pacientes, data_nascimento, comorbidades, medicacoes, alergias, sinais, evolucao, conduta, receituario
                    FROM pacientes ORDER BY nome_pacientes ASC; """)
        
        for i in lista:
            self.lista_Clientes.insert("", END, values= i)
        
        self.desconectarbd()

    def duploclick(self, event):
        self.limpar()
        self.lista_Clientes.selection()
        for n in self.lista_Clientes.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = self.lista_Clientes.item(n, 'values')
            self.cod_input.insert(END, col1)
            self.nome_input.insert(END, col2)
            self.data_input.insert(END, col3)
            self.comorbidades_input.insert(END, col4)
            self.remedio_input.insert(END, col5)
            self.alergia_input.insert(END, col6)
            self.sinais_input.insert(END, col7)
            self.evolucao_input.insert(END, col8)
            self.conduta_input.insert(END, col9)
            self.receituario_input.insert(END, col10)

    def deletarpaciente(self):
        self.variaveis()
        self.conectarbd()
        self.cursor.execute(""" DELETE FROM pacientes WHERE cpf = ? """, [self.cod_pac])
        self.conectar.commit()
        msg1 = "O cadastro de paciente foi apagado."
        messagebox.showinfo("Cadastro", msg1)

        self.desconectarbd()
        self.limpar()
        self.select_lista()

    def alterarparciente(self):
        self.variaveis()
        self.conectarbd()

        self.cursor.execute(""" UPDATE pacientes SET nome_pacientes = ?,  data_nascimento = ?, comorbidades = ?, medicacoes= ?, alergias= ?, sinais= ?, evolucao= ?, conduta= ?, receituario= ?
            WHERE cpf=? """, (self.nome_pac, self.data_pac, self.comorbidades_pac, self.remedio_pac, self.alergia_pac, self.sinais_pac, self.evolucao_pac, self.conduta_pac, self.receituario_pac, self.cod_pac))

        self.conectar.commit()

        msg2 = "O cadastro do paciente foi alterado."
        messagebox.showinfo("Cadastro", msg2)

        self.desconectarbd()
        self.select_lista()
        self.limpar()

    def buscar(self):
        self.variaveis()
        self.conectarbd()
        self.lista_Clientes.delete(*self.lista_Clientes.get_children())

        self.nome_input.insert(END, '%')

        if self.nome_pac == "":
            msg4 = "Preencha o campo nome."
            messagebox.showinfo("Cadastro", msg4)

        else:
            nome = self.nome_input.get()
            self.cursor.execute(
                """ SELECT cpf, nome_pacientes, data_nascimento, comorbidades, medicacoes,  alergias, sinais, evolucao, conduta, receituario
                        FROM pacientes WHERE nome_pacientes LIKE '%s'  ORDER BY nome_pacientes ASC  """ % nome)
            
            buscarnome = self.cursor.fetchall()

            for i in buscarnome:
                self.lista_Clientes.insert("", END, values = i)
        
        self.limpar()
        
        self.desconectarbd()


class Prontuario(Funcoes, Relatorios, Validacao):

    def __init__(self):

        
        self.janela = janela
        self.validacpf()
        self.tela()
        self.frames()
        self.botoes()
        self.labels_frame1()
        self.labels_frame2()
        self.criarPaciente()
        self.select_lista()
        self.menus()

        
        


        janela.mainloop()

    def tela(self):

        self.janela.title(53*space+"Prontuário Eletrônico Consulta solidária")

        self.janela.configure(background= '#32CD32')

        self.janela.geometry("1280x720")

        self.janela.resizable(True, True)

        self.janela.maxsize(width= 1920, height= 1080)

        self.janela.minsize(width=550, height=380)
        
        self.janela.iconbitmap(main_path,'ico.ico')

    def frames(self):

        self.frame1 = Frame(self.janela, bd = 4, bg = '#F0F8FF',

                            highlightbackground= 'black', highlightthickness=4 )

        self.frame1.place(relx= 0.02 , rely=0.02, relwidth= 0.96,relheight= 0.45)



        self.frame2 = Frame(self.janela, bd=4, bg='#BEBEBE',

                            highlightbackground='black', highlightthickness=3)

        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)
    
    def botoes(self):
        #Buscar
        self.bt_buscar = Button(self.frame1, text= 'Buscar', bd= 3, bg= '#836FFF', fg= 'black'
                                ,font=('candara', 12, 'bold' ), command=self.buscar)
        self.bt_buscar.place(relx= 0.9, rely= 0.01, relwidth=0.1, relheight=0.15)
        
        #limpar
        self.bt_limpar = Button(self.frame1, text= 'Limpar', fg= 'black'
                                ,font=('candara', 12, 'bold' ), command= self.limpar)
        self.bt_limpar.place(relx= 0.9, rely= 0.2, relwidth=0.1, relheight=0.15)

        #alterar
        self.bt_alterar = Button(self.frame1, text= 'Alterar', bd=3, bg='#FFDEAD', fg= 'black'
                                ,font=('candara', 12, 'bold' ), command=self.alterarparciente)
        self.bt_alterar.place(relx= 0.9, rely= 0.4, relwidth=0.1, relheight=0.15)

        #apagar
        self.bt_apagar = Button(self.frame1, text= 'Apagar', bd=3, bg ='#A0522D', fg= 'black'
                                ,font=('candara', 12, 'bold' ), command=self.deletarpaciente)
        self.bt_apagar.place(relx= 0.9, rely= 0.6, relwidth=0.1, relheight=0.15)

        #adicionar
        self.bt_add = Button(self.frame1, text= 'Adicionar', bd=3, bg='#66CDAA', fg= 'black'
                                ,font=('candara', 12, 'bold' ), command=self.adicionar)
        self.bt_add.place(relx= 0.9, rely= 0.8, relwidth=0.1, relheight=0.15)
    
    def labels_frame1(self):

        #codigo_paciente
        self.cod_paciente = Label(self.frame1, text='CPF',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.cod_paciente.place(relx= 0.18, rely= 0.1)
        self.cod_input = Entry(self.frame1, validate="key", validatecommand=self.cpf_var)
        self.cod_input.place(relx= 0.07, rely= 0.1)
        
        #nome_paciente
        self.nome_paciente = Label(self.frame1, text='Nome',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.nome_paciente.place(relx= 0.18, rely= 0.2)
        self.nome_input = Entry(self.frame1)
        self.nome_input.place(relx= 0.07, rely= 0.2)

        #data de nascimento
        self.data_paciente = Label(self.frame1, text='Data de nascimento',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.data_paciente.place(relx= 0.18, rely= 0.3)
        self.data_input = Entry(self.frame1)
        self.data_input.place(relx= 0.07, rely= 0.3)

        #Comorbidades
        self.comorbidades_paciente = Label(self.frame1, text='Comorbidades',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.comorbidades_paciente.place(relx= 0.18, rely= 0.4)
        self.comorbidades_input = Text(self.frame1)
        self.comorbidades_input.place(relx= 0.07, rely= 0.4, relwidth=0.1, relheight=0.18)

        #medicações de uso continuo
        self.remedio_paciente = Label(self.frame1, text='Medicações de uso contínuo',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.remedio_paciente.place(relx= 0.18, rely= 0.6)
        self.remedio_input = Text(self.frame1)
        self.remedio_input.place(relx= 0.07, rely= 0.6, relwidth=0.1, relheight=0.18)

        #alergias
        self.alergia_paciente = Label(self.frame1, text='Alergia Medicamentosa',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.alergia_paciente.place(relx= 0.18, rely= 0.8)
        self.alergia_input = Text(self.frame1)
        self.alergia_input.place(relx= 0.07, rely= 0.8, relwidth=0.1, relheight=0.18)

        #sinais vitais
        self.sinais_paciente = Label(self.frame1, text='Sinais vitais',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.sinais_paciente.place(relx= 0.37, rely= 0.1)
        self.sinais_input = Entry(self.frame1)
        self.sinais_input.place(relx= 0.48, rely= 0.1, relwidth=0.168, relheight=0.08)

        #evolução médica
        self.evolucao_paciente = Label(self.frame1, text='Evolução Médica',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.evolucao_paciente.place(relx= 0.37, rely= 0.2)
        self.evolucao_input = Text(self.frame1)
        self.evolucao_input.place(relx= 0.48, rely= 0.2, relwidth=0.168, relheight=0.18)

        #conduta
        self.conduta_paciente = Label(self.frame1, text='Conduta',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.conduta_paciente.place(relx= 0.37, rely= 0.4)
        self.conduta_input = Text(self.frame1)
        self.conduta_input.place(relx= 0.48, rely= 0.4, relwidth=0.168, relheight=0.18)

        #Receituário médico
        self.receituario_paciente = Label(self.frame1, text='Receituário Médico',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.receituario_paciente.place(relx= 0.37, rely= 0.6)
        self.receituario_input = Text(self.frame1)
        self.receituario_input.place(relx= 0.48, rely= 0.6, relwidth=0.168, relheight=0.35)

        #Balões de mensagem
        self.ba_buscar = tix.Balloon(self.frame1)
        self.ba_buscar.bind_widget(self.bt_buscar, balloonmsg = "Clique para buscar pelo nome do paciente.")

        self.ba_limpar = tix.Balloon(self.frame1)
        self.ba_limpar.bind_widget(self.bt_limpar, balloonmsg = "Clique para preencher novamente o formulário.")

        self.ba_alterar = tix.Balloon(self.frame1)
        self.ba_alterar.bind_widget(self.bt_alterar, balloonmsg = "Clique para alterar os dados do paciente, CPF NÁO PODE SER ALTERADO!.")
        
        self.ba_apagar = tix.Balloon(self.frame1)
        self.ba_apagar.bind_widget(self.bt_apagar, balloonmsg = "Clique para apagar os dados do paciente.")

        self.ba_adicionar = tix.Balloon(self.frame1)
        self.ba_adicionar.bind_widget(self.bt_add, balloonmsg = "Preencha os dados do paciente e clique em adicionar.")

        
        #logo
        self.logo = Label(janela, image= logo, bg='#F0F8FF')
        self.logo.place(relx=0.64, rely= 0.075)
        
        #sobre
        self.sobre = Label(self.frame1, text='Idealizado por Joelma', fg= 'black', bg='#F0F8FF', font=('candara', 12 ,'bold'))
        self.sobre.place(relx= 0.69, rely= 0.8)

    def labels_frame2(self):
        self.lista_Clientes= ttk.Treeview(self.frame2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        #cabeçario
        self.lista_Clientes.heading('#0', text="COD")
        self.lista_Clientes.heading('#1', text="CPF")
        self.lista_Clientes.heading('#2', text="NOME")
        self.lista_Clientes.heading('#3', text="DATA DE NASCIMENTO")
        self.lista_Clientes.heading('#4', text="COMORBIDADES")

        #colunas
        self.lista_Clientes.column('#0', width=1)
        self.lista_Clientes.column('#1', width=200)
        self.lista_Clientes.column('#2', width=500)
        self.lista_Clientes.column('#3', width=125)
        self.lista_Clientes.column('#4', width=125)

        #criaçao
        self.lista_Clientes.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.85)

        #barra de rolagem
        self.barra_rolagem = Scrollbar(self.frame2, orient='vertical')
        self.lista_Clientes.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.place(relx= 0.96 , rely= 0.01, relwidth= 0.04, relheight= 0.85)
        self.lista_Clientes.bind("<Double-1>", self.duploclick)

    def menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        menu1 = Menu(menubar)
        menu2 = Menu(menubar) 

        def Quit(): self.janela.destroy()
        
        menubar.add_cascade(label="Opções", menu = menu1)
        menubar.add_cascade(label="Exportar", menu = menu2)

        menu1.add_command(label="Sair", command=Quit)
        menu2.add_command(label="Gerar relatório", command=self.geraRel)

    def validacpf(self):
        self.cpf_var = (self.janela.register(self.null), "%P")
    

Prontuario()