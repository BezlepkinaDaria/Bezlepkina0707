try:
    import tkinter as tk
    from tkinter import ttk


    def register():
        # Логика обработки данных (можно добавить сохранение в файл/БД)
        print("Регистрация завершена!")
        print("Имя:", entry_name.get())
        print("Пароль:", entry_password.get())
        print("Подтверждение пароля:", entry_confirm.get())
        print("Специализация:", combo_specialization.get())
        print("Пол:", gender_var.get())
        print("Навыки:", [skill for skill, var in skills_vars.items() if var.get()])
        print("Доп. сведения:", text_about.get("1.0", tk.END))


    def clear_form():
        entry_name.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        entry_confirm.delete(0, tk.END)
        combo_specialization.set("Web-мастер")
        gender_var.set("")
        for var in skills_vars.values():
            var.set(False)
        text_about.delete("1.0", tk.END)


    # Создание главного окна
    root = tk.Tk()
    root.title("Анкета Web-разработчика")
    root.geometry("600x540")
    root.resizable(False, False)

    # Заголовок
    title_label = tk.Label(root, text="Анкета Web-разработчика", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    # Фрейм для основной формы
    form_frame = tk.Frame(root)
    form_frame.pack(padx=20, pady=10, fill=tk.X)

    # Регистрационное имя
    tk.Label(form_frame, text="Регистрационное имя", anchor="w").grid(row=0, column=0, sticky="w", pady=2)
    entry_name = tk.Entry(form_frame)
    entry_name.grid(row=0, column=1, sticky="ew", padx=5, pady=2)
    root.columnconfigure(0, weight=10, minsize=10, pad=10)

    # Пароль
    tk.Label(form_frame, text="Пароль", anchor="w").grid(row=1, column=0, sticky="w", pady=2)
    entry_password = tk.Entry(form_frame, show="*")
    entry_password.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

    # Подтверждение пароля
    tk.Label(form_frame, text="Подтвердите пароль", anchor="w").grid(row=2, column=0, sticky="w", pady=2)
    entry_confirm = tk.Entry(form_frame, show="*")
    entry_confirm.grid(row=2, column=1, sticky="ew", padx=5, pady=2)

    # Специализация
    tk.Label(form_frame, text="Ваша специализация", anchor="w").grid(row=3, column=0, sticky="w", pady=2)
    combo_specialization = ttk.Combobox(form_frame, values=["Web-мастер", "Frontend", "Backend", "Fullstack"])
    combo_specialization.set("Web-мастер")
    combo_specialization.grid(row=3, column=1, sticky="ew", padx=5, pady=2)

    # Пол
    tk.Label(form_frame, text="Пол", anchor="w").grid(row=4, column=0, sticky="w", pady=2)
    gender_frame = tk.Frame(form_frame)
    gender_frame.grid(row=4, column=1, sticky="w", padx=5, pady=2)
    gender_var = tk.StringVar()
    tk.Radiobutton(gender_frame, text="М", variable=gender_var, value="М").pack(side=tk.LEFT)
    tk.Radiobutton(gender_frame, text="Ж", variable=gender_var, value="Ж").pack(side=tk.LEFT, padx=10)

    # Навыки
    tk.Label(form_frame, text="Ваши навыки", anchor="w").grid(row=5, column=0, sticky="nw", pady=2)
    skills_frame = tk.Frame(form_frame)
    skills_frame.grid(row=5, column=1, sticky="w", padx=5, pady=2)

    skills = [
        "знание HTML и CSS",
        "знание Perl",
        "знание ASP",
        "знание Adobe Photoshop",
        "знание JAVA",
        "знание JavaScript",
        "знание Flash"
    ]

    skills_vars = {}
    for i, skill in enumerate(skills):
        skills_vars[skill] = tk.BooleanVar()
        tk.Checkbutton(skills_frame, text=skill, variable=skills_vars[skill], anchor="w").grid(row=i, column=0,
                                                                                               sticky="w")

    # Дополнительные сведения
    tk.Label(form_frame, text="Дополнительные сведения о себе", anchor="w").grid(row=6, column=0, sticky="nw", pady=2)
    text_about = tk.Text(form_frame, height=5, width=30)
    text_about.grid(row=6, column=1, sticky="ew", padx=5, pady=2)

    # Кнопки
    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=20)

    tk.Button(buttons_frame, text="зарегистрировать", command=register).pack(side=tk.LEFT, padx=10)
    tk.Button(buttons_frame, text="очистить форму", command=clear_form).pack(side=tk.LEFT, padx=10)

    # Настройка растягивания колонок
    form_frame.columnconfigure(1, weight=1)

    root.mainloop()

except ValueError:
    print("ошибка")