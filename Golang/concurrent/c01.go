package main

import (
	"fmt"
)

func cetak() {
	var id int
	id = 1
	fmt.Printf("cetak: %d\n", id)
}

func main() {
	fmt.Println("Concurrent 1")
	go cetak()

	// supaya function conccurent terlihat
	fmt.Scanln()
}
