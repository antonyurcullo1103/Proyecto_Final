import io
from msilib.schema import ComboBox
import os
import openpyxl
import pandas as pd
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

#Dando la Interfaz a la variable root
root = Tk()
root.title("Sistema de Gestion de Imagenes")
root.geometry("1360x720")

#Dando el Treeview a la variable my_tree y colocando en la Intefaz
my_tree = ttk.Treeview(root)
nombreSistema = "Sistema de Gestion de Imagenes"


#FUNCIONES
##Funcion para
def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

##Funcion mostrar combobox seleccionado
def selection_changed(event):
    selection = ComboboxCategoria.get()
    file_openbox(selection)
   
##Funcion file_open(excel) desde el combobox
def file_openbox(seleccion):
   
    if seleccion:
        try:
            filename = ('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(seleccion))+'.metadata.xlsx')
            df = pd.read_excel(filename, engine='openpyxl')
        except ValueError:
            messagebox.showinfo("Alerta","Archivo no puede ser abierto... intenta de nuevo")
        except FileNotFoundError:
            messagebox.showinfo("Alerta","Archivo no encontrado...intenta de nuevo")
    #limpiar antiguo treeview(dataframe)
    clear_tree()
    #Establecer nuevo treeview(dataframe)
    my_tree['column'] = list(df.columns)
    my_tree['show'] = 'headings'
    #loop thru column list
    for column in my_tree['column']:
        my_tree.heading(column,text=column)

    #Colocar datos en treeview
    df_rows = df.to_numpy().tolist()
    for row in reverse(df_rows):
        my_tree.insert('','end', values=row)
    #Dando ubicacion al treeview
    my_tree.grid(row=1, column=5)

##Funcion limpiar filas del treeview
def clear_tree():
    my_tree.delete(*my_tree.get_children())

##Funcion agregar registro al excel desde el BOTON
def agregarRegistro():
    categoria= ComboboxCategoria.get()
    wb=openpyxl.load_workbook(('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(categoria))+'.metadata.xlsx'))
    ws = wb['Sheet1']
 
    File_Name = str(entryFile_Name.get())
    Format = str(entryFormat.get())
    Size = str(entrySize.get())
    Url = str(entryUrl.get())
    if File_Name == "" or Format == " ":
        messagebox.showinfo("Error", "Inserte File_Name!")
    if Format == "" or Format == " ":     
        messagebox.showinfo("Error", "Inserte Format!")
    if Size == "" or Size == " ":
        messagebox.showinfo("Error", "Inserte Size!")
    if Url == "" or Url == " ":
        messagebox.showinfo("Error", "Inserte Url!")
    else:
       #Revisa si existe registro por FILE NAME
        for i in range(2,(ws.max_row)+1):
            if File_Name==ws['A'+str(i)].value:
                Found=True
                break

            else:
                Found = False

        if(Found==True):
            messagebox.showinfo("Error", "File Name ya Existe!")
                    
        else:
            lastRow=str((ws.max_row)+1)
            ws['A'+lastRow]=File_Name
            ws['B'+lastRow]=Format
            ws['C'+lastRow]=Size
            ws['D'+lastRow]=Url
            #guardar imagen en el dataset
            guardar_imagen(File_Name,categoria)

        wb.save(('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(categoria))+'.metadata.xlsx'))
        messagebox.showinfo("Alerta", "Datos Modificados Exitosamente!")
    #limpiar antiguo treeview(dataframe)
    clear_tree()
    #Establecer nuevo treeview(dataframe)
    filename = ('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(categoria))+'.metadata.xlsx')
    df = pd.read_excel(filename, engine='openpyxl')
    my_tree['column'] = list(df.columns)
    my_tree['show'] = 'headings'
    #loop thru column list
    for column in my_tree['column']:
        my_tree.heading(column,text=column)

    #Colocar datos en treeview
    df_rows = df.to_numpy().tolist()
    for row in reverse(df_rows):
        my_tree.insert('','end', values=row)
    #pack(enpaquetar) the treeview finally
    my_tree.grid(row=1, column=5)

##Funcion editar registro del excel desde el BOTON
def editarRegistro():
    categoria= ComboboxCategoria.get()
    wb=openpyxl.load_workbook(('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(categoria))+'.metadata.xlsx'))
    ws = wb['Sheet1']
 
    File_Name = str(entryFile_Name.get())
    Format = str(entryFormat.get())
    Size = str(entrySize.get())
    Url = str(entryUrl.get())
    if File_Name == "" or Format == " ":
        messagebox.showinfo("Error", "Inserte File_Name!")
    if Format == "" or Format == " ":     
        messagebox.showinfo("Error", "Inserte Format!")
    if Size == "" or Size == " ":
        messagebox.showinfo("Error", "Inserte Size!")
    if Url == "" or Url == " ":
        messagebox.showinfo("Error", "Inserte Url!")
    else:
       #Revisa si existe registro por FILE NAME
        for i in range(2,(ws.max_row)+1):
            if File_Name==ws['A'+str(i)].value:
                Found = False
                ws['A'+str(i)]=File_Name
                ws['B'+str(i)]=Format
                ws['C'+str(i)]=Size
                ws['D'+str(i)]=Url
                messagebox.showinfo("Alerta", "Datos Modificados Exitosamente!")
                #guardar imagen en el dataset
                guardar_imagen(File_Name,categoria)
                break

            else:   
               
                Found=True
               
        if(Found==True):
            messagebox.showinfo("Error", "File Name no Existe!")


        wb.save(('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(categoria))+'.metadata.xlsx'))
    #limpiar antiguo treeview(dataframe)
    clear_tree()
    #Establecer nuevo treeview(dataframe)
    filename = ('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(categoria))+'.metadata.xlsx')
    df = pd.read_excel(filename, engine='openpyxl')
    my_tree['column'] = list(df.columns)
    my_tree['show'] = 'headings'
    #loop thru column list
    for column in my_tree['column']:
        my_tree.heading(column,text=column)

    #Colocar datos en treeview
    df_rows = df.to_numpy().tolist()
    for row in reverse(df_rows):
        my_tree.insert('','end', values=row)
    #pack(enpaquetar) the treeview finally
    my_tree.grid(row=1, column=5)


##Funcion eliminar registro del excel desde el BOTON
def eliminarRegistro():
    categoria= ComboboxCategoria.get()
    wb=openpyxl.load_workbook(('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(categoria))+'.metadata.xlsx'))
    ws = wb['Sheet1']
 
    File_Name = str(entryFile_Name.get())
    Format = str(entryFormat.get())
    Size = str(entrySize.get())
    Url = str(entryUrl.get())
    if File_Name == "" or Format == " ":
        messagebox.showinfo("Error", "Inserte File_Name!")
    if Format == "" or Format == " ":     
        messagebox.showinfo("Error", "Inserte Format!")
    if Size == "" or Size == " ":
        messagebox.showinfo("Error", "Inserte Size!")
    if Url == "" or Url == " ":
        messagebox.showinfo("Error", "Inserte Url!")
    else:
       #Revisa si existe registro por FILE NAME
        for i in range(2,(ws.max_row)+1):
            if File_Name==ws['A'+str(i)].value:
                Found = False
                if messagebox.askyesno('Alerta','Estas seguro que deseas eliminar el registo?'):
                    ws.delete_rows(i, 1)
                    eliminar_imagen(File_Name,categoria)
                    break
                break

            else:   
               
                Found=True
               

        if(Found==True):
            messagebox.showinfo("Error", "File Name no Existe!")
                    
        # else:
        #     lastRow=str((ws.max_row)+1)
        #     ws['A'+lastRow]=File_Name
        #     ws['B'+lastRow]=Format
        #     ws['C'+lastRow]=Size
        #     ws['D'+lastRow]=Url

        wb.save(('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(categoria))+'.metadata.xlsx'))

    #limpiar antiguo treeview(dataframe)
    clear_tree()
    #Establecer nuevo treeview(dataframe)
    filename = ('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(categoria))+'.metadata.xlsx')
    df = pd.read_excel(filename, engine='openpyxl')
    my_tree['column'] = list(df.columns)
    my_tree['show'] = 'headings'
    #loop thru column list
    for column in my_tree['column']:
        my_tree.heading(column,text=column)

    #Colocar datos en treeview
    df_rows = df.to_numpy().tolist()
    for row in reverse(df_rows):
        my_tree.insert('','end', values=row)
    #pack(enpaquetar) the treeview finally
    my_tree.grid(row=1, column=5)

##Funcion cambiar imagen en la interfaz
def cambiar_Imagen():
    global redimensionado
    archivo = filedialog.askopenfilename(title="abrir", filetypes=[("Archivos png","*.png")])
    archivo2 = Image.open(archivo)
    redimensionado = archivo2.resize((256,256))
    render = ImageTk.PhotoImage(redimensionado)
    imgLabel=""
    imgLabel = Button(root, image=render, borderwidth=2, relief='ridge',command=cambiar_Imagen)
    imgLabel.image= render
    imgLabel.grid(row=1, column=1,columnspan=3)

#Guarda la imagen desde la intefaz con el nombre dado
def guardar_imagen(file_name,cat):
    if redimensionado:
        redimensionado.save(('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(cat))+'/images/'+file_name +'.png'))

def eliminar_imagen(file_name,cat):
    if redimensionado:
       os.remove(('dataset/COVID-19_Radiography_Dataset/'+(r"{}".format(cat))+'/images/'+file_name +'.png'))

##Funcion mostrar Integrantes desde el Menubar
def integrantes():
    messagebox.showinfo("Integrantes","Adan Maikon Teran Juarez \n"
                        "Ronald Torrico \n"
                        "Victor Ernesto Ortega L \n"
                        "Antony Urcullo Rosales")




#########Interfaz GUI(root) del Sistema
#Crea Menubar
menubar = Menu(root)
  
# Agrega DatosKaggle Menu y command(llamada de funcion)
Datoskaggle = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Obtener Datos', menu = Datoskaggle)
Datoskaggle.add_command(label ='Covid Kaggle', command = None)

# Agrega Nosotros a Menu and commands
ayuda = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Ayuda', menu = ayuda)
ayuda.add_command(label ='Sobre Nosotros', command = integrantes)


#Titulo del Sistemas
titleLabel = Label(root, text=nombreSistema, font=('Arial bold', 25), bd=2)
titleLabel.grid(row=0, column=2, columnspan=4, padx=5, pady=5)


# label atributos
File_FormatLabel = Label(root, text="File Name", font=('Arial bold', 15))
FormatLabel = Label(root, text="Format", font=('Arial bold', 15))
SizeLabel = Label(root, text="Size", font=('Arial bold', 15))
UrlLabel = Label(root, text="Url", font=('Arial bold', 15))
File_FormatLabel.grid(row=2, column=0, padx=10, pady=10)
FormatLabel.grid(row=3, column=0, padx=10, pady=10)
SizeLabel.grid(row=4, column=0, padx=10, pady=10)
UrlLabel.grid(row=5, column=0, padx=10, pady=10)

#imagen vacia
global redimensionado
img = PhotoImage(file='NoImagen.png')
redimensionado = Image.open('NoImagen.png')
imgLabel = Button(root, image=img, borderwidth=2, relief='ridge',command=cambiar_Imagen)
imgLabel.grid(row=1, column=1,columnspan=3)
# entradas atributos
entryFile_Name = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryFormat = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entrySize = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryUrl = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryFile_Name.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryFormat.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entrySize.grid(row=4, column=1, columnspan=3, padx=5, pady=5)
entryUrl.grid(row=5, column=1, columnspan=3, padx=5, pady=5)

#botones
buttonAgregar = Button(
    root, text="Agregar", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=agregarRegistro)
buttonAgregar.grid(row=6, column=1, columnspan=1)

buttonEditar = Button(
    root, text="Editar", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#ffff00", command=editarRegistro)
buttonEditar.grid(row=6, column=2, columnspan=1)

buttonEliminar = Button(
    root, text="Eliminar", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#e62e00", command=eliminarRegistro)
buttonEliminar.grid(row=6, column=3, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

#Posicion treview(datagrid) en interfaz
my_tree['columns'] = ("FILE NAME", "FORMAT", "SIZE", "URL")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("FILE NAME", anchor=W, width=200)
my_tree.column("FORMAT", anchor=W, width=200)
my_tree.column("SIZE", anchor=W, width=200)
my_tree.column("URL", anchor=W, width=200)
my_tree.grid(row=1, column=4)

#Combobox de categoria
ComboboxCategoria = ttk.Combobox(
    root, values=["Covid","Lung_Opacity","Normal","Viral Pneumonia"],  state="readonly",width=25,
     font=('Arial', 15))
ComboboxCategoria.grid(row=2, column=4, columnspan=3)
#Trae excel a traves de la funcion selection_changed()
ComboboxCategoria.bind("<<ComboboxSelected>>", selection_changed)

#Menuarriba
root.config(menu = menubar)

#llama a Ventana
root.mainloop()