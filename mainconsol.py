import smtplib, ssl, csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# начало блока работы с данными пользователей
# ----------------------------------------------------------
# начало работы с оценками
#-----------------------------------------------------------


def value_column_score():
    print("Имя", "Фамилия")
    return input("Введите по какому параметру искать: ")


def input_user_1(val):
    return input("Ввод параметра " + val.lower() + ": ")


def find_scores_user(value, line):
    f = open("inf/оценки.csv", "r")
    a = csv.DictReader(f, delimiter=',')

    for col in a:
        if value in col[line]:
            print("{:15s} {:15s} {:20s} {:20s} {:30s} {:30s} {:30s} {:30s}".
                  format(col["Имя"], col["Фамилия"],
                         str(col["Оператор условия"]),
                         str(col["Построение графиков"]),
                         str(col["Сортировка и фильтрация"]),
                         str(col["Контрольная работа № 3"]),
                         str(col["Контрольная работа № 1"]),
                         str(col["Итоговая оценка за курс"])))


def data_users_score():
    data = open("inf/оценки.csv", "r")
    a = "Имя,Фамилия,Оператор условия,Построение графиков,Сортировка и фильтрация,Контрольная работа № 3," "Контрольная работа № 1,Итоговая оценка за курс".split(
        ",")
    print("{:15s} {:15s} {:20s} {:20s} {:30s} {:30s} {:30s} {:30s}".format(
        a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]))
    for col in csv.DictReader(data, delimiter=","):
        print("{:15s} {:15s} {:20s} {:20s} {:30s} {:30s} {:30s} {:30s}".format(
            col["Имя"], col["Фамилия"], str(col["Оператор условия"]),
            str(col["Построение графиков"]),
            str(col["Сортировка и фильтрация"]),
            str(col["Контрольная работа № 3"]),
            str(col["Контрольная работа № 1"]),
            str(col["Итоговая оценка за курс"])))


#------------------------------------------------------------
#Конец работы с оценками


def value_column():
    print("Логин", "Имя", "Фамилия", "Электронная почта")
    return input("Введите по какому параметру искать: ")


def input_user(val):
    return input("Ввод параметра " + val.lower() + ": ")


def read_to_file(value, line):
    f = open("inf/users.csv", "r")
    a = csv.DictReader(f, delimiter=',')

    for col in a:
        if value in col[line]:
            print("{:20s} {:20s} {:20s} {:20s} {:20s}".format(
                col["Логин"], col["Пароль"], col["Имя"], col["Фамилия"],
                col["Электронная почта"]))


def output_all_users():
    f = open("inf/users.csv", "r")
    a = csv.DictReader(f, delimiter=',')

    for col in a:
        print("{:20s} {:20s} {:20s} {:20s} {:20s}".format(
            col["Логин"], col["Пароль"], col["Имя"], col["Фамилия"],
            col["Электронная почта"]))

#Конец блока работы с данными пользователей
# ---------------------------------------------------------




#-----------------------------------------------------
#Начало блока работы с электронной почтой
def mail_choice():
    return input(
        "Введите адрес электронной почты на который надо отправить сообщение: "
    )


def subject_email():
    return input("Введите тему письма: ")


def send_message():
    return input("Введите сообщение, которое хотите отправить пользвателю: ")


def send_email(mes, sub, m_usr):
    sender_email = "mtest8893@gmail.com"
    receiver_email = m_usr
    password = "316853bl98d3"

    message = MIMEMultipart("alternative")
    message["Subject"] = sub
    message["From"] = sender_email
    message["To"] = m_usr

    text = mes
    html = """\
    <html>
      <body>
        <img src = "https://im0-tub-ru.yandex.net/i?id=df192ca99ba344222fdb5bafdb390569-l&n=13"
        <h1>
        Привет
        </h1>
      </body>
    </html>
    """
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


#----------------------------------------------------------------------------------
#Конец блока работы с электронной почтой


#Начало блока визуализации данных
#Находим пользователя
def data():
    f = open("inf/оценки.csv", "r")
    a = csv.DictReader(f, delimiter=',')

    for col in a:
        print(col['Фамилия'] + ' ' + col['Имя'])
        # print(col[2:])

    f.close()

    f = open("inf/оценки.csv", "r")
    a = csv.DictReader(f, delimiter=',')

    value = input("Введите имя или фамилию пользователя: ")

    for col in a:
        user = col['Фамилия'] + ' ' + col['Имя']
        print(user)
        if value in user:
            #return col[2:]
            print('123')

#Функция для перевода списка строк в список чисел
#-------------------------------------------------------------
#переводим его оценки в в чисорврй тип
def convert(data):
    return [int(item) for item in data]
#-------------------------------------------------------------
#Функция для перевода списка строк в список чисел

def visual_data(data):
    X = list(range(len(data)))
    Y = data

    plt.xlim(0, len(data))
    plt.ylim(0, max(data) + 1)

    plt.xlabel("Номер задания курса")
    plt.ylabel("Оценка")
    plt.title('График изменения оценок студента')

    plt.plot(X, Y, linewidth=3, color='blue')
    plt.plot(
        X,
        Y,
        'o',
        color='gray',
        markersize=8, linewidth=5,
        markerfacecolor='red',
        markeredgecolor='gray',
        markeredgewidth=2)

    plt.legend(['Изменение', 'Контрольные точки'], loc='lower left')

    plt.show()

#Конец работы с графиками
#------------------------------------------------------------------------------
def main():
    print(
        "Меню выбирите из предложенного списка нужную функцию из представленных ниже: "
    )

    while True:
        print(""" 
            1. Просмотреть данные о пользователе или пользователях(информация в таблице: логин,пароль,имя,фамилия,  эл.почта)
            2. Посмотреть журнал оценок
            3. Послать оповещение пользователю или пользователям
            4. Вывести график зависимости 
            5. Выход

            """)
        user_input = input("Введите цифру соответствующую разделу меню: ")
        if user_input == "1":
            if input("Хотите посмотреть информацию о конкретном пользователе? "
                     "Введите Да для продолжения: ") == "Да":
                value = value_column()
                line = input_user(value)
                read_to_file(line, value)
                continue

            else:
                print("Произведен вывод информации о всех пользователях")
                output_all_users()
                continue

        if user_input == "2":
            if input("Хотите посмотреть оценки конкретного пользователя,"
                     " введите Да для подтверждения: ") == "Да":
                value = value_column_score()
                line = input_user_1(value)
                a = "Имя,Фамилия,Оператор условия,Построение графиков,Сортировка и фильтрация,Контрольная работа № 3," "Контрольная работа № 1,Итоговая оценка за курс".split(
                    ",")
                print(
                    "{:15s} {:15s} {:20s} {:20s} {:30s} {:30s} {:30s} {:30s}".
                    format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]))
                find_scores_user(line, value)
                continue
            else:
                data_users_score()
                break
        if user_input == "3":
            message = send_message()
            subject = subject_email()
            mail_receiver = mail_choice()
            send_email(message, subject, mail_receiver)
            continue
        if user_input == "4":
            #graph_user = data()
            #data_convert = convert(graph_user)
            #visual_data(data_convert)
            data()

        if user_input == "5":
            if input(
                    "Вы желаете выйти? для подверждения введите Да: ") == "Да":
                break
            else:
                continue
main()