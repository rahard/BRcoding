// kode sederhana untuk menunjukkan concurrency
// Budi Rahardjo (@rahard)
// 2022, public domain
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

	// supaya function conccurent terlihat, kita tunggu dengan Scanln
        // jika bagian ini dikomentarkan maka sering kali 
        // "main()" sudah selesai, thread "cetak()" belum sempat dijalankan
	fmt.Scanln()
}
