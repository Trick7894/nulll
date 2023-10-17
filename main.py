import os
import gdown
import requests
from banner import banner
from banner import baner1
from pystyle import *
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

def save_file_google_drive(link, filename):
    import gdown

    file = os.path.dirname(os.path.abspath(__file__))

    file = file + "/avto/" + filename
    gdown.download(link,file, quiet=False, fuzzy=True)


def save_file_from_google_drive(link, filename):
    import gdown

    file = os.path.dirname(os.path.abspath(__file__))

    file = file + "/src/" + filename
    gdown.download(link,file, quiet=False, fuzzy=True)

def save_from_google_drive(link, filename):
    import gdown

    file = os.path.dirname(os.path.abspath(__file__))

    file = file + "/tg/" + filename
    gdown.download(link,file, quiet=False, fuzzy=True)



print(Colors.blue,Center.XCenter(baner1))
print(Colorate.Vertical(Colors.blue_to_purple,Center.XCenter(banner)))
select = input(f'{COLOR_CODE["BLUE"]} Выбрать >{COLOR_CODE["RED"]} ')
if select == '1':
    from deanon import get_number
    from deanon import  tdat
    from deanon import  hdat
    from deanon import  dat
    from deanon import tele
    from deanon import meg
    from deanon import tyr
    from deanon import russ
    from deanon import getcont
    from deanon import bilane
    from deanon import getc
    from deanon import vk
    from deanon import vk1
    vk_file='vk//vk1.csv'
    vk1_file='vk//vk (1).txt'
    data_file = 'src//aliy.csv'
    datat_file="src//rit.csv"
    datar_file = "src//viм.csv"
    datah_file = "src//russkoe-slovo.ru_cleaned.csv"
    tele_file="src//tele2.csv"
    mega_file="src//ny.csv"
    tyr_file="src//tyr.sql.csv"
    russ_file="src//772.csv"
    bilane_file='src//Beeline2019.csv'
    bilane2_file='src//Beeline2019.002.csv'
    bilane3_file='src//Beeline2019.003.csv'
    bilane4_file = 'src//Beeline2019.004.csv'
    bilane5_file = 'src//Beeline2019.005.csv'
    getc_file='src//Get1.csv'
    getc1_file='src//Get2.csv'
    getc2_file='src//Get3.csv'
    getcon_file = "src//Getcontact .csv"

    search_value =input(f'{COLOR_CODE["RED"]}Введите номер телефона:')
    search_value = search_value[1:]
    vk1(vk1_file,search_value)
    get_number(data_file, search_value)
    tdat(datat_file,search_value)
    hdat(datah_file,search_value)
    dat(datar_file,search_value)
    meg(mega_file,search_value)
    tele(tele_file,search_value)
    tyr(tyr_file,search_value)
    russ(russ_file,search_value)
    vk(vk_file,search_value)
    getcont(getcon_file,search_value)
    getc(getc_file,getc1_file,getc2_file,search_value)
    bilane(bilane_file, bilane2_file, bilane3_file, bilane4_file, bilane5_file, search_value)
elif select == '2':
      print("не доступно")
elif select == '3':
    from get_ip import get_ip
    get_ip()
elif select =='4':
    from ddos import get_link
    from ddos import get_content
    print("Ctrl + z stop atack")
    lin = input(str('Link: '))
    get_link(lin)
    get_content(link)
elif select == '5':
    from iddeanon import get_tg
    from iddeanon import bog
    databases_file = 'tg//csv.fixed.001.csv'
    databasesh_file="tg//csv.fixed.002.csv"
    databasesk_file="tg//csv.fixed.003.csv"
    databasesl_file='tg//csv.fixed.004.csv'
    databasesm_file='tg//csv.fixed.005.csv'
    bog_file='tg//id.csv'
    searchs_value = input(f'{COLOR_CODE["RED"]}Введите id:')
    get_tg(databases_file, databasesh_file,databasesk_file,databasesl_file,databasesm_file, searchs_value)
    bog(bog_file,searchs_value)


elif select =='6':
      from indeanon import get_in
      databased_file='number2.csv'
      searchd_value = input(f'{COLOR_CODE["RED"]}Введите instagram:')
      get_in( databased_file, searchd_value )
elif select == '8':
        from phio import phi
        phio_file="avto//10.csv"
        phio1_file="avto//1.csv"
        phio2_file="avto//2.csv"
        phio3_file="avto//3.csv"
        phio4_file="avto//4.csv"
        phio5_file="avto//5.csv"
        phio6_file="avto//6.csv"
        phio7_file="avto//7.csv"
        phio8_file="avto//8.csv"
        phio9_file="avto//9.csv"


        search_value = input(f'{COLOR_CODE["RED"]}Введите ФИО:')
        phi(phio_file,phio1_file,phio2_file,phio3_file,phio4_file,phio5_file,phio6_file,phio7_file,phio8_file,
        phio9_file,search_value)

