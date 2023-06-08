#### Ускорить пакетный менеджер
sudo nano /etc/dnf/dnf.conf
  
  fastestmirror=True
  max_parallel_downloads=10
  defaultyes=True


sudo dnf repolist - посмотреть список подключенных репозиториев
