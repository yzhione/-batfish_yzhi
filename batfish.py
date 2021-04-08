#! source /home/yzhi/OKRUZHENIE/BYTFISH/BATFISH_IPY/bin/activate python3.8
"""
два файла batfish.py и req.txt
Скачиваем docker контейнер для batfish:
    docker run --name batfish -v batfish-data:/data -p 8889:8888 -p 9997:9997 -p 9996:9996 batfish/allinone

Устанавливаем batfish в virtualen и добавляем зависимости из файла req.txt:
    python3.8 -m venv BATFISH
    pip install -r ../../req.txt 

Файл для конфигов '/home/yzhi/#SHARA/configs'
"""
import pandas as pd
from pybatfish.client.commands import *
from pybatfish.datamodel import *
from pybatfish.datamodel.answer import *
from pybatfish.datamodel.flow import *
from pybatfish.question import *
from pybatfish.question import bfq
# import threading


# Запрос имени снапшота
SNAPSHOT_NAME = input('Введи имя снапшота: ')

#имя выходного файла
file_excel_name = f"{SNAPSHOT_NAME}.xlsx"

# Локальный сервер
bf_session.host = 'localhost'
# Имя сети по деволту
bf_set_network('example_dc')

#Место с конфигами
SNAPSHOT_DIR = '/home/yzhi/#SHARA/configs'
bf_init_snapshot(SNAPSHOT_DIR, name=SNAPSHOT_NAME, overwrite=True)

# Задаем параметры для Батфиш
bf_set_network('example_dc')
bf_set_snapshot(SNAPSHOT_NAME)

# загрузка вопросов - тестов
load_questions()

"""
# Создание файла в конфигурации, если его нету
with open(file_excel_name, mode='w') as create_exel_file:
    #create_exel_file.write('')
    print(f'Файл {file_excel_name} создан \n')
"""    
#######################################################
#######################################################

#запись вывода в excel
def zapis_v_excel(data_frame_source,file_excel_name=file_excel_name, listname=SNAPSHOT_NAME,zapis='a',**kwr):
    """ Функция принимает data_frame_source - как DataFrame и 
        записывает в exel файл с именем file_excel_name, который по умолчанию равен file_excel_name
        по умолчанию имя листа == SNAPSHOT_NAME"""
    with pd.ExcelWriter(file_excel_name, mode=zapis) as writer:
        data_frame_source.to_excel(writer, sheet_name=listname)
    return None

#######################################################
#######################################################
# Функции разбора batfish

#разбор проблемы с парсингом в Batfish == пойдет, начальный
def razbor_initIssues():
    vyvod = bfq.initIssues().answer().frame()
    return vyvod

#разбираем ACL в Batfish
def razbor_acl():
    vyvod = bfq.filterLineReachability().answer().frame()
    return vyvod

#разбор IP owner  в Batfish
def razbor_ipowner():
    vyvod = bfq.ipOwners().answer().frame()
    return vyvod

#разбор VLANS  в Batfish, неочень на транках --
def razbor_vlans():
    vyvod = bfq.switchedVlanProperties().answer().frame()
    return vyvod

#разбор L3edge  в Batfish
def razbor_l3edge():
    vyvod = bfq.layer3Edges().answer().frame()
    return vyvod

#разбор routing_bgp  в Batfish
def razbor_routing_bgp():
    vyvod = bfq.bgpSessionCompatibility().answer().frame()
    return vyvod

#разбор loopdetect  в Batfish == ничего
def razbor_loopdetect():
    vyvod = bfq.detectLoops().answer().frame()
    return vyvod

#разбор multipath в Batfish == ничего
def razbor_multipath():
    vyvod = bfq.subnetMultipathConsistency().answer().frame()
    return vyvod

#разбор ipsecSessionStatus в Batfish == мало инфы
def razbor_ipsecSession():
    vyvod = bfq.ipsecSessionStatus().answer().frame()
    return vyvod


if __name__ == '__main__':
    print(f"Mesto s konfigoq: {SNAPSHOT_DIR} \nImya snapshota: {SNAPSHOT_NAME}""")
    #создаем таблицу
    data_frame_razbor_initIssues = razbor_initIssues() # определеяем какую функцию будем использовать
    zapis_v_excel(data_frame_source=data_frame_razbor_initIssues, listname="initIssues", zapis='w')
    # добавляем в таблицу данные
    data_frame_razbor_acl = razbor_acl() # определеяем какую функцию будем использовать
    data_frame_razbor_ipowner = razbor_ipowner() # определеяем какую функцию будем использовать
    data_frame_razbor_vlans = razbor_vlans() # определеяем какую функцию будем использовать
    data_frame_razbor_l3edge = razbor_l3edge() # определеяем какую функцию будем использовать
    data_frame_razbor_routing_bgp = razbor_routing_bgp() # определеяем какую функцию будем использовать
    data_frame_razbor_loopdetect = razbor_loopdetect() # определеяем какую функцию будем использовать
    data_frame_razbor_multipath = razbor_multipath() # определеяем какую функцию будем использовать
    data_frame_razbor_ipsecSession = razbor_ipsecSession() # определеяем какую функцию будем использовать
  
    zapis_v_excel(data_frame_source=data_frame_razbor_vlans, listname="VLANS")
    zapis_v_excel(data_frame_source=data_frame_razbor_l3edge, listname="l3edge")
    zapis_v_excel(data_frame_source=data_frame_razbor_acl, listname="ACL")
    zapis_v_excel(data_frame_source=data_frame_razbor_routing_bgp, listname="routing_bgp")
    zapis_v_excel(data_frame_source=data_frame_razbor_ipowner, listname="IP_ADDR")
    zapis_v_excel(data_frame_source=data_frame_razbor_loopdetect, listname="loopdetect")
    zapis_v_excel(data_frame_source=data_frame_razbor_multipath, listname="multipath")
    zapis_v_excel(data_frame_source=data_frame_razbor_ipsecSession, listname="ipsecSession")
 # Мультипоточность, потом может допишу
    """    
      for i in range(4):
          my_thread = threading.Thread(target=doubler, args=(i,))
          my_thread.start()
          my_thread.join()
    """
 
 