package main

import "fmt"

func f(x int, ch chan int) {
	a := x

	for i := 0; i < 100_000_001; i++ {
		a += i * i
	}

	ch <- a

	fmt.Printf("Send: %v\n", x)
}

func main() {
	count := 8
	ch := make(chan int, count)

	for i := 0; i < count; i++ {
		go f(i, ch)
	}

	fmt.Println("All goroutines created")

	for i := 0; i < count; i++ {
		fmt.Println(<-ch)
	}

	fmt.Println("Done")
}
