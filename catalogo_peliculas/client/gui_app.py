import tkinter as tk
from tkinter import ttk
from model.pelicula_dao import crear_tabla, borrar_table

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=480, height=320)
    
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    
    menu_inicio.add_command(label='Crear Registros', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro', command=borrar_table)
    menu_inicio.add_command(label='Salir', command=root.destroy)
    
    barra_menu.add_cascade(label='Consultas', menu=menu_inicio)
    barra_menu.add_cascade(label='Configuracion', menu=menu_inicio)
    barra_menu.add_cascade(label='Ayuda', menu=menu_inicio)
      


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.config(width=480, height=320)
        self.campos_pelicula()
        self.desabiliar_campos()
        self.tabla_peliculas()
        
    def campos_pelicula(self):
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arieal', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_duracion = tk.Label(self, text='Duracion ')
        self.label_duracion.config(font=('Arieal', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_genero = tk.Label(self, text='Genero: ')
        self.label_genero.config(font=('Arieal', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)
        
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row = 0, column = 1, padx=10, pady=10)
        
        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width=50, font=('Arial', 12))
        self.entry_duracion.grid(row = 1, column = 1, padx=10, pady=10)
        
        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width=50, font=('Arial', 12))
        self.entry_genero.grid(row = 2, column = 1, padx=10, pady=10)
        
        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6',bg='#35BD6F', cursor='hand2', activebackground='#35BD6F')
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10, columnspan = 1)
        
        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_campos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6',bg='#1658A2', cursor='hand2', activebackground='#35866F')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10, columnspan=1)
        
        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.desabiliar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6',bg='#BD152E', cursor='hand2', activebackground='#E15370')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10, columnspan=1)
        
        
    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
            
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')
        
    def desabiliar_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disable')
        self.entry_genero.config(state='disable')
            
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
        
    def guardar_campos(self):
        
        self.desabiliar_campos()
        
    def tabla_peliculas(self):
        self.tabla = ttk.Treeview(self, column = ('Nombre', 'Duracion', 'Genero'))
        self.tabla.grid(row=4, column=0, columnspan = 4)
        
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACION')
        self.tabla.heading('#3', text='GENERO')
        
        self.tabla.insert('',0, text='1',
        values = ('hola', '2.35', 'otros'))
        
        self.boton_Editar = tk.Button(self, text="Nuevo")
        self.boton_Editar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6',bg='#35BD6F', cursor='hand2', activebackground='#35BD6F')
        self.boton_Editar.grid(row=5, column=0, padx=10, pady=10, columnspan = 1)
        
        self.boton_Eliminar = tk.Button(self, text="Guardar")
        self.boton_Eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6',bg='#1658A2', cursor='hand2', activebackground='#35866F')
        self.boton_Eliminar.grid(row=5, column=1, padx=10, pady=10, columnspan=1)
        
        
        