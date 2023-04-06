import requests
import json
from bs4 import BeautifulSoup
from sys import stdin

# def get_page(url):
#     s = requests.Session()
#     response = s.get(url=url,headers= headers)
#     with open("index1.html","w") as file:
#         file.write(response.text)
#     soup = BeautifulSoup(response,"lxml")
    
# def main():
#   get_page(url="https://www.asics.com/gb/en-gb/gel-nimbus%E2%84%A2-25/p/1011B547-002.html")

# if __name__ == "__main__":
#     main()
#     # with open("index1.html","r") as file:
#     #     response = file.read()
#     # soup = BeautifulSoup(response,"lxml")
# url="https://www.asics.com/gb/en-gb/gel-nimbus%E2%84%A2-25-wide/p/1011B625-001.html"
# q = requests.get(url)
# res = q.content

# soup = BeautifulSoup(res,'lxml')
# ans  = soup.find_all("script")
def jsson_parser():
    count = 0
    d = dict()
    with open('/workspaces/Individual-HW/parsing/index.html', 'r') as file:
        flage = False
        with open('js.json','w+') as js:
            js.write('{\n'+'"'+
    "utag_data"+'"' +":" 
    +"{\n")
            for line in file:
                if "var utag_data = {" in line:
                    flage = True
                elif ("};" == line or count ==138):
                    flage = False
                    js.write("    }"+"\n"+"}")
                    break;
                elif (flage == True):
                    js.write(line)
                count+=1
with open('/workspaces/Individual-HW/js.json', 'r', encoding='utf-8') as f: #открыли файл
    text = json.load(f) #загнали все из файла в переменную
    print(text['utag_data']["forceSSL"]) 

        












# with open('/workspaces/Individual-HW/parsing/index.html', 'r') as fr:
#         lines = fr.readlines()
#         flage = False
#         for line in lines:
#             if "var utag_data = {" in line:
#                     flage = True
#             elif ("};" == line ):
#                     flage = False
#                     break;
#             elif (flage == True):
#                     print(line.replace(' ','').replace('"','').split(':'))
        
