#помилки розділяються на файлові та інші

#функція створює(відкриває) текстовий файл і додає в кінець питання
def write_question(filename):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            question = input("Введіть питання: ")
            file.write(f"Питання: {question}\n")
    except IOError as err:
        print(f"Error with file: {err}")
    except Exception as err:
        print(f"Error: {err}")

#записати відповідь у файл + ім'я, прізвище
def write_answer(filename, answer_text):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"{answer_text}\n")
    except IOError as err:
        print(f"Error with file: {err}")
    except Exception as err:
        print(f"Error: {err}")

#функція обробки даних з консолі
def answer_question():
    surname = input("Введіть ваше прізвище: ")
    name = input("Введіть ваше ім'я: ")
    print("Ваша відповідь (введіть порожній рядок, щоб завершити):")
    answer = []
    while True:
        line = input()
        if line == "":
            break
        answer.append(line)
    return f"\n{surname} {name}\nВідповідь: {'\n'.join(answer)}"

#функція читає і виводить зміст файлу
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except IOError as err:
        print(f"Error with file: {err}")
    except Exception as err:
        print(f"Error: {err}")


#Плутенко
# Функція додає меню, що надає користувачеві вибір дій:
# 1. Прочитати вміст файлу.
# 2. Додати дані до файлу.
# 3. Додати питання до файлу.
# 4. Вийти з програми.
# Програма продовжує виконуватися, доки користувач не введе опцію "4" для завершення.
def menu(name_file):
    while True:
        print("\nОберіть дію:")
        print("1. Прочитати файл")
        print("2. Додати відповідь")
        print("3. Додати питання")
        print("4. Вийти")
        choice = input("(1, 2, 3 або 4): ")

        if choice == '1':
            read_file(name_file)
        elif choice == '2':
            write_answer(name_file, answer_question())
        elif choice == '3':
            write_question(name_file)
        elif choice == '4':
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

menu("output.txt")