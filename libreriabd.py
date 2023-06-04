import pymysql
import tkinter as tk
from tkinter import *
from tkcalendar import *



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
class server:

    def __init__(self):
        pass

    def Registrar(self,nom,pas,cor):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="micanal456",
            db="calendario"
        )
        cursor = connection.cursor()
        sql="INSERT INTO usuario(usuario,contraseña,correo) VALUES('"+nom+"','"+pas+"','"+cor+"')"
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()
    
    
    def Iniciarsecion(self,nom,pas):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="micanal456",
            db="calendario"
        )
        cursor = connection.cursor()
        try:
            print(nom,"nom input")
            resultadon = self.buscar_elemento('usuario', 'usuario',nom)
            print(resultadon[0][1]+"nom")
            print(resultadon[0][2]+"pas")
            if ((nom in (resultadon[0][1])) and (pas in (resultadon[0][2]))):
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
                print("onombre o contraseña")
        except:
            cursor.close()
            connection.close()
            print("ninguno ecexcion")
            return False
    
    
    
    def Editar_usuarios(self,nomid,nom,pas,cor):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="micanal456",
            db="calendario"
        )
        cursor = connection.cursor()
        try:
            objeto = self.buscar_elemento('usuario', 'usuario', nomid)
            Id = objeto[0][0]
            sql = "UPDATE `calendario`.`usuario` SET `usuario` = '" + nom + "', `contraseña` = '" + pas + "', `correo` = '" + cor + "' WHERE(`Id` = '" +str(Id)+ "');"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except:
            cursor.close()
            connection.close()
            return False
    
    
    def Crear_recordatorios(self,nom,fec,col):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="micanal456",
            db="calendario"
        )
        cursor = connection.cursor()
        try:
            sql="INSERT INTO `calendario`.`recordatorio` (`nombre`, `fecha-final`, `color`) VALUES ('"+nom+"', '"+fec+"', '"+col+"')"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except:
            cursor.close()
            connection.close()
            return False
    
    def Crear_metas(self,nom,fec,fecf,col):
         connection = pymysql.connect(
             host="localhost",
             user="root",
             password="micanal456",
             db="calendario"
         )
         cursor = connection.cursor()
         try:
             sql="INSERT INTO `calendario`.`meta` (`nombre`, `fecha-inicio`, `fecha-final`, `color`) VALUES ('"+nom+"', '"+fec+"', '"+fecf+"', '"+col+"');"
             cursor.execute(sql)
             connection.commit()
             cursor.close()
             connection.close()
             return True
         except:
             cursor.close()
             connection.close()
             return False

    def Crear_metasm(self,nom,fec,fecf,col):
         connection = pymysql.connect(
             host="localhost",
             user="root",
             password="micanal456",
             db="calendario"
         )
         cursor = connection.cursor()
         try:
             sql="INSERT INTO `calendario`.`metasm` (`titulo`, `fechainicio`, `fechafinal`, `color`) VALUES ('"+nom+"', '"+fec+"', '"+fecf+"', '"+col+"');"
             cursor.execute(sql)
             connection.commit()
             cursor.close()
             connection.close()
             return True
         except:
             cursor.close()
             connection.close()
             return False

    def Crear_eventos(self,nom,fec,col):
         connection = pymysql.connect(
             host="localhost",
             user="root",
             password="micanal456",
             db="calendario"
         )
         cursor = connection.cursor()
         try:
             sql="INSERT INTO `calendario`.`evento` (`nombre`, `fecha`, `color`) VALUES ('"+nom+"', '"+fec+"', '"+col+"');"
             cursor.execute(sql)
             connection.commit()
             cursor.close()
             connection.close()
             return True
         except:
             cursor.close()
             connection.close()
             return False

    def Crear_presupuesto(self,nomid,val,fec):
         connection = pymysql.connect(
             host="localhost",
             user="root",
             password="micanal456",
             db="calendario"
         )
         cursor = connection.cursor()
         objeto = self.buscar_elemento('usuario', 'usuario', nomid)
         Ids = objeto[0][0]

         try:
             sql="UPDATE `calendario`.`usuario` SET `presupuesto` = '"+val+"', `fechalimite` = '"+fec+"' WHERE (`id` = '"+str(Ids)+"');"
             cursor.execute(sql)
             connection.commit()
             cursor.close()
             connection.close()
             return True
         except:
             cursor.close()
             connection.close()
             print("fail 2")
             return False

    
    
    def Modificar_presupuesto(self,nomid,pre,fec):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="micanal456",
            db="calendario"
        )
        cursor = connection.cursor()
        try:
            objeto = self.buscar_elemento('usuario', 'usuario', nomid)
            Id = objeto[0][0]
            sql = "UPDATE `calendario`.`usuario` SET `presupuesto` = '" + pre + "', `fechalimite` = '" + fec + "' WHERE(`Id` = '" + str(Id) + "');"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except:
            cursor.close()
            connection.close()
            return False

    def Modificar_meta(self,nomid,newm,newfec,newcol,newfecf):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="micanal456",
            db="calendario"
        )
        cursor = connection.cursor()
        try:
            objeto = self.buscar_elemento('meta', 'nombre', nomid)
            Id = objeto[0][0]
            sql = "UPDATE `calendario`.`meta` SET `nombre` = '"+newm+"', `fecha-inicio` = '"+newfec+"', `fecha-final` = '"+newfecf+"', `color` = '"+newcol+"' WHERE (`id` = '"+str(Id)+"');"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except:
            cursor.close()
            connection.close()
            return False

    def Modificar_recordatorio(self,nomid,newm,newfec,newcol):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="micanal456",
            db="calendario"
        )
        cursor = connection.cursor()
        try:
            objeto = self.buscar_elemento('recordatorio', 'nombre', nomid)
            Id = objeto[0][0]
            sql = "UPDATE `calendario`.`recordatorio` SET `nombre` = '"+newm+"', `fecha-final` = '"+newfec+"', `color` = '"+newcol+"' WHERE (`id` = '"+str(Id)+"');"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except:
            cursor.close()
            connection.close()
            return False


    def Modificar_evento(self,nomid,newm,newfec,newcol):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="micanal456",
            db="calendario"
        )
        cursor = connection.cursor()
        try:
            objeto = self.buscar_elemento('evento', 'nombre', nomid)
            Id = objeto[0][0]
            sql = "UPDATE `calendario`.`evento` SET `nombre` = '"+newm+"', `fecha` = '"+newfec+"', `color` = '"+newcol+"' WHERE (`id` = '"+str(Id)+"');"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except:
            cursor.close()
            connection.close()
            return False


    def leer_registros(self,tablas):
        conexion = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="micanal456",
                    db="calendario")
        
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM "+tablas+"")
        
        registros = cursor.fetchall()
        
        return registros

    def eliminarperfil(self,nomid):
         connection = pymysql.connect(
             host="localhost",
             user="root",
             password="micanal456",
             db="calendario"
         )
         cursor = connection.cursor()
         objeto = self.buscar_elemento('usuario', 'usuario', nomid)
         Ids = objeto[0][0]

         try:
             sql="DELETE FROM `calendario`.`usuario` WHERE (`id` = '"+str(Ids)+"');"
             cursor.execute(sql)
             connection.commit()
             cursor.close()
             connection.close()
             return True
         except:
             cursor.close()
             connection.close()
             print("fail delete")
             return False


    def eliminarrecordatorio(self,nomid):
         connection = pymysql.connect(
             host="localhost",
             user="root",
             password="micanal456",
             db="calendario"
         )
         cursor = connection.cursor()
         objeto = self.buscar_elemento('recordatorio', 'nombre', nomid)
         Ids = objeto[0][0]

         try:
             sql="DELETE FROM `calendario`.`recordatorio` WHERE (`id` = '"+str(Ids)+"');"
             cursor.execute(sql)
             connection.commit()
             cursor.close()
             connection.close()
             return True
         except:
             cursor.close()
             connection.close()
             print("fail 2lete")
             return False


    def eliminarevento(self,nomid):
         connection = pymysql.connect(
             host="localhost",
             user="root",
             password="micanal456",
             db="calendario"
         )
         cursor = connection.cursor()
         objeto = self.buscar_elemento('evento', 'nombre', nomid)
         Ids = objeto[0][0]

         try:
             sql="DELETE FROM `calendario`.`evento` WHERE (`id` = '"+str(Ids)+"');"
             cursor.execute(sql)
             connection.commit()
             cursor.close()
             connection.close()
             return True
         except:
             cursor.close()
             connection.close()
             print("fail 2lete")
             return False


    def eliminarmetas(self,nomid):
         connection = pymysql.connect(
             host="localhost",
             user="root",
             password="micanal456",
             db="calendario"
         )
         cursor = connection.cursor()
         objeto = self.buscar_elemento('meta', 'nombre', nomid)
         Ids = objeto[0][0]

         try:
             sql="DELETE FROM `calendario`.`meta` WHERE (`id` = '"+str(Ids)+"');"
             cursor.execute(sql)
             connection.commit()
             cursor.close()
             connection.close()
             return True
         except:
             cursor.close()
             connection.close()
             print("fail 2lete")
             return False

    
    def Leer_usuario(self,nom):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="micanal456",
            db="calendario"
        )
        cursor = connection.cursor()
        resultados = self.buscar_elemento('usuario', 'usuario', nom)
        connection.commit()
        cursor.close()
        connection.close()
        return resultados
    
    def Leer_recordatorio(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="micanal456",
            db="calendario"
        )
        cursor = connection.cursor()
        consulta = "SELECT * FROM calendario.recordatorio"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        cursor.close()
        connection.close()
        return resultados
    
    def buscar_elemento(self,tabla, columna, valor_buscado):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="micanal456",
            db="calendario"
        )
        cursor = connection.cursor()
        consulta = "SELECT * FROM " + tabla + " WHERE " + columna + " = %s"
        datos = valor_buscado
        cursor.execute(consulta, datos)
        resultados = cursor.fetchall()
        cursor.close()
        connection.close()
        return resultados

