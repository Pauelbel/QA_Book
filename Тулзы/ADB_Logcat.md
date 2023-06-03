* Качаем [SDK Platform Tools](https://developer.android.com/studio/releases/platform-tools) - это компонент Android SDK. включает adb, fastboot, и systrace.

#### Подключение устройства через Wi-Fi
1. На Аndroid - установить `ADB wireless by Henry` (покажет данные для подключения)
2. На ПК через командную строку перейти в корень скачанного `SDK Platform Tools`
3. Через командную строку (телефон должен быть подключен через кабель) прописать:
    - adb tcpip 5555
    - adb connect 192.168.1.202
    - adb devices - убедиться что подключен девайс
4. Можно отключить кабель и работать дальше

#### основные команды
- https://developer.android.com/tools/logcat

| <!-- -->                          | <!-- -->                                |
| --------------------------------- | --------------------------------------- |
| `adb logcat`                      | Открыть логи                            |
| `adb logcat -c`                   | - Очистить логи                         |
| `adb logcat -d -v time >.123.txt` | - Cохранить логи в папку platform-tools |
| `adb kill-server`                 | - Выключить сервер                      |
| `adb pull /data/anr/traces.txt`   | - ANR                                   |
|                                   |                                         |
- дернуть лог определенного приложения

| <!-- -->                     | <!-- -->                       |
| ---------------------------- | ------------------------------ |
| `adb shell pm list packages` | - Cписок установленных пакетов |
| `adb logcat \| find "name"`  | - Открыть лог приложения       |
|                              |                                |

