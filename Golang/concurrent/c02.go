package main

import (
	"fmt"
)

func cetak(terima chan int) {
	var x int
	x = <-terima
	fmt.Printf("terima: %d\n", x)
}

func main() {
	fmt.Println("Concurrent 2")

	kirim := make(chan int)
	go cetak(kirim)
	kirim <- 7

	// supaya function conccurent terlihat
	fmt.Printf("Tekan Enter untuk selasai ")
	fmt.Scanln()
}
