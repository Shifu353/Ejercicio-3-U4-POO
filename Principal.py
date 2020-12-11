import sys

version = sys.version_info.major

if (version < 3):
    try:
        import Tkinter
    except ImportError:
        raise ("Se solicita una version de python de 3.X")
else:
    try:
        import tkinter as tk
        import getpass
        from tkinter import font,ttk
        import requests
        class Moneda():
            __ventana = None
            __dolarventa = None
            __dolarcompra = None
            def __init__ (self):
                respuesta = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
                respuesta_json = respuesta.json()
                #print(len(respuesta_json))
                i = 0
                self.Listanom = []
                self.Listaventa= []
                self.ListaCompra = []
                #print(respuesta_json[5]["casa"]["nombre"].find("Dolar"))
                while(i<len(respuesta_json)):
                    if(respuesta_json[i]["casa"]["nombre"].find("Dolar") != -1):
                        #print(respuesta_json[i]["casa"]["compra"])
                        if(respuesta_json[i]["casa"]["compra"] != "No Cotiza"):
                            self.__nombredolar = respuesta_json[i]["casa"]["nombre"]
                            self.Listanom.append(self.__nombredolar)
                            self.__dolarventa = respuesta_json[i]["casa"]["venta"]
                            self.Listaventa.append(self.__dolarventa)
                            self.__dolarcompra = respuesta_json[i]["casa"]["compra"]
                            self.ListaCompra.append(self.__dolarcompra)
                    i += 1
                
                self.__ventana = tk.Tk()
                self.__ventana.geometry("350x200")
                texto = "Bienvenido/a %s a mi ejercicio 3" %getpass.getuser()
                self.__ventana.title(texto)
                self.myframe = ttk.Frame(self.__ventana,relief="raised",padding=(10,10))
                self.myframe.grid(row=0,column=0,padx=10,pady=10)

                ttk.Label(self.myframe,text="Nombre del Dolar").grid(row=0,column=0,padx=1,pady=1)
                ttk.Separator(self.myframe,orient=tk.VERTICAL)
                ttk.Label(self.myframe,text="Compra").grid(row=0,column=3,padx=4,pady=4)
                ttk.Label(self.myframe,text="Venta").grid(row=0,column=5,padx=6,pady=6,sticky=tk.NE)
                for i in range(len(self.Listanom)):
                    ttk.Label(self.myframe,text=self.Listanom[i],font="Arial 7").grid(row=i+1,column=0)
                for c in range(len(self.ListaCompra)):
                    ttk.Label(self.myframe,text=self.ListaCompra[c]).grid(row=c+1,column=1)
                
                self.__ventana.mainloop()
        if __name__ == "__main__":
            app=Moneda()
    except ImportError:
        raise ("Se solicita una version de python de 3.X")
