import numpy
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Calcolatrice")
window.geometry("210x280")
window.resizable(False, False)
window.configure(background="light gray")
#icona del programma
im = Image.open("myIcon.ico")
photo = ImageTk.PhotoImage(im)
window.wm_iconphoto(True, photo)

#funzioni
def somma():
    num1 = float(input_num1.get())
    num2 = float(input_num2.get())
    risultato.set(num1 + num2)

def sottrazione():
    num1 = float(input_num1.get())
    num2 = float(input_num2.get())
    risultato.set(num1 - num2)

def moltiplicazione():
    num1 = float(input_num1.get())
    num2 = float(input_num2.get())
    risultato.set(num1 * num2)

def divisione():
    num1 = float(input_num1.get())
    num2 = float(input_num2.get())
    if num2 == 0:
        risultato.set("Impossibile")
    else:
        risultato.set(num1 / num2)

#interfatccia
etichetta=tk.Label(window, text="Calcolatrice", fg="#008080", font=("Verdana", 20), background="Light gray")
etichetta.grid(row=0, column=1, sticky="N", padx=5, pady=5)

etichetta=tk.Label(window, text="Inserisci il primo numero:", fg="#808080", font=("Verdana", 10), background="Light gray")
etichetta.grid(row=1, column=1, sticky="N", padx = 5)

input_num1 = tk.Entry(window)
input_num1.grid(row=2, column=1, sticky="N")

etichetta=tk.Label(window, text="Inserisci il secondo numero:", fg="#808080", font=("Verdana", 10), background="Light gray")
etichetta.grid(row=3, column=1, sticky="N", padx = 5, pady=5)

etichetta=tk.Label(window, text="Inserisci il secondo numero:", fg="#808080", font=("Verdana", 10), background="Light gray")
etichetta.grid(row=3, column=1, sticky="N", padx = 5, pady=5)

input_num2 = tk.Entry(window)
input_num2.grid(row=4, column=1, sticky="N")

etichetta=tk.Label(window, text="Scegli l'operazione da svolgere", fg="#808080", font=("Verdana", 10), background="Light gray")
etichetta.grid(row=5, column=1, sticky="N")

#pulsanti operazione
plus_button = tk.Button(text="+", bg="#008080", command= somma)
plus_button.place(x=5, y=180)

minus_button = tk.Button(text="-", bg="#008080", command= sottrazione)
minus_button.place(x=65, y=180)

mult_button = tk.Button(text="x", bg="#008080", command= moltiplicazione)
mult_button.place(x=115, y=180)

mult_button = tk.Button(text=":", bg="#008080", command= divisione)
mult_button.place(x=170, y=180)

# Variabile risultato
risultato = tk.StringVar()
risultato.set("")  # Inizialmente vuoto

#etichetta risultato
etichetta=tk.Label(window, text="Risultato:", fg="#808080", font=("Verdana", 10), background="Light gray")
etichetta.place(relx=0.5 , y=225, anchor="center")

# Etichetta per visualizzare il risultato al centro
risultato_label = tk.Label(window, textvariable=risultato, fg="#008080", font=("Verdana", 12), background="Light gray")
risultato_label.place(relx=0.5 , y= 250, anchor="center")


if __name__ == "__main__":
    window.mainloop()
