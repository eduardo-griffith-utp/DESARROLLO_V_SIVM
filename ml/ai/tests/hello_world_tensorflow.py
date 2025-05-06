import tensorflow as  tf
import tkinter as tk
hello_world = tf.constant("Hello World")
hw_value = hello_world.numpy().decode('utf-8')
window = tk.Tk()
window.title("Impresion de Hello World con TensorFlow")
label = tk.Label(window, text=f"{hw_value}")
label.pack(padx=20,pady=20)
window.mainloop()