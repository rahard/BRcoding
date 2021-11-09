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

func generator(kemana chan int) {
	for i := 100; i < 110; i++ {
		kemana <- i
	}
}

func generator2(kemana chan int) {
	for i := 200; i < 210; i++ {
		kemana <- i
	}
}

func main() {
	fmt.Println("Concurrent 5")
	// ada banyak pengirim

	kirim := make(chan int)
	go cetak(kirim)
	go generator(kirim)
	go generator2(kirim)

	for i := 0; i < 10; i++ {
		kirim <- i
	}

	// supaya function conccurent terlihat
	fmt.Printf("Tekan Enter untuk selasai ")
	fmt.Scanln()
}