elif select == '9':
         print(f'''
                                  Base
                  ______________________________________
                  +    b-bilane               base5    +
                  +    g-getcontact           base6    +
                  +    base1                  base7    +
                  +    tele2                  base8    +
                  +    avto                   base9    + 
                  +    tg                     base10   + 
                  +____________________________________+ 
                       
                          ''')
         search_value = input(f'{COLOR_CODE["RED"]}Введите ФИО:')

         try:
            if search_value=='b':
                save_file_from_google_drive('https://drive.google.com/file/d/1hYcwD0BYqu1R0LJZ2iHwPsZr1g9DvRnb/view?usp=sharing', 'Beeline2019.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1YYQ99jX1u16tkxx8jGkIsdr68QPSDgF0/view?usp=sharing','Beeline2019.002.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/18lfP9nOWDfaHDBfcbnpi5mVhc8sFUjUU/view?usp=sharing','Beeline2019.003.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1knDJi7y_W55cW4D7JLhzKZuBCucQQPUF/view?usp=sharing','Beeline2019.004.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1jxhiGnF4rD64R_Gwj1saX_vCOqP7UOdc/view?usp=sharing','Beeline2019.005.csv')
         except:
           print("ERROR")
         try:
            if search_value=='g':
                save_file_from_google_drive('https://drive.google.com/file/d/1YBTJqibhavl50EnReyUlMl3dQJ0JCKq5/view?usp=sharing', 'Get1.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/13L8uq0RxriK7v9wbpbtAUAFSXoxix8by/view?usp=sharing','Get2.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1YANpC9jrQzCQ6B2EA3ExrfKgC6cYSmjl/view?usp=sharing','Get3.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1rMrfs2UeYq4F5mizZ3XYJX4Gzpf3Vurt/view?usp=sharing','Getcontact .csv')
         except:
           print("ERROR")
         try:
            if search_value=='base1':
                save_file_from_google_drive('https://drive.google.com/file/d/1B2qdnCN4juTt2-GwZsvyGnnqxNLxzJIM/view?usp=sharing', 'ny.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1uY8i_uwXwruDGN6KuNdRKm6UQj_S-OuU/view?usp=sharing',' tyr.sql.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1mG9pbuLWR8uiHOy5pr07bSqWkpBxX5pN/view?usp=sharing','rit.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1WXU9CMvnTV8xXnQdf0sFkEakYTXc768C/view?usp=sharing','viм.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1G6vrfgt8c36F-Bw3S376sVoquR6Gl4iw/view?usp=sharing','772.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1uaXey-fzVTRqwbgMNNZpVCx0tZ_HczL-/view?usp=sharing','aliy.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1YMRlYlVwO2ZdqyY6AtZ38QECkYhMg6tn/view?usp=sharing','russkoe-slovo.ru_cleaned.csv')
         except:
           print("ERROR")
         try:
            if search_value=='tele2':
                save_file_from_google_drive('https://drive.google.com/file/d/1-bkQ3Zpr8xXXI4I8r2FV0-Qsq8ABgq6i/view?usp=sharing', 'tele2.csv')
         except:
           print("ERROR")
         try:
               if search_value == 'avto':
                   save_file_google_drive('https://drive.google.com/file/d/1fsGyAProjYdYSVqGRUUr76Z0FH7enkXL/view?usp=sharing','1.csv')
                   save_file_google_drive('https://drive.google.com/file/d/1nUul756egX8EdTqI88imv32ltKJdlTIl/view?usp=sharing','2.csv')
                   save_file_google_drive('https://drive.google.com/file/d/1mVc7PczEkTb2NBt1QQC8lRoN6tlmOAVN/view?usp=sharing','3.csv')
                   save_file_google_drive('https://drive.google.com/file/d/1MOJLUELxehW47JOItXBmslVpTdufi-Aq/view?usp=sharing','4.csv')
                   save_file_google_drive('https://drive.google.com/file/d/1VE3GxFZRqDqGhMT7MO_gKdVB0saqgucj/view?usp=sharing','5.csv')
                   save_file_google_drive('https://drive.google.com/file/d/1yJPm0xkjfGJFtnWo-ptXTwrXFE5M55x2/view?usp=sharing','6.csv')
                   save_file_google_drive('https://drive.google.com/file/d/1Il4eWm1rZQ_E1nK9EoGfN11uf_msyZN7/view?usp=sharing','7.csv')
                   save_file_google_drive('https://drive.google.com/file/d/1ZdnzBeO2QMvXAxHFTNn7ZdexP0VbdvJH/view?usp=sharing','8.csv')
                   save_file_google_drive('https://drive.google.com/file/d/1T5S6B6j_JbNyc2EaZoA0t8UWkI8hBwEf/view?usp=sharing','9.csv')
                   save_file_google_drive('https://drive.google.com/file/d/1JsmGwrmzePqs8K0-2yFTFN6GSUZUykm0/view?usp=sharing','10.csv')
         except:
             print("ERROR")
         try:
             if search_value == 'tg':
                save_from_google_drive('https://drive.google.com/file/d/1vTzYRJoMq8t1KcvPHnMPfs3Xdl2DLUZg/view?usp=sharing','id.csv')
                save_from_google_drive('https://drive.google.com/file/d/14ALpgj5VdvMOv1RiciygolQrA_cmILCU/view?usp=sharing','csv.fixed.001.csv')
                save_from_google_drive('https://drive.google.com/file/d/1h9WFhPE45wxsu38NNMJe8W3Jd7XQFGbv/view?usp=sharing','csv.fixed.002.csv')
                save_from_google_drive('https://drive.google.com/file/d/1KCvvmwbNBz5R0gN2580Sv2_QZKpmsopL/view?usp=sharing','csv.fixed.003.csv')
                save_from_google_drive('https://drive.google.com/file/d/1KlwLs7t13WQKM_3akjGf4O5wPTO59fZY/view?usp=sharing','csv.fixed.004.csv')
                save_from_google_drive('https://drive.google.com/file/d/1ahER0qnQR4sakNciIpL7zvzoDYnAQOZm/view?usp=sharing','csv.fixed.005.csv')
         except:
            print("ERROR")
elif select =='N':
    exit


