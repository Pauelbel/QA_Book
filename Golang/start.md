## Установка (fedora)

- ```$ sudo dnf install golang```
- ```$ mkdir -p $HOME/go```
- ```$ echo 'export GOPATH=$HOME/go' >> $HOME/.bashrc```
- ```$ source $HOME/.bashrc```
- ```$ go env GOPATH``` 

Посмотреть переменные окружения 
- ```$ go env```
    - **GOROOT** - путь к дистрибутиву go

****
## скачивание и установка пакетов 
- ```$ go get -d github.com/...``` - скачивается в ```/home/user/go/src```
    -  ... - включая  все дочерние пакеты
    - -d - только скачивание (без параметра пакет установится)
- ```go install github.com/...``` - копилируется и устанавливается в 
    - ```home/user/go/pkg``` - сами библиотеки
    - ```home/user/go/bin``` - исполняемый файл
****

## GO модули 

- ```go mod init github.com/путь```
> При скачивании пакетов они попадут в ```home/user/go/pkg/mod```
