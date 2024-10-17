#помилки розділяються на файлові та інші

#функція створює(відкриває) текстовий файл і додає в кінець питання
def write_question(filename):
    try:
        with open(filename, 'a') as file:
            question = input("Введіть питання: ")
            file.write(f"Питання: {question}\n")
    except IOError as err:
        print(f"Error with file: {err}")
    except Exception as err:
        print(f"Error: {err}")

#записати відповідь у файл + ім'я, фамілія
def write_answer(filename, answer_text):
    try:
        with open(filename, 'a') as file:
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
    return f"{surname} {name}\nВідповідь: {'\n'.join(answer)}"

#функція читає і виводить зміст файлу
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except IOError as err:
        print(f"Error with file: {err}")
    except Exception as err:
        print(f"Error: {err}")
        
read_file("output.txt")
write_answer("output.txt", answer_question())
write_question("output.txt")
read_file("output.txt")
