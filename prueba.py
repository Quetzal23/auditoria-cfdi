import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("Preguntas")
        self.respuesta = tk.Entry(self)
        self.respuesta.place(x=100, y=40)
        self.pregunta=tk.Label(self,text="¿Cuál es la capital de Brasil?")
        self.pregunta.place(x=10,y=10)
        self.label=tk.Label(self,text="Responde:").place(x=20,y=40)
        self.tiempo=tk.Label(self,text="1")
        self.tiempo.place(x=300,y=10)
        self.controlar=tk.Button(self,text="Verificar",command=self.verificacion)
        self.controlar.place(x=60,y=90)
        self.remaining=0
        self.countdown(5)
 
    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining
 
        elif self.remaining == 100:
            return
        if self.remaining <= 0:
            self.tiempo.configure(text="Se agotó el tiempo")
        else:
            self.tiempo.configure(text="Espere por %d seg" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
 
    def verificacion(self):
        self.ver=self.respuesta.get()
        if self.ver == "Brasilia":
            self.tiempo.configure(text="Excelente!!")
            self.remaining=100
 
 
 
if __name__ == "__main__":
    app = App()
    app.mainloop()