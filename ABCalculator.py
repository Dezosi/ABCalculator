import tkinter as tk
from tkinter import messagebox as mb
import os
import math

#Функция закрытия (do_close)
def do_close():
    root.destroy()
    
#Функция форматирования процентов
def num_percent(num):
    return "{:.2f}".format(num*100).rjust(10) + '%'
    
#Функция считывания данных из полей ввода
def do_processing():
    n1 = int(entVisitors1.get())
    c1 = int(entConversions1.get())
    n2 = int(entVisitors2.get())
    c2 = int(entConversions2.get())
    
    #Проверка данных из полей ввода
    if n1<=0 or n2 <=0:
        mb.showerror(title="ERROR", message="Неверное количество посетителей")
        return
    
    #Открытие окна результатов
    popup_window(n1, c1, n2, c2)

def popup_window(n1, c1, n2, c2):
    window = tk.Toplevel()
    window.geometry("500x500")
    window.title("A/B результат")
    
    #Добавление вызова окна результатов
    txtOutput = tk.Text(window, font = ('Courier New', 10, 'bold'))
    txtOutput.place(x=15, y=115, width=470, height=300)
    
    #Добавление заголовка
    txtOutput.insert(tk.END, '                              Контрольная     Тестовая' + os.linesep)
    txtOutput.insert(tk.END, '                              группа          группа' + os.linesep)
    txtOutput.insert(tk.END, '                                              ' + os.linesep)
    
    #Добавление вывода конверсии и стандартного отклонения
    p1 = c1/n1
    p2 = c2/n2
    txtOutput.insert(tk.END, 'Конверсия                ' + num_percent(p1)
        +'      '+ num_percent(p2) + os.linesep)
        
    sigma1 = math.sqrt(p1*(1-p1)/n1)
    sigma2 = math.sqrt(p2*(1-p2)/n2)
    txtOutput.insert(tk.END, 'Стандартное отклонение   '+ num_percent(sigma1)
        +'      '+ num_percent(sigma2) + os.linesep)
    txtOutput.insert(tk.END,'                                                  ' + os.linesep)
    
    #Кнопка закрытия
    btnClosePopup = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold' ), command=window.destroy)
    btnClosePopup.place(x=190, y=450, width=90, height=30)
    
    #Перевод фокуса на созданное окно
    window.focus_force()

#Главное окно
root=tk.Tk()
root.geometry("280x300")
root.title("A/B calculator")

#Метка заголовка
lblTitle = tk.Label(root, text="A/B Calculator", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=20)

#Метка заголовка контрольной группы
lblTitle = tk.Label(root, text="Контрольная группа", font = ('Helvetica', 12, 'bold'), fg = '#0066ff')
lblTitle.place(x=25, y=55)

#Поля ввода контрольной группы
lblVisitors1 = tk.Label(text="Посетители", font = ('Helvetica', 10, 'bold'))
lblVisitors1.place(x=25, y=85)

entVisitors1 = tk.Entry(font = ('Helvetica', 10, 'bold' ), justify='center')
entVisitors1.place(x=115, y=85, width=90, height=20)
entVisitors1.insert(tk.END, '255')

lblConversions1 = tk.Label(text="Конверсии", font = ('Helvetica', 10, 'bold'))
lblConversions1.place(x=25, y=115)

entConversions1 = tk.Entry(font = ('Helvetica', 10, 'bold' ), justify='center')
entConversions1.place(x=115, y=115, width=90, height=20)
entConversions1.insert(tk.END, '26')

#Метка заголовка ТЕСТовой группы
lblTitle = tk.Label(root, text="Контрольная группа", font = ('Helvetica', 12, 'bold'), fg = '#008800')
lblTitle.place(x=25, y=145)

#Поля ввода ТЕСТовой группы
lblVisitors2 = tk.Label(text="Посетители", font = ('Helvetica', 10, 'bold'))
lblVisitors2.place(x=25, y=175)

entVisitors2 = tk.Entry(font = ('Helvetica', 10, 'bold' ), justify='center')
entVisitors2.place(x=115, y=175, width=90, height=20)
entVisitors2.insert(tk.END, '235')

lblConversions2 = tk.Label(text="Конверсии", font = ('Helvetica', 10, 'bold'))
lblConversions2.place(x=25, y=205)

entConversions2 = tk.Entry(font = ('Helvetica', 10, 'bold' ), justify='center')
entConversions2.place(x=115, y=205, width=90, height=20)
entConversions2.insert(tk.END, '18')

#Кнока "Рассчитать"
btnProcess = tk.Button(root, text="Рассчитать", font = ('Helvetica', 10, 'bold' ), command=do_processing)
btnProcess.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text="Закрыть", font = ('Helvetica', 10, 'bold' ), command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)

#Закрытие цикла
root.mainloop()
