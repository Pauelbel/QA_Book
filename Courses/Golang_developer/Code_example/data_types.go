package main

import (
	"fmt"
)

var storage = make(map[string]string)

type User struct {
	Name     string //будет видна во внешних пакетах
	password string //видна не будет
}

func main() {
	fmt.Print("Hello world")
}

// числовые функции

func int_0() int {
	return 13 //Всегда должна вернуть число
}

func int_1() {
	var i int = 13
	r := i
	fmt.Print(r)
}
