# Разработать программу с применением пакета tk
# Дано целое число a. Проверить истинность высказывания: «Число a является четным»
try:
    import tkinter as tk
    from tkinter import messagebox


    def check_number():
        try:
            A = int(entry_a.get())

            if A % 2 == 0:
                result_label.config(text=f"Число {A} является четным", fg="green")
            else:
                result_label.config(text=f"Число {A} является не четным", fg="red")
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите целое число")


    # Создание главного окна
    root = tk.Tk()
    root.title("Проверка четности числа")
    root.geometry("300x200")

    # Элементы интерфейса
    tk.Label(root, text="Введите целое число A:").pack(pady=10)
    entry_a = tk.Entry(root)
    entry_a.pack()

    check_button = tk.Button(root, text="Проверить", command=check_number)
    check_button.pack(pady=10)

    result_label = tk.Label(root, text="", font=('Arial', 12))
    result_label.pack()

    root.mainloop()

except ValueError:
    print("ошибка")