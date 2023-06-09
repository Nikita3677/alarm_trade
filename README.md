# alarm_trade

### Описание
Программа, которая следит за ценой интересующего фьючерса с биржи Binance. В случае, если цена за последний час изменится более, чем на 1%, то в консоль выводится сообщение. При этом программа остановится на минуту и продолжит свою работу, постоянно считывая актуальную цену.  

### Переменные окружения 
Для безопасности, api_key и secret_key хранятся в переменных окружения.  
  Для того, чтобы использовать переменные окружения, нужно:
  - создать файл с расширением .env в корневом каталоге 
  - добавить в созданный файл секретные данные в формате Ключ='Значение'

### Технологии
- Python 3.9
- Python-binance
- Python-dotenv

### Как запустить программу
- Клонируйте репозиторий и перейдите в него
```
git clone <тут ссылка>
``` 
- Установите и активируйте виртуальное окружение
```
python -m venv venv
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Запуск программы
```
python main.py
```
