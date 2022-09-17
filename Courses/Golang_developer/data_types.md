
# Типы данных 

- Целые - ```int, uint, int8, uint8, ...```
    - Значение "по умолчанию" - 0
    - Типы int и uint могут занимать 32 и 64 бита на разных платформах
    - Нет автоматического преобразования типов
    - uintptr - целое число, не указатель
- Аалиасы к целым числам - ```byte = uint8, rune = int32```
- Плавающие - ```float32, float64```
- Комплексные - ```complex64, complex128```
- Строки - ```string```
- Указатели - ```uintptr, *int, *string, ...``` 

## Операции над типами данных

```
+ -sum        - integers, floats, complex values, strings
­- -difference - integers, floats, complex values
* -product    - integers, floats, complex values
/ -quotient   - integers, floats, complex values
% -remainder  - integers


& -bitwise AND - integers
| -bitwise OR  - integers
^ -bitwise XOR - integers
&^ -bit clear (AND NOT) - integers

<< -left shift  - integer << unsigned integer
>> -right shift - integer >> unsigned integer
```

## Строки
```
s := "hello world"       // создавать
var c byte = s[0]        // получать доступ к байту(!) в строке
var s2 string = s[5:10]  // получать подстроку (в байтах!)
s2 := s + " again"       // склеивать
l := len(s)              // узнавать длину в байтах
```
