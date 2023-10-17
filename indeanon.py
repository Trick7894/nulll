COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "RED": "\033[31m",
    "CYAN": "\033[36m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m",
    "BLUE": "\033[34m",
}


def get_in(databased_file, searchd_value):
    found = False

    with open(databased_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 2:
            instagram = data[4]
            if searchd_value in instagram:
                EMAIL = data[0]
                FNAME = data[1]
                LNAME = data[2]
                PHONE = data[3]

                print(f'''{COLOR_CODE["BLUE"]}
       {COLOR_CODE["RED"]}
                Почта пользователя: {EMAIL}
                Первый ник пользователя: {FNAME}
                Последний ник пользователя: {LNAME}
                Телефон пользователя: {PHONE}
                Инстаграм пользователя: {instagram}



                      ''')
                found = True

    if not found:
        print(f'{COLOR_CODE["RED"]}[ERROR]Ничего не найдено в базе данных по Инстаграм')
    for line in lines:
        data = line.strip().split('|""')
        if len(data) >= 3:
            phone = data[2]
            if searchd_value in phone:
                user_id = data[3]
                registration_date = data[0]
                print(f'''{COLOR_CODE["RED"]}

                 {COLOR_CODE["RED"]}
                 ФИО пользователя: {registration_date}
                 Почта пользователя: {user_id}
                 ТЕЛЕФОН: {phone}

                    ''')
                found = True

    if not found:
        print("not base")

