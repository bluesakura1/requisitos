import tkinter as tk
from libreriabd import server
from libreriabd import calendaios
from tkinter import colorchooser
from tkinter import messagebox
from datetime import *
import calendar


def index(nomid):
   def open_window():
        new_window = tk.Toplevel(root)
        new_window.geometry("356x770")
        new_window.title("Nueva ventana")
   
        def botoneeliminar():
           pass
   
        def botonguardar():
           nom=nome.get()
           cor=core.get()
           pas=pase.get()
   
           print(nomid, nom, pas, cor)
           bd = server()
           bd.Editar_usuarios(nomid, nom, pas, cor)
   
        def botonegresar():
            new_window.destroy()
   
        # Añadir imagen de fondo
        imagen = tk.PhotoImage(file="Images\loguing.png")
        tk.Label(new_window, image=imagen).place(x=0, y=0, relwidth=1, relheight=1)
   
        bd = server()
        usurior = bd.Leer_usuario(nomid)
        print(usurior)
   
        tk.Label(new_window, text=usurior[0][1]).place(y=300,x=30,height=38,width=300)
        tk.Label(new_window, text=usurior[0][3]).place(y=410,x=30,height=38,width=300)
        tk.Label(new_window, text=usurior[0][2]).place(y=520,x=30,height=38,width=300)
        
        nome = tk.Entry(new_window)
        nome.place(y=350,x=30,height=38,width=300)
   
        core = tk.Entry(new_window)
        core.place(y=450,x=30,height=38,width=300)
   
        pase = tk.Entry(new_window)
        pase.place(y=570,x=30,height=38,width=300)
   
   
        
   
        # Añadir botónes
        #------------------------ botones ----------------------
        def eliminarp():
           bd = server()
           bd.eliminarperfil(nomid)
           root.destroy()

        eliminarimage = tk.PhotoImage(file="Images\eliminarb.png")
        eliminar = tk.Button(new_window, image=eliminarimage, text="X", command=eliminarp)
        eliminar.place(x=150, y=2, width=81, height=36)
        eliminar.config(border=0)
        eliminar.pack

        guardarimage = tk.PhotoImage(file="Images\guardarb.png")
        guardar = tk.Button(new_window, image=guardarimage, text="text",command=botonguardar)
        guardar.place(x=50, y=625,width=254,height=58)
        guardar.config(border=0)
        
   
        egresarimage = tk.PhotoImage(file="Images\egresarb.png")
        egresar = tk.Button(new_window, image=egresarimage, text="text" ,command=botonegresar)
        egresar.place(x=50, y=690,width=254,height=58)
        egresar.config(border=0)
   
   
   
        closeButton1 = Button(new_window, text="Cerrar", command=new_window.destroy)
        closeButton1.place(x=10, y=10)
   
   def recordatoriosf():
        new_window = tk.Toplevel(root)
        new_window.geometry("356x770")
        new_window.title("Nueva ventana")
        colores:str
        def botoneeliminar():
           nom=titulo.get()
           bd = server()
           bd.eliminarrecordatorio(nom)
   
        def botonguardar():
           colos = tk.colorchooser
           fin = colos.askcolor()
           col=fin[1]
           nom=titulo.get()
           fec=fecha.get()
           print(nom,col,fec)
   
           bd = server()
           bd.Crear_recordatorios(nom, fec, col)
        def botonegresar():
            new_window.destroy()
   
        def modificar():
           colos = tk.colorchooser
           fin = colos.askcolor()
           nom=titulo.get()
           newm=newtitulo.get()
           newfec=fecha.get()
           newcol=fin[1]
           bd = server()
           bd.Modificar_recordatorio(nom, newm, newfec, newcol)
   
   
        # Añadir imagen de fondo
        imagen = tk.PhotoImage(file="Images\ecordatorio.png")
        tk.Label(new_window, image=imagen).place(x=0, y=0, relwidth=1, relheight=1)
   
        newtitulo = tk.Entry(new_window)
        newtitulo.place(y=340,x=30,height=38,width=300)
   
   
        titulo = tk.Entry(new_window)
        titulo.place(y=440,x=30,height=38,width=300)
   
        fecha = tk.Entry(new_window)
        fecha.place(y=520,x=30,height=38,width=300)
   
        
        
   
        # Añadir botónes
        #------------------------ botones -----------------------
        deletebimage = tk.PhotoImage(file="Images\eliminarb.png")
        deleteb = tk.Button(new_window, image=deletebimage, text="text",command=botoneeliminar)
        deleteb.place(x=150, y=2,width=48,height=48)
        deleteb.config(border=0)
   
        userimage = tk.PhotoImage(file="Images\log.png")
        user = tk.Button(new_window, image=userimage, text="text",command=modificar)
        user.place(x=250, y=2,width=48,height=48)
        user.config(border=0)
   
   
   
        guardarimage = tk.PhotoImage(file="Images\guardarb.png")
        guardar = tk.Button(new_window, image=guardarimage, text="text",command=botonguardar)
        guardar.place(x=50, y=625,width=254,height=58)
        guardar.config(border=0)
        
   
        egresarimage = tk.PhotoImage(file="Images\egresarb.png")
        egresar = tk.Button(new_window, image=egresarimage, text="text",command=botonegresar)
        egresar.place(x=50, y=690,width=254,height=58)
        egresar.config(border=0)
   
   
   
        closeButton1 = Button(new_window, text="Cerrar", command=new_window.destroy)
        closeButton1.place(x=10, y=10)
   
   def metas():
        new_window = tk.Toplevel(root)
        new_window.geometry("356x770")
        new_window.title("Nueva ventana")
   
        def botoneeliminar():
           nom=titulo.get()
           bd = server()
           bd.eliminarmetas(nom)
   
        def botonguardar():
           colos = tk.colorchooser
           fin = colos.askcolor()
           col=fin[1]
           nom=titulo.get()
           fec=fecha.get()
           fecf=fechafinal.get()
   
           bd = server()
           bd.Crear_metas(nom, fec, fecf, col)
   
        def botonegresar():
            new_window.destroy()
   
        # Añadir imagen de fondo
        imagen = tk.PhotoImage(file="Images\metas.png")
        tk.Label(new_window, image=imagen).place(x=0, y=0, relwidth=1, relheight=1)
   
   
   
   
        titulo = tk.Entry(new_window)
        titulo.place(y=400,x=30,height=38,width=300)
   
        fecha = tk.Entry(new_window)
        fecha.place(y=480,x=30,height=38,width=300)
   
        fechafinal = tk.Entry(new_window)
        fechafinal.place(y=580,x=30,height=38,width=300)
   
        # Añadir botónes
        #------------------------ botones -----------------------
        userimage = tk.PhotoImage(file="Images\log.png")
        user = tk.Button(new_window, image=userimage, text="text",command=botoneeliminar)
        user.place(x=150, y=2,width=48,height=48)
        user.config(border=0)
   
   
        def aux():
           print(titulo.get())
   
   
        guardarimage = tk.PhotoImage(file="Images\guardarb.png")
        guardar = tk.Button(new_window, image=guardarimage, text="text",command=botonguardar)
        guardar.place(x=50, y=625,width=254,height=58)
        guardar.config(border=0)
        
   
        egresarimage = tk.PhotoImage(file="Images\egresarb.png")
        egresar = tk.Button(new_window, image=egresarimage, text="text",command=botonegresar)
        egresar.place(x=50, y=690,width=254,height=58)
        egresar.config(border=0)
   
   
   
        closeButton1 = Button(new_window, text="Cerrar", command=new_window.destroy)
        closeButton1.place(x=10, y=10)

   def metasm():
       new_window = tk.Toplevel(root)
       new_window.geometry("356x770")
       new_window.title("Nueva ventana")

       def botoneeliminar():
           nom = titulo.get()
           bd = server()
           bd.eliminarmetas(nom)

       def botonguardar():
           colos = tk.colorchooser
           fin = colos.askcolor()
           col = fin[1]
           nom = titulo.get()
           fec = fecha.get()
           fecf = fechafinal.get()

           bd = server()
           bd.Crear_metasm(nom, fec, fecf, col)

       def botonegresar():
           new_window.destroy()

       # Añadir imagen de fondo
       imagen = tk.PhotoImage(file="Images\metas.png")
       tk.Label(new_window, image=imagen).place(x=0, y=0, relwidth=1, relheight=1)

       titulo = tk.Entry(new_window)
       titulo.place(y=400, x=30, height=38, width=300)

       fecha = tk.Entry(new_window)
       fecha.place(y=480, x=30, height=38, width=300)

       fechafinal = tk.Entry(new_window)
       fechafinal.place(y=580, x=30, height=38, width=300)

       # Añadir botónes
       # ------------------------ botones -----------------------
       userimage = tk.PhotoImage(file="Images\log.png")
       user = tk.Button(new_window, image=userimage, text="text", command=botoneeliminar)
       user.place(x=150, y=2, width=48, height=48)
       user.config(border=0)

       def aux():
           print(titulo.get())

       guardarimage = tk.PhotoImage(file="Images\guardarb.png")
       guardar = tk.Button(new_window, image=guardarimage, text="text", command=botonguardar)
       guardar.place(x=50, y=625, width=254, height=58)
       guardar.config(border=0)

       egresarimage = tk.PhotoImage(file="Images\egresarb.png")
       egresar = tk.Button(new_window, image=egresarimage, text="text", command=botonegresar)
       egresar.place(x=50, y=690, width=254, height=58)
       egresar.config(border=0)

       closeButton1 = Button(new_window, text="Cerrar", command=new_window.destroy)
       closeButton1.place(x=10, y=10)
   def eventos():
        new_window = tk.Toplevel(root)
        new_window.geometry("356x770")
        new_window.title("Nueva ventana")
   
        def botoneeliminar():
           nom=titulo.get()
           bd = server()
           bd.eliminarevento(nom)
   
        def botonguardar():
           colos = tk.colorchooser
           fin = colos.askcolor()
           col=fin[1]
   
           nom=titulo.get()
           fec=fecha.get()
   
           bd = server()
           bd.Crear_eventos(nom, fec, col)
   
        def botonegresar():
            new_window.destroy()

        def modificarevento():
            bd = server()
            colos = tk.colorchooser
            fin = colos.askcolor()
            oldn = titulo.get()
            col = fin[1]
            fec = newfecha.get()
            nom = newtitulo.get()
            print(nomid,nom,fec,col)
            bd.Modificar_evento(oldn,nom,fec,col)

        # Añadir entradas
        imagen = tk.PhotoImage(file="Images\eventos.png")
        tk.Label(new_window, image=imagen).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(new_window, text="Titulo nuevo").place(y=102,x=30,height=38,width=300)
        tk.Label(new_window, text= "Fecha nueva").place(y=178,x=30,height=38,width=300)

        newtitulo = tk.Entry(new_window)
        newtitulo.place(y=140, x=30, height=38, width=300)

        newfecha = tk.Entry(new_window)
        newfecha.place(y=220, x=30, height=38, width=300)

        titulo = tk.Entry(new_window)
        titulo.place(y=440,x=30,height=38,width=300)
   
        fecha = tk.Entry(new_window)
        fecha.place(y=520,x=30,height=38,width=300)
   
   
   
        # Añadir botónes
        #------------------------ botones -----------------------
        userimage = tk.PhotoImage(file="Images\log.png")
        user = tk.Button(new_window, image=userimage, text="text",command=modificarevento)
        user.place(x=150, y=2,width=48,height=48)
        user.config(border=0)

        def aux():
           print(titulo.get())
   
   
        guardarimage = tk.PhotoImage(file="Images\guardarb.png")
        guardar = tk.Button(new_window, image=guardarimage, text="text",command=botonguardar)
        guardar.place(x=50, y=625,width=254,height=58)
        guardar.config(border=0)
        
   
        egresarimage = tk.PhotoImage(file="Images\egresarb.png")
        egresar = tk.Button(new_window, image=egresarimage, text="text",command=botonegresar)
        egresar.place(x=50, y=690,width=254,height=58)
        egresar.config(border=0)
   
   
   
        closeButton1 = Button(new_window, text="Cerrar", command=new_window.destroy)
        closeButton1.place(x=10, y=10)
   
   def presupuesto():
        new_window = tk.Toplevel(root)
        new_window.geometry("356x770")
        new_window.title("Nueva ventana")
   
        def botoneeliminar():
           pass
   
        def botonguardar():
           val=vala.get()
           fec=fechas.get()
           print(val,fec,nomid)
           bd = server()
           bd.Crear_presupuesto(nomid, val, fec)
   
        def botonegresar():
            new_window.destroy()
   
        # Añadir imagen de fondo
        imagen = tk.PhotoImage(file="Images\presupuesto.png")
        tk.Label(new_window, image=imagen).place(x=0, y=0, relwidth=1, relheight=1)
   
   
   
   
   
        vala = tk.Entry(new_window)
        vala.place(y=520,x=30,height=38,width=300)
   
        fechas = tk.Entry(new_window)
        fechas.place(y=580,x=30,height=38,width=300)
   
   
        # Añadir botónes
        #------------------------ botones -----------------------
        userimage = tk.PhotoImage(file="Images\log.png")
        user = tk.Button(new_window, image=userimage, text="text")
        user.place(x=150, y=2,width=48,height=48)
        user.config(border=0)
   
   
        def aux():
           print(titulo.get())
   
   
        guardarimage = tk.PhotoImage(file="Images\guardarb.png")
        guardar = tk.Button(new_window, image=guardarimage, text="text",command=botonguardar)
        guardar.place(x=50, y=625,width=254,height=58)
        guardar.config(border=0)
        
   
        egresarimage = tk.PhotoImage(file="Images\egresarb.png")
        egresar = tk.Button(new_window, image=egresarimage, text="text",command=botonegresar)
        egresar.place(x=50, y=690,width=254,height=58)
        egresar.config(border=0)
   
   
   
        closeButton1 = Button(new_window, text="Cerrar", command=new_window.destroy)
        closeButton1.place(x=10, y=10)
   
   def cerrars():
    root.destroy()
   
   
   
   
   root = tk.Tk()
   root.geometry("356x770")
   frut =1
   dias =[]
   navb = 0
   def findDay(date):
       born = datetime.strptime(date, '%d %m %Y').weekday()
       return (calendar.day_name[born])
   
   def diasy():
    x=1
    l=13
    while(x<l):
        if (x<10):
              date = '01 0'+str(x)+' 2023'
        else:
            date = '01 '+str(x)+' 2023'
        if (findDay(date) == "Monday"):
            dias.append(1)
            x=x+1
        if (findDay(date) == "Tuesday"):
            dias.append(2)
            x=x+1
        if (findDay(date) =="Wednesday"):
            dias.append(3)
            x=x+1
        if (findDay(date) =="Thursday"):
            dias.append(4)
            x=x+1
        if (findDay(date) =="Friday"):
            dias.append(5)
            x=x+1
        if (findDay(date) =="Saturday"):
            dias.append(6)
            x=x+1
        if (findDay(date) =="Sunday"):
            dias.append(7)
            x=x+1
        print(x)
                
   print((int(datetime.today().strftime('%m')))==5)
   diasy()
        
        
        
   n =31
   k = dias[(int(datetime.today().strftime('%m')))-1]
        
   def calendarioright():
     global k
     global navb
     try:
          navb = navb+1
          k = dias[((int(datetime.today().strftime('%m')))-1)+navb]
          loca.mes(100, 100, k, n)
     except:
        print("NO")
   
   
   def calendarioleft():
     global k
     global navb
     try:
          navb = navb-1
          k = dias[((int(datetime.today().strftime('%m')))-1)+navb]
          loca.mes(100, 100, k, n)
     except:
        print("NO")
   
   
   #-----------root = tk.Tk()---------------------------------------
   mesactual = datetime.today().strftime('%m/%Y')
   fecha_actual = datetime.today().strftime('%d/%m/%Y')
   
   mensajer="recordatorios del mes: "
   mensajev="eventos del dia: "
   mensajem="metas del mes: "
   mensajemm = "METAS MEDICAS DEL MES: "

   bdroot = server()
   recordatorios = bdroot.leer_registros("recordatorio")
   metass = bdroot.leer_registros("meta")
   metassm = bdroot.leer_registros("metasm")

   eventoss = bdroot.leer_registros("evento")
   
   for recordatorio in recordatorios:
       if(mesactual in (recordatorio[2])):
          mensajer = mensajer+str(recordatorio)+"\n"
   
   for meta in metass:
       if(mesactual in (meta[3])):
          mensajem = mensajem+str(meta)+"\n"

   for metam in metassm:
       if (mesactual in (metam[3])):
           mensajemm = mensajemm + str(metam) + "\n"

   for evento in eventoss:
       if(fecha_actual in (evento[2])):
          mensajev=mensajev+str(evento)+"\n"
   
   
   messagebox.showinfo("recordatorios", mensajer)
   messagebox.showinfo("eventos", mensajev)
   messagebox.showinfo("metas", mensajem)
   messagebox.showinfo("metasm", mensajemm)

   #---------
   bg_image = tk.PhotoImage(file="Images\index.png")
   tk.Label(root, image=bg_image).place(x=0, y=0)
   
   
   userimage = tk.PhotoImage(file="Images\log.png")
   user = tk.Button(root, image=userimage, text="text",command=open_window)
   user.place(x=150, y=2,width=48,height=48)
   user.config(border=0)
   user.pack




   
   presupuestoimage = tk.PhotoImage(file="Images\presupuestob.png")
   presupuesto = tk.Button(root, image=presupuestoimage, text="text",command=presupuesto)
   presupuesto.place(x=50, y=422,width=254,height=58)
   presupuesto.config(border=0)
   presupuesto.pack
   
   recordatoriosimage = tk.PhotoImage(file="Images\ecordatoriosb.png")
   recordatorios = tk.Button(root, image=recordatoriosimage, text="text",command=recordatoriosf)
   recordatorios.place(x=50, y=484,width=254,height=58)
   recordatorios.config(border=0)
   recordatorios.pack
   
   metasimage = tk.PhotoImage(file="Images\metasb.png")
   metas = tk.Button(root, image=metasimage, text="text",command=metas)
   metas.place(x=50, y=608,width=254,height=58)
   metas.config(border=0)
   metas.pack
   
   eventoimage = tk.PhotoImage(file="Images\eventosb.png")
   evento = tk.Button(root, image=eventoimage, text="text",command=eventos)
   evento.place(x=50, y=546,width=254,height=58)
   evento.config(border=0)
   evento.pack
   

   mes = tk.Button(root, text="medicas",command=metasm)
   mes.place(x=50, y=670,width=254,height=58)
   mes.config(border=0)
   mes.pack
   loca = calendaios(root)
   
   loca.mes(20, 100, k, n)
   root.mainloop()