// package main

// import (
// 	"syscall/js"
// )

// // func add(a float64, b float64) float64 {
// // 	return a + b
// // }

// func add(this js.Value, inputs []js.Value) interface{} {
// 	return inputs[0].Float() + inputs[1].Float()
// }

// func sub(this js.Value, inputs []js.Value) interface{} {
// 	message := inputs[0].String()

// 	document := js.Global().Get("document")
// 	p := document.Call("getElementById", args[0])
// 	p.Set("innerHTML", message)
// 	document.Get("body").Call("appendChild", p)

// 	return 0
// }

// func main() {
// 	c := make(chan bool)

// 	js.Global().Set("printMessage", js.FuncOf(sub))

// 	<-c

// }

//==================================================

package main

import (
	"strconv"
	"syscall/js"
)

var document js.Value

func inc(this js.Value, args []js.Value) interface{} {
	document := js.Global().Get("document")
	var val = (document.Call("getElementById", args[0])).Get("innerHTML").String()
	// var value = p.Get("innerHTML").String()
	count, _ := strconv.Atoi(val)
	count += 1
	document.Call("getElementById", args[0]).Set("innerHTML", count)
	return val
}

func dec(this js.Value, args []js.Value) interface{} {
	document := js.Global().Get("document")
	var val = (document.Call("getElementById", args[0])).Get("innerHTML").String()
	// var value = p.Get("innerHTML").String()
	count, _ := strconv.Atoi(val)
	count -= 1
	document.Call("getElementById", args[0]).Set("innerHTML", count)
	return val
}

func res(this js.Value, args []js.Value) interface{} {
	document := js.Global().Get("document")
	p := document.Call("getElementById", args[0])
	p.Set("innerHTML", "go!")
	return nil
}

func registerCallbacks() {
	js.Global().Set("inc", js.FuncOf(inc))
	js.Global().Set("dec", js.FuncOf(dec))
	js.Global().Set("res", js.FuncOf(res))
}

func main() {
	c := make(chan struct{}, 0)
	println("Hello World")
	registerCallbacks()

	<-c
}
