from tkinter import *
import math
import unittest

window = Tk()
window.title('Расчёт')
window.geometry('500x400')

def calculate():
    val = value1.get().split(';')
    mas = []
    for item in val:
        mas.append(float(item))
    result = Function(mas)
    label2["text"] = ", ".join(str(i) for i in result)

def Main(args):
    numbers = []

    try:
        while True:
            numberString = input()

            if numberString == ".":
                break

            temp_out_number = OutObject()
            if not TryParseHelper.try_parse_float(numberString, temp_out_number):
                number = temp_out_number.arg_value
                raise Exception()
            else:
                number = temp_out_number.arg_value

            numbers.append(number)

        result = Function(numbers)

        for arg in result:
            print(arg)
    except Exception as ex:
        print(ex.Message)

def Function(args):
    result = []

    for arg in args:
        newNumber = 0

        if arg < 1.1:
            newNumber = math.sin(math.e) + math.tan(arg)
        else:
            newNumber = math.log(abs(math.sin(arg) + math.sqrt(2 * arg)))

        result.append(newNumber)

    return result

class OutObject:
    def __init__(self):
        self.arg_value = None

class TryParseHelper:
    @staticmethod
    def try_parse_int(s, result):
        try:
            result.arg_value = int(s)
            return True
        except:
            return False

    @staticmethod
    def try_parse_float(s, result):
        try:
            result.arg_value = float(s)
            return True
        except:
            return False

    @staticmethod
    def try_parse_bool(s, result):
        try:
            result.arg_value = bool(s)
            return True
        except:
            return False

class TestStringMethods(unittest.TestCase):

    def test_function(self):
        result = Function([2.0, -54.0])
        self.assertEqual(1.06791161795298, result[0])
        self.assertEqual(-0.263018810145151, result[1])


frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

label1 = Label(
    frame,
    text="Введите значение  "
)
label1.grid(row=3, column=1)

label2 = Label(
    frame,
    text="Результат  ",
)
label2.grid(row=4, column=1)

value1 = Entry(
    frame,
)
value1.grid(row=3, column=2, pady=5)



cal_btn = Button(
    frame,
    text='Рассчитать ',
    command=calculate
)
cal_btn.grid(row=5, column=2)

window.mainloop()




