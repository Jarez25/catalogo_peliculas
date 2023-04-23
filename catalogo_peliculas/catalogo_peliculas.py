import tkinter as tk
from  client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Catalogo De Peliculas')
    root.resizable(1,1)
    barra_menu(root)
    
    
    app = Frame(root=root)
    
    app.mainloop()

if __name__=='__main__':
    main()