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
}
def get_number(data_file, search_value):
    found = False

    with open(data_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 10:
            phone = data[2]
            if search_value in phone:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                birthday = data[5]


                print(f'''{COLOR_CODE["RED"]}

                {COLOR_CODE["RED"]}
                  ФИО пользователя: {user_id}
                  Дата рождения: {registration_date}
                  Город: {last_name}
                  Работа: {birthday}
                  ТЕЛЕФОН: {phone}
        
                      ''')
                found = True
    if not found: print("not base")

def vk1(vk1_file, search_value):
    found = False

    with open(vk1_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 3:
            phone = data[1]
            if search_value in phone:
                user_id = data[0]
                registration_date = data[2]
                print(f'''{COLOR_CODE["RED"]}

                 {COLOR_CODE["RED"]}
                 VK пользователя : {user_id}
                 ФИО пользователя: {registration_date}
                 ТЕЛЕФОН: {phone}

                    ''')
                found = True

    if not found:
        print("not base")

def tdat(datat_file, search_value):
    found = False

    with open(datat_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 3:
            phone = data[1]
            if search_value in phone:
                user_id = data[0]
                registration_date = data[2]
                print(f'''{COLOR_CODE["RED"]}

                 {COLOR_CODE["RED"]}
                 ФИО пользователя: {user_id}
                 Почта пользователя: {registration_date}
                 ТЕЛЕФОН: {phone}

                    ''')
                found = True

    if not found:
        print("not base")


def hdat(datah_file,search_value):
                    found = False

                    with open(datah_file, 'r', encoding='utf-8') as file:
                        lines = file.readlines()

                    for line in lines:
                        data = line.strip().split('|')
                        if len(data) >= 4:
                            phone = data[1]
                            if search_value in phone:
                                user_id = data[0]
                                registration_date = data[2]
                                last_name = data[3]
                                birthday = data[4]

                                print(f'''{COLOR_CODE["RED"]}

                                 {COLOR_CODE["RED"]}
                                 ФИО пользователя: {user_id}
                                 Почта пользователя: {registration_date}
                                 Город: {last_name}
                                 Адрес: {birthday}
                                 ТЕЛЕФОН: {phone}

                                                         ''')
                                found = True

                    if not found:
                     print("not base")

def dat(datar_file,search_value):
    found = False

    with open(datar_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 5:
            phone = data[5]
            if search_value in phone:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                birthday = data[6]

                print(f'''{COLOR_CODE["RED"]}

                                   {COLOR_CODE["RED"]}
                                     ФИО пользователя: {user_id}
                                     Дата рождения: {registration_date}
                                     Город: {last_name}
                                     Работа: {birthday}
                                     ТЕЛЕФОН: {phone}

                                         ''')
                found = True

    if not found:



        print("not base")

def tele(tele_file, search_value):
    found = False

    with open(tele_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 3:
            phone = data[2]
            if search_value in phone:
                user_id = data[1]
                registration_date = data[0]
                print(f'''{COLOR_CODE["RED"]}

                 {COLOR_CODE["RED"]}
                 ФИО пользователя: {user_id}
                 Почта пользователя: {registration_date}
                 ТЕЛЕФОН: {phone}

                    ''')
                found = True

    if not found:
        print("not base")


def tyr(tyr_file, search_value):
    found = False

    with open(tyr_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 3:
            phone = data[9]
            if search_value in phone:
                user_id = data[3]
                nam=data[4]
                registration_date = data[2]
                last_name = data[7]
                birthday = data[6]
                birthd=data[5]
                ytu=data[8]
                print(f'''{COLOR_CODE["RED"]}

                 {COLOR_CODE["RED"]}
                 ФИО пользователя: {registration_date + user_id + nam}
                 Серия пасопорта: {user_id}
                 ТЕЛЕФОН: {phone}
                 Адрес нас пункт: {birthd}
                 Улица: {birthday}
                 Дом: {last_name}
                 Квартира: {ytu}

                    ''')
                found = True

    if not found:
        print("not base")

def russ(russ_file, search_value):
    found = False
    with open(russ_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()


    for line in lines:
        data = line.strip().split('|""')
        if len(data) >= 3:
            phone = data[2]
            if search_value in phone:
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


def meg(mega_file, search_value):
    found = False

    with open(mega_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 3:
            phone = data[0]
            if search_value in phone:
                user_id = data[1]
                registration_date = data[2]
                last_name = data[7]
                birthday = data[6]
                birthd=data[5]
                ytu=data[8]
                print(f'''{COLOR_CODE["RED"]}

                 {COLOR_CODE["RED"]}
                 ФИО пользователя: {user_id}
                 Серия пасопорта: {registration_date}
                 ТЕЛЕФОН: {phone}
                 Адрес нас пункт: {birthd}
                 Улица: {birthday}
                 Дом: {last_name}
                 Квартира: {ytu}

                    ''')
                found = True

    if not found:
        print("not base")

def getcont(getcon_file, search_value):
    found = False

    with open(getcon_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 4:
            phone = data[0]
            if search_value in phone:
                num = data[1]
                getc = data[2]

                fa = data[7]
                b = data[6]
                a=data[5]
                y=data[8]
                ta = data[9]
                g= data[10]
                l = data[11]
                k = data[12]
                n = data[13]
                u = data[14]
                d = data[15]
                t = data[16]
                h = data[17]
                p = data[18]
                s =data[19]
                z =data[20]
                f = data[21]
                r = data[22]
                i = data[23]
                m = data[24]
                x=data[25]
                v=data[26]
                fah = data[27]
                bh = data[28]
                ah = data[29]
                yh = data[30]

                tah = data[31]
                gh = data[32]
                lh = data[33]
                kh = data[34]
                nh = data[35]
                uh = data[36]


                print(f'''{COLOR_CODE["RED"]}

                 {COLOR_CODE["RED"]}
                 ФИО пользователя: {num}
                 Серия пасопорта: {getc}
                 ТЕЛЕФОН: {phone}
                 Адрес нас пункт: {b+l+a+g+f+fa+m+v+x+i+r+z+s+p+h+t+d+u+n+k+y+ta+bh+lh+ah+gh
                                   +fah+uh+nh+kh+yh+tah
                }


                    ''')
                found = True


    if not found:
        print("not base")



def bilane(bilane_file,bilane2_file,bilane3_file,bilane4_file,bilane5_file,search_value):
    found = False

    with open(bilane_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|')
        if len(data) >= 14:
            phone = data[14]

            if search_value in phone:
                gor=[2]
                registration_date = data[2]
                birthday = data[3]
                uset = data[4]
                user_id = data[9]
                Kom=data[10]
                phio=data[13]

                print(f'''{COLOR_CODE["RED"]}

                 {COLOR_CODE["RED"]}
                 ФИО пользователя: { phio}
                 Серия пасопорта: {registration_date}
                 ТЕЛЕФОН: {phone}
                 GOrod: {gor}
                 RAuon:{registration_date}
                 Улица: {birthday}
                 Дом: {uset}
                 Квартира: {user_id}
                 KOmnata:{Kom}

                    ''')
                found = True

    if not found:
        found = False

        with open(bilane2_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split('|')
            if len(data) >= 14:
                phone = data[14]

                if search_value in phone:
                    gor = [2]
                    registration_date = data[2]
                    birthday = data[3]
                    uset = data[4]
                    user_id = data[9]
                    Kom = data[10]
                    phio = data[13]

                    print(f'''{COLOR_CODE["RED"]}

                         {COLOR_CODE["RED"]}
                         ФИО пользователя: {phio}
                         Серия пасопорта: {registration_date}
                         ТЕЛЕФОН: {phone}
                         GOrod: {gor}
                         RAuon:{registration_date}
                         Улица: {birthday}
                         Дом: {uset}
                         Квартира: {user_id}
                         KOmnata:{Kom}

                            ''')
                    found = True

        if not found:
            found = False

            with open(bilane3_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                data = line.strip().split('|')
                if len(data) >= 14:
                    phone = data[14]

                    if search_value in phone:
                        gor = [1]
                        registration_date = data[2]
                        birthday = data[3]
                        uset = data[4]
                        user_id = data[9]
                        Kom = data[10]
                        phio = data[13]

                        print(f'''{COLOR_CODE["RED"]}

                             {COLOR_CODE["RED"]}
                             ФИО пользователя: {phio}
                             Серия пасопорта: {registration_date}
                             ТЕЛЕФОН: {phone}
                             GOrod: {gor}
                             RAuon:{registration_date}
                             Улица: {birthday}
                             Дом: {uset}
                             Квартира: {user_id}
                             KOmnata:{Kom}

                                ''')
                        found = True

            if not found:
                found = False

                with open(bilane4_file, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                for line in lines:
                    data = line.strip().split('|')
                    if len(data) >= 14:
                        phone = data[14]

                        if search_value in phone:
                            gor = [1]
                            registration_date = data[2]
                            birthday = data[3]
                            uset = data[4]
                            user_id = data[9]
                            Kom = data[10]
                            phio = data[13]

                            print(f'''{COLOR_CODE["RED"]}

                                 {COLOR_CODE["RED"]}
                                 ФИО пользователя: {phio}
                                 Серия пасопорта: {registration_date}
                                 ТЕЛЕФОН: {phone}
                                 GOrod: {gor}
                                 RAuon:{registration_date}
                                 Улица: {birthday}
                                 Дом: {uset}
                                 Квартира: {user_id}
                                 KOmnata:{Kom}

                                    ''')
                            found = True

                if not found:
                    found = False

                    with open(bilane5_file, 'r', encoding='utf-8') as file:
                        lines = file.readlines()

                    for line in lines:
                        data = line.strip().split('|')
                        if len(data) >= 14:
                            phone = data[14]

                            if search_value in phone:
                                gor = [1]
                                registration_date = data[2]
                                birthday = data[3]
                                uset = data[4]
                                user_id = data[9]
                                Kom = data[10]
                                phio = data[13]

                                print(f'''{COLOR_CODE["RED"]}

                                     {COLOR_CODE["RED"]}
                                     ФИО пользователя: {phio}
                                     Серия пасопорта: {registration_date}
                                     ТЕЛЕФОН: {phone}
                                     GOrod: {gor}
                                     RAuon:{registration_date}
                                     Улица: {birthday}
                                     Дом: {uset}
                                     Квартира: {user_id}
                                     KOmnata:{Kom}

                                        ''')
                                found = True

                    if not found:
                        print("not")


def getc(getc_file,getc1_file,getc2_file, search_value):
    found = False

    with open(getc_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|')
        if len(data) >= 2:
            phone = data[0]
            if search_value in phone:
                registration_date = data[1]

                print(f'''{COLOR_CODE["RED"]}

                 {COLOR_CODE["RED"]}
                 ФИО: {phone}
                 ИНформация: {registration_date}

                    ''')
                found = True

    if not found:
        found = False

        with open(getc1_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split('|')
            if len(data) >= 2:
                phone = data[0]
                if search_value in phone:
                    registration_date = data[1]

                    print(f'''{COLOR_CODE["RED"]}

                         {COLOR_CODE["RED"]}
                         ФИО: {phone}
                         ИНформация: {registration_date}

                            ''')
                    found = True

        if not found:
            found = False

            with open(getc2_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                data = line.strip().split('|')
                if len(data) >= 2:
                    phone = data[0]
                    if search_value in phone:

                        registration_date = data[1]

                        print(f'''{COLOR_CODE["RED"]}

                             {COLOR_CODE["RED"]}
                             ФИО: {phone}
                             ИНформация: {registration_date}

                                ''')
                        found = True

            if not found:
                print("Not base")

def vk(vk_file, search_value):
                    found = False

                    with open(vk_file, 'r', encoding='utf-8') as file:
                        lines = file.readlines()

                    for line in lines:
                        data = line.strip().split(';')
                        if len(data) >= 10:
                            phone = data[10]
                            if search_value in phone:
                                user_id = data[0]
                                name=data[3]
                                age=data[6]
                                sity=data[8]
                                registration_date = data[2]
                                print(f'''{COLOR_CODE["RED"]}

                                 {COLOR_CODE["RED"]}
                                 VK пользователя : {user_id}
                                 ФИО пользователя: {registration_date + name}
                                 Взраст: {age}
                                 Город: {sity}
                                 ТЕЛЕФОН: {phone}

                                    ''')
                                found = True

                    if not found:
                        print("not base")
