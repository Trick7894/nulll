import socket
import requests
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

def get_ip():
    ip = input(f'{COLOR_CODE["RED"]}IP:' )

    try:
        ip = socket.gethostbyname(ip)
        
        infoList1 = requests.get(f"http://ipwho.is/{ip}")
        infoList = infoList1.json()
        
        if infoList.get("success"):
            print(f'{COLOR_CODE["RED"]}\n')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} Айпи адресс:{COLOR_CODE["RED"]}  {infoList["ip"]}')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} Успех:{COLOR_CODE["RED"]}  {infoList["success"]}  ')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} Тип:{COLOR_CODE["RED"]}   {infoList["type"]}     ')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} Континент:{COLOR_CODE["RED"]}   {infoList["continent"]}')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} Страна:{COLOR_CODE["RED"]}   {infoList["country"]}')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} Регион:{COLOR_CODE["RED"]}   {infoList["region"]}')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} Город:{COLOR_CODE["RED"]}   {infoList["city"]}')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} Почтовый код:{COLOR_CODE["RED"]}   {infoList["postal"]}')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} Столица:{COLOR_CODE["RED"]}  {infoList["capital"]}\n')
            print(f'{COLOR_CODE["RED"]}\n')

            
        else:
            print(f'{COLOR_CODE["RED"]}\n')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} IP:{COLOR_CODE["RED"]}  {infoList["ip"]}')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} Success:{COLOR_CODE["RED"]}   {infoList["success"]}')
            print(f'     {COLOR_CODE["RED"]}{COLOR_CODE["RED"]} Message:{COLOR_CODE["RED"]}  {infoList["message"]}')
            print(f'{COLOR_CODE["RED"]}\n')
    except Exception as e:
        print(f'An error occurred: {e}')