class calendaios(tk.Tk):
    def __init__ (self,win):
     self.win = win
     self.dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
     self.acaba = 0
    def mes(self,x,y,k,n):
     id_boton = 1
     
     # Crear el frame para los botones
     botones_frame = tk.Frame(self.win)
     botones_frame.grid(row=0, column=0)

     # Crear etiquetas para los días de la semana
     for i, dia in enumerate(self.dias_semana):
         etiqueta = tk.Label(botones_frame, text=dia)
         etiqueta.grid(row=0, column=i)


     # Crear botones para cada día del calendario


     for fila in range(1, 7):
          for columna in range(7):
               if fila == 1:
                   if columna >= k-1 and id_boton <= n:
                        boton = tk.Button(botones_frame, text=str(id_boton), width=4, height=2)
                        boton.grid(row=fila, column=columna)
                        id_boton += 1
                   else:
                        boton = tk.Button(botones_frame, text='', width=4, height=2, disabledforeground='grey')
                        boton.grid(row=fila, column=columna)
               else:
                   if  id_boton <= n:
                        boton = tk.Button(botones_frame, text=str(id_boton), width=4, height=2)
                        boton.grid(row=fila, column=columna)
                        id_boton += 1
                        
                   else:
                        if(fila == 5):
                            self.acaba = self.acaba+1
                            print(self.acaba,"-------- self acaba1")
                            boton = tk.Button(botones_frame, text='.', width=4, height=2, disabledforeground='grey')
                            boton.grid(row=fila, column=columna)
                        else:
                              boton = tk.Button(botones_frame, text='', width=4, height=2, disabledforeground='grey')
                              boton.grid(row=fila, column=columna)

     botones_frame.place(x=x,y=y)

class Window:
     def __init__(self, src,ventana):
          self.window = ventana 
          self.window.geometry("356x770")
          self.window.title("My Window")
          self.add_background(src)

     def add_background(self, src):
          self.background_image = PhotoImage(file=src)
          self.background_label = Label(self.window, image=self.background_image)
          self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


     def add_button(self, x, y, text,comand,w,h):

        if(comand!=None):

             button = Button(self.window, text=text,command=comand)

             button.place(x=x, y=y,width=w,height=h)
             button.pack()


     def add_input(self, x, y):
          input_box = Entry(self.window)
          input_box.place(x=x, y=y,width=267,height=38)
          return(input_box.get())
          





# Crear ventana principal
#ventana = tk.Tk()
#ventana.title('Calendario')
#loca = calendaios(ventana)
#loca.mes(100, 100, 3, 31)
#loca.mes(100, 500, 3, 28)
#ventana.mainloop()


#print(Crear_recordatorios("ginacio","03/06/2004","#012845E"))
#print(Modificar_presupuesto("luis","012","03/06/2005"))
#print(Leer_usuario("luis"))
#print(Leer_recordatorio())