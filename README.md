<<<<<<< HEAD
опыты с batfish

два файла batfish.py и req.txt Скачиваем docker контейнер для batfish: 
docker run --name batfish -v batfish-data:/data -p 8889:8888 -p 9997:9997 -p 9996:9996 batfish/allinone

Устанавливаем batfish в virtualen и добавляем зависимости из файла req.txt:
python3.8 -m venv BATFISH pip install -r ../../req.txt

Файл для конфигов '/home/yzhi/#SHARA/configs' - поставить свою и в нее залить конфиги
=======
# -batfish_yzhi
опыты с batfish

два файла batfish.py и req.txt
Скачиваем docker контейнер для batfish:
    docker run --name batfish -v batfish-data:/data -p 8889:8888 -p 9997:9997 -p 9996:9996 batfish/allinone

Устанавливаем batfish в virtualen и добавляем зависимости из файла req.txt:
    python3.8 -m venv BATFISH
    pip install -r ../../req.txt

Файл для конфигов '/home/yzhi/#SHARA/configs'
>>>>>>> 892c7ac01dd270001f2fa6e06712d19347254f36
