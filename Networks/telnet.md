**Telnet** ( **TELNET** ) предназначен для взаимодействия терминалов

- Используется для удаленного администрирования

##### Как пользоваться

`sudo apt install telnet`

`telnet {опции} {хост} {порт}`

* -4 – использовать поддержку стандарта IPv4;
* -6 – использовать поддержку стандарта IPv6;
* -8 – использовать 8-битную кодировку – например, Unicode;
* -E – отключить поддержку Escape-последовательностей;
* -a – автоматический вход с логином из переменного окружения USER;
* -b – использовать локальный сокет;
* -d – использовать режим отладки;
* -p – использовать эмуляцию rlogin;
* -l – указать пользователя авторизации.

##### После подключения к удаленной машине 2 режима работы

1. **Построчный** – строка полностью редактируется на локальном компьютере и в готовом виде целиком отправляется на сервер.

2. **Посимвольный** – каждый символ, который вы набираете, отправляется на сервер. В этом случае не получится что-то исправить, если вы допустите ошибку при вводе.

###### Основные команды после подключения

* CLOSE – отключить соединение с удаленным сервером;
* ENCRYPT – передавать всю информацию в зашифрованном виде;
* LOGOUT – выйти и закрыть соединение;
* MODE – переключить режима со строчного на символьный или наоборот;
* STATUS – показать текущий статус соединения;
* SEND – отправить один из специальных символов telnet;
* SET – установить значение параметра;
* OPEN – открыть соединение с удаленным сервером;
* DISPLAY – показать используемые спецсимволы;
* SLC – изменить используемые спецсимволы.
