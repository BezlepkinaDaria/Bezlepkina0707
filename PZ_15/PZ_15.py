# Приложение КАФЕДРА для автоматизации работы отдела кадров ВУЗа.
# Таблица Преподавательский состав должна содержать следующие данные:
# Табельный номер, Фамилия И.О., Дата рождения, Должность, Ученая степень, Нагрузка, Зарплата.
try:
    import sqlite3
    from datetime import datetime

    # Создание и подключение к базе данных
    conn = sqlite3.connect('department.db')
    cursor = conn.cursor()

    # Создание таблицы "Преподавательский состав"
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teaching_staff (
        employee_id TEXT PRIMARY KEY,
        full_name TEXT NOT NULL,
        birth_date TEXT NOT NULL,
        position TEXT NOT NULL,
        academic_degree TEXT,
        workload REAL NOT NULL,
        salary REAL NOT NULL
    )
    ''')
    conn.commit()


    def add_teacher():
        print("\nДобавление нового преподавателя:")
        employee_id = input("Табельный номер: ")
        full_name = input("Фамилия И.О.: ")
        birth_date = input("Дата рождения (ДД.ММ.ГГГГ): ")
        position = input("Должность: ")
        academic_degree = input("Ученая степень (если есть): ")
        workload = float(input("Нагрузка (часы/ставка): "))
        salary = float(input("Зарплата: "))

        cursor.execute('''
        INSERT INTO teaching_staff 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (employee_id, full_name, birth_date, position, academic_degree, workload, salary))
        conn.commit()
        print("Преподаватель успешно добавлен!")


    def view_teachers():
        print("\nСписок преподавателей:")
        cursor.execute("SELECT * FROM teaching_staff")
        teachers = cursor.fetchall()

        if not teachers:
            print("Нет данных о преподавателях.")
        else:
            for teacher in teachers:
                print(f"""
                Табельный номер: {teacher[0]}
                ФИО: {teacher[1]}
                Дата рождения: {teacher[2]}
                Должность: {teacher[3]}
                Ученая степень: {teacher[4] or 'нет'}
                Нагрузка: {teacher[5]}
                Зарплата: {teacher[6]}
                """)


    def update_teacher():
        employee_id = input("Введите табельный номер преподавателя для изменения: ")
        cursor.execute("SELECT * FROM teaching_staff WHERE employee_id=?", (employee_id,))
        teacher = cursor.fetchone()

        if not teacher:
            print("Преподаватель не найден!")
            return

        print(f"Текущие данные преподавателя {teacher[1]}:")
        print(f"1. ФИО: {teacher[1]}")
        print(f"2. Дата рождения: {teacher[2]}")
        print(f"3. Должность: {teacher[3]}")
        print(f"4. Ученая степень: {teacher[4]}")
        print(f"5. Нагрузка: {teacher[5]}")
        print(f"6. Зарплата: {teacher[6]}")

        field = input("Выберите номер поля для изменения (1-6): ")
        new_value = input("Введите новое значение: ")

        fields = {
            '1': 'full_name',
            '2': 'birth_date',
            '3': 'position',
            '4': 'academic_degree',
            '5': 'workload',
            '6': 'salary'
        }

        cursor.execute(f'''
        UPDATE teaching_staff 
        SET {fields[field]} = ? 
        WHERE employee_id = ?
        ''', (new_value, employee_id))
        conn.commit()
        print("Данные успешно обновлены!")


    def delete_teacher():
        employee_id = input("Введите табельный номер преподавателя для удаления: ")
        cursor.execute("DELETE FROM teaching_staff WHERE employee_id=?", (employee_id,))
        conn.commit()
        print("Преподаватель удален!" if cursor.rowcount else "Преподаватель не найден!")


    def main_menu():
        while True:
            print("\n=== КАФЕДРА — Управление преподавательским составом ===")
            print("1. Добавить преподавателя")
            print("2. Просмотреть всех преподавателей")
            print("3. Изменить данные преподавателя")
            print("4. Удалить преподавателя")
            print("5. Выход")

            choice = input("Выберите действие (1-5): ")

            if choice == '1':
                add_teacher()
            elif choice == '2':
                view_teachers()
            elif choice == '3':
                update_teacher()
            elif choice == '4':
                delete_teacher()
            elif choice == '5':
                print("Работа завершена.")
                break
            else:
                print("Некорректный ввод!")


    if __name__ == "__main__":
        main_menu()
        conn.close()

except ValueError:
    print("Ошибка")
