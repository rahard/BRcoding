package main

import (
	"fmt"
)

func cetak(terima chan int) {
	var x int
	for {
		x = <-terima
		fmt.Printf("cetak terima: %d\n", x)
	}
}

func dengar(terima chan int) {
	var x int
	for {
		x = <-terima
		fmt.Printf("dengar terima: %d\n", x)
	}
}

func main() {
	fmt.Println("Concurrent 3")
	// ada dua fungsi yang mendengarkan
	// apa yang terjadi?

	kirim := make(chan int)
	go cetak(kirim)
	go dengar(kirim)

	for i := 0; i < 10; i++ {
		kirim <- i
	}

	// supaya function conccurent terlihat
	fmt.Printf("Tekan Enter untuk selasai ")
	fmt.Scanln()
}
