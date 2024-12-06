import tkinter as tk

#Функция закрытия (do_close)
def do_close():
    root.destroy()

#Главное окно
root=tk.Tk()
root.geometry("280x300")
root.title("A/B calculator")

#Метка заголовка
lblTitle = tk.Label(root, text="A/B Calculator", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=20)

#Кнока "Рассчитать"
btnProcess = tk.Button(root, text="Рассчитать", font = ('Helvetica', 10, 'bold' ))
btnProcess.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text="Закрыть", font = ('Helvetica', 10, 'bold' ), command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)

#Закрытие цикла
root.mainloop()
