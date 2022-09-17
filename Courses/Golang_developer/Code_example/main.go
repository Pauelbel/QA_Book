package main //Основной пкет, к нему подключаются все остальные

import (
	"fmt"
	"reflect"
)

func main() {
	test := "строковая переменная"
	var test_1 string = "строковая переменная" //Можно использовать без string
	const test_2 string = "константа"          //Ее нельзя переопределить

	fmt.Println(test)
	fmt.Println(test_1)
	fmt.Println(test_2)

	fmt.Println(reflect.TypeOf(test)) //Посмотреть тип переменной
}
