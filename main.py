from tkinter import *
from tkinter import messagebox
import random
import time

class Ball:  # создаём класс Мяч
    def __init__(self, canvas, paddle, color):  # создаём функцию, которая принимает аргументы холст, ракетку и цвет
        self.canvas = canvas  # сохраняем аргумент canvas в свойстве с таким же именем
        self.paddle = paddle  # сохраняем аргумент paddle в свойстве с таким же именем
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # вызываем функцию для рисования круга с 5 аргументами -> х и у левого верхнего угла (10, 10)
                                                                 # х и у правого нижнего угла (25, 25) и цвет заполнения
        self.canvas.move(self.id, 245, 100)  # перемещаем круг (self.id) в центр холста
        starts = [-3, -2, -1, 1, 2, 3]  # создаём переменную и помещаем в неё список из 6 цифр
        random.shuffle(starts)  # перемешиваем рандомно элементы списка
        self.x = starts[0]  # по горизонтале может выпасть любое значение из списка starts
        self.y = -3  # -3 - перемещение на три пикселя вверхдля ускорения движения
        self.canvas_height = self.canvas.winfo_height()  # функция возвращает текущую высоту холста
        self.canvas_width = self.canvas.winfo_width()  # функция возвращает текущую ширину холста
        self.hit_bottom = False  # свойство мяча, при котором он достиг нижней границы холста

    def hit_paddle(self, pos):  # объявляем функцию с аргументом pos, в котором будем передавать текущие координаты мяча
        paddle_pos = self.canvas.coords(self.paddle.id)  #  получаем координаты ракетки и сохраняем их в переменной paddle_pos
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:  # если х-координата правой стороны мяча, больше х-координаты
                                                                 # левой стороны ракетки и х-координата левой стороны мяча
                                                                 # меньше, чем х-координата правой стороны ракетки
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:  # проверяет не находится ли нижняя сторона мяча pos[3] между
                                                                     # верхом ракетки paddle_pos[1] и её низом paddle_pos[3]
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  # перемещение мяча (self.id) по координатам холста
        pos = self.canvas.coords(self.id)  # помещаем в переменную значение, полученное от функции холста coords (она
                                           # возвращает х и у координаты любой фигуры на холсте по идентификатору(мяч))
        if pos[1] <= 0:  # сравниваем верх мяча с верхней границей холста, если мяч достиг верха, то прекращаем его двигать вверх
            self.y = 3  # перестаем вычитать 3 из его вертикальной координаты, вместо этого прибавляем 3, что бы мяч сменил направление
        if pos[3] >= self.canvas_height:  # сравниваем низ мяча с текущей высотой холста
            self.hit_bottom = True  # проверяем не коснулся ли мяч нижней границы холста
        if self.hit_paddle(pos) == True:  # проверка на столкновении мяча с ракеткой
            self.y = -3  # если функция возвращает True, то мы меняем направление полета мяча
        if pos[0] <= 0:  # сравниваем левый край мяча с левой границей холста, если мяч достиг её, то прекращаем его двигать влево
            self.x = 3  # перестаем вычитать 3 из его горизонтальной координаты, вместо этого прибавляем 3, что бы мяч сменил направление
        if pos[2] >= self.canvas_width:  # сравниваем правый край мяча с текущей шириной холста
            self.x = -3  # вычитаем пока правый край мяча не коснеться правой стороны холста


class Paddle:  # создаём класс Ракетка
    def __init__(self, canvas, color):  # создаём функцию, которая принимает аргументы холст и цвет
        self.canvas = canvas  # сохраняем аргумент canvas в свойстве с таким же именем
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)   # вызываем функцию для рисования прямоугольника с 5 аргументами -> х и у левого верхнего угла (0, 0)
                                                                 # х и у правого нижнего угла (100, 10) и цвет заполнения
        self.canvas.move(self.id, 200, 300) # перемещаем ракетку в позицию 200 пикселей от левого края холста и 300 пикселей
                                            # от верхнего края
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()  # функция возвращает текущую ширину холста
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)  # Привязываем событие нажатия кнопки влево к параметру функции
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)  # Привязываем событие нажатия кнопки вправо к параметру функции

    def draw(self):
        self.canvas.move(self.id, self.x, 0)  # перемещение ракетки (self.id) по координатам холста, по вертикали 0
        pos = self.canvas.coords(self.id)  # помещаем в переменную значение, полученное от функции холста coords (она
                                           # возвращает х и у координаты любой фигуры на холсте по идентификатору(ракетка))
        if pos[0] <= 0:  # если левый край ракетки касаеться левого края холста, то останавливаеться
            self.x = 0  # обнуляем свойство х
        elif pos[2] >= self.canvas_width:  # иначе правый край ракетки касаеться правого края холста, то останавливаеться
            self.x = 0  # обнуляем свойство х

    def turn_left(self, evt):  # Создаём функцию для привязки к нажатию клавиши-стрелки "влево"
        self.x = -2

    def turn_right(self, evt):  # Создаём функцию для привязки к нажатию клавиши-стрелки "вправо"
        self.x = 2

# def start():
    # StartButton = Button(tk)  # Кнопка для начала игры
    # StartButton["text"] = "Начало игры"
    # StartButton.bind("<Button-1>")
    # StartButton.pack()

# def exit():
    # ExitButton = Button(tk)  # Кнопка для конца игры
    # ExitButton["text"] = "Конец игры"
    # ExitButton.bind("<Button-1>")
    # ExitButton.pack()


tk = Tk()
tk.title("Game Ping-Pong")  # заголовок игрового окна
tk.resizable(0, 0)  # функция фиксирует размер окна
tk.wm_attributes("-topmost", 1)  # размещает холст поверх всех окон ("-topmost")
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)  # задаём размеры холста
canvas.pack()  # при вызове функции холст принимает параметры выше
tk.update()  # подготавливает tkinter к игровой анимации
canvas.focus_set()  # Установим фокус на Canvas чтобы он реагировал на нажатия клавиш

def closing_windom():  # Функция отвечающая за выход из игры и закрытие окна
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        tk.destroy()

tk.protocol("WM_DELETE_WINDOW", closing_windom)  # Обращаемся к функции закрытия окна

paddle = Paddle(canvas, "green")  # создаём объект Ракетка синего цвета
ball = Ball(canvas, paddle, "purple")  # создаём обЪект Мяч красного цвета

while 1:  # бесконечный цикл, пока не закроем окно
    if ball.hit_bottom == False:  # проверяем не достиг ли мяч нижней границы холста
        ball.draw()  # вызывает мяч
        paddle.draw()  # вызываем ракетку
    tk.update_idletasks()  # перерисовывает экран
    tk.update()  # подготавливает tkinter к игровой анимации
    time.sleep(0.01)  # делает паузу на одну сотую секунды



