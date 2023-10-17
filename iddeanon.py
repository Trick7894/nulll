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


def get_tg(databases_file, databasesh_file, databasesk_file, databasesl_file, databasesm_file,
           searchs_value):
    found = False

    with open(databases_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|')
        if len(data) >= 6:

            uid = data[5]

            if searchs_value in uid:
                phone = data[4]
                nik = data[6]
                first_name = data[2]
                name = data[2]

                print(f'''{COLOR_CODE["BLUE"]}
       {COLOR_CODE["RED"]}
                ID пользователя: {uid}
                телефон пользователя: {phone}
                Ник пользователя: {name}
                Первый ник пользователя: {first_name}
                Последний ник пользователя: {nik}
               


                      ''')
                found = True

    if not found:
        found = False

        with open(databasesh_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split('|')
            if len(data) >= 6:
                uid = data[5]
                if searchs_value in uid:
                    phone = data[4]
                    nik = data[6]
                    first_name = data[2]
                    name = data[2]

                    print(f'''{COLOR_CODE["BLUE"]}
               {COLOR_CODE["RED"]}
                        ID пользователя: {uid}
                        телефон пользователя: {phone}
                        Ник пользователя: {name}
                        Первый ник пользователя: {first_name}
                        Последний ник пользователя: {nik}



                              ''')
                    found = True
        if not found:
            found = False

            with open(databasesk_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                data = line.strip().split('|')
                if len(data) >= 6:
                    uid = data[5]
                    if searchs_value in uid:
                        phone = data[4]
                        nik = data[6]
                        first_name = data[2]
                        name = data[2]

                        print(f'''{COLOR_CODE["BLUE"]}
                   {COLOR_CODE["RED"]}
                            ID пользователя: {uid}
                            телефон пользователя: {phone}
                            Ник пользователя: {name}
                            Первый ник пользователя: {first_name}
                            Последний ник пользователя: {nik}



                                  ''')
                        found = True

        if not found:
            found = False

            with open(databasesl_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                data = line.strip().split('|')
                if len(data) >= 6:
                    uid = data[5]
                    if searchs_value in uid:
                        phone = data[4]
                        nik = data[6]
                        first_name = data[2]
                        name = data[2]

                        print(f'''{COLOR_CODE["BLUE"]}
                          {COLOR_CODE["RED"]}
                                   ID пользователя: {uid}
                                   телефон пользователя: {phone}
                                   Ник пользователя: {name}
                                   Первый ник пользователя: {first_name}
                                   Последний ник пользователя: {nik}



                                         ''')
                        found = True
        if not found:
            found = False

            with open(databasesm_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                data = line.strip().split('|')
                if len(data) >= 6:
                    uid = data[5]
                    if searchs_value in uid:
                        phone = data[4]
                        nik = data[6]
                        first_name = data[2]
                        name = data[2]

                        print(f'''{COLOR_CODE["BLUE"]}
                          {COLOR_CODE["RED"]}
                                   ID пользователя: {uid}
                                   телефон пользователя: {phone}
                                   Ник пользователя: {name}
                                   Первый ник пользователя: {first_name}
                                   Последний ник пользователя: {nik}



                                         ''')
                        found = True

        if not found:

            found = False

            with open(databasesk_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                data = line.strip().split('|')
                if len(data) >= 6:
                    uid = data[5]
                    if searchs_value in uid:
                        phone = data[4]
                        nik = data[6]
                        first_name = data[2]
                        name = data[2]

                        print(f'''{COLOR_CODE["BLUE"]}
                          {COLOR_CODE["RED"]}
                                   ID пользователя: {uid}
                                   телефон пользователя: {phone}
                                   Ник пользователя: {name}
                                   Первый ник пользователя: {first_name}
                                   Последний ник пользователя: {nik}



                                         ''')
                        found = True
        if not found:
            print(f'{COLOR_CODE["RED"]}[ERROR]Ничего не найдено в базе данных по номеру телефона.')




def bog(bog_file, searchs_value):
    found = False
    with open(bog_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()


    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 3:
            phone = data[0]
            if searchs_value in phone:
                user_id = data[3]
                nik = data[2]
                registration_date = data[1]
                print(f'''{COLOR_CODE["RED"]}

                 {COLOR_CODE["RED"]}
                 
                 АЙДИ: {phone}
                 ПЕРВЫЙ НИКНЕЙМ: {user_id}
                 НИКНЕЙМ: {nik}
                 ТЕЛЕФОН: {registration_date}

                    ''')
                found = True

    if not found:
        print("not base")



