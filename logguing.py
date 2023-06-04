import tkinter as tk
from libreriabd import server
from tkinter import messagebox

verificacion:bool
nombre:str
bd = server()
def iniciar():
     def registrarse():
        new_window = tk.Toplevel(root1)
        new_window.geometry("356x770")
        new_window.title("Nueva ventana")
   
        def botoneeliminar():
           pass
   
        def botonguardar():
           con=contrase.get()
           conc=contrasec.get()
           if(con==conc):
                 nom=nombre.get()
                 pas=contrase.get()
                 cor=email.get()
                 bd = server()
                 bd.Registrar(nom, pas, cor)
           else:
                 messagebox.showinfo("contraseña", "la contraseña no coincide porfavor revisar")
   
        def botonegresar():
            new_window.destroy()
   
        # Añadir imagen de fondo
        imagen = tk.PhotoImage(file="Images\legistro.png")
        tk.Label(new_window, image=imagen).place(x=0, y=0, relwidth=1, relheight=1)
   
   
   
   
   
        nombre = tk.Entry(new_window)
        nombre.place(y=290,x=30,height=38,width=300)
   
        email = tk.Entry(new_window)
        email.place(y=377,x=30,height=38,width=300)
   
        contrase = tk.Entry(new_window)
        contrase.place(y=460,x=30,height=38,width=300)

        contrasec = tk.Entry(new_window)
        contrasec.place(y=538,x=30,height=38,width=300)


        # Añadir botónes
        #------------------------ botones -----------------------   
   
        guardarimage = tk.PhotoImage(file="Images\guardarb.png")
        guardar = tk.Button(new_window, image=guardarimage, text="text",command=botonguardar)
        guardar.place(x=50, y=630,width=254,height=58)
        guardar.config(border=0)
        
   
        egresarimage = tk.PhotoImage(file="Images\egresarb.png")
        egresar = tk.Button(new_window, image=egresarimage, text="text",command=botonegresar)
        egresar.place(x=50, y=690,width=254,height=58)
        egresar.config(border=0)
   
   
   
        closeButton1 = Button(new_window, text="Cerrar", command=new_window.destroy)
        closeButton1.place(x=10, y=10)
        
     
     root1 = tk.Tk()
     root1.geometry("356x770")
     frut =1
     
     def boton1():
         global verificacion
         global bd
         global nombre
         identifica = bd.Iniciarsecion(input_box.get(),passwordg.get())
         if(identifica):
            verificacion=True
            nombre=input_box.get()
            root1.destroy()
         else:
            verificacion=False
            print("no")
     
     imagen = tk.PhotoImage(file="Images\inicio.png")
     tk.Label(root1, image=imagen).place(x=0, y=0, relwidth=1, relheight=1)
     
     
     text1 =tk.Label(root1)
     text1.place(x=565,y=380,height=20)
     
     input_box = tk.Entry(root1)
     input_box.place(y=290,x=28,height=38,width=300)
     
     passwordg = tk.Entry(root1)
     passwordg.place(x=28, y=370,height=38,width=300)
     
     image = tk.PhotoImage(file="Images\iniciob.png")
     iniciar = tk.Button(root1, image=image, text="text",command=boton1)
     iniciar.place(x=50, y=670,width=254,height=58)
     iniciar.config(border=0)
     iniciar.pack
     
     
     image1 = tk.PhotoImage(file="Images\egistrob.png")
     registrar = tk.Button(root1, image=image1, text="text",command=registrarse)
     registrar.place(x=50, y=570,width=254,height=58)
     registrar.config(border=0)
     registrar.pack
     
     #my_window.add_buttont(50,670, "iniciar seccion",boton1,254,58,"Images\iniciob.png")
     #my_window.add_buttont(50,570, "registrar",boton1,254,58,"Images\egistrob.png")
     
     
     
     root1.mainloop()
     if (verificacion):
        return nombre
     else:
        return False
