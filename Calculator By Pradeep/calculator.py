import tkinter as tk

calculation = ""

def add_to_calculations(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=('Ariel', 24))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1",bg="cadetblue", command=lambda:add_to_calculations(1), width=5,
                  font=("Ariel",15))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2",bg="cadetblue", command=lambda:add_to_calculations(2), width=5,
                  font=("Ariel",15))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3",bg="cadetblue", command=lambda:add_to_calculations(3), width=5,
                  font=("Ariel",15))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4",bg="cadetblue", command=lambda:add_to_calculations(4), width=5,
                  font=("Ariel",15))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5",bg="cadetblue", command=lambda:add_to_calculations(5), width=5,
                  font=("Ariel",15))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6",bg="cadetblue", command=lambda:add_to_calculations(6), width=5,
                  font=("Ariel",15))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7",bg="cadetblue", command=lambda:add_to_calculations(7), width=5,
                  font=("Ariel",15))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8",bg="cadetblue", command=lambda:add_to_calculations(8), width=5,
                  font=("Ariel",15))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", bg="cadetblue",command=lambda:add_to_calculations(9), width=5,
                  font=("Ariel",15))
btn_9.grid(row=4, column=3)
btn_10 = tk.Button(root, text="0",bg="cadetblue", command=lambda:add_to_calculations(0), width=5,
                  font=("Ariel",15))
btn_10.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+",bg="aqua", command=lambda:add_to_calculations("+"), width=5,
                  font=("Ariel",15))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", bg="aqua",command=lambda:add_to_calculations("-"), width=5,
                  font=("Ariel",15))
btn_minus.grid(row=3, column=4)
btn_mul = tk.Button(root, text="*", bg="aqua",command=lambda:add_to_calculations("*"), width=5,
                  font=("Ariel",15))
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text="/",bg="aqua", command=lambda:add_to_calculations("/"), width=5,
                  font=("Ariel",15))
btn_div.grid(row=5, column=4)

btn_11 = tk.Button(root, text="(", bg="cadetblue",command=lambda:add_to_calculations("("), width=5,
                  font=("Ariel",15))
btn_11.grid(row=5, column=1)
btn_12 = tk.Button(root, text=")",bg="cadetblue", command=lambda:add_to_calculations(")"), width=5,
                  font=("Ariel",15))
btn_12.grid(row=5, column=3)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation,bg="darkorange", width=11,
                  font=("Ariel",15))
btn_equals.grid(row=6, column=3, columnspan=2)
btn_clr = tk.Button(root, text="C", command=clear_field,bg="sandybrown" ,width=11,
                  font=("Ariel",15))
btn_clr.grid(row=6, column=1, columnspan=2)

root.mainloop()