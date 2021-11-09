package main

import (
	"fmt"
)

func cetak(terima chan int) {
	var x int
	for {
		x = <-terima
		fmt.Printf("terima: %d\n", x)
	}
}

func main() {
	fmt.Println("Concurrent 3")
	// fungsi cetak ada looping terus

	kirim := make(chan int)
	go cetak(kirim)
	kirim <- 7
	kirim <- 11
	kirim <- 2
	kirim <- 5

	// supaya function conccurent terlihat
	fmt.Printf("Tekan Enter untuk selasai ")
	fmt.Scanln()
}
