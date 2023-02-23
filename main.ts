let a = 0
let b = 0
input.onPinPressed(TouchPin.P0, function () {
    a = a - 1
    basic.showNumber(a)
})
input.onButtonPressed(Button.A, function () {
    a += 1
    basic.showNumber(a)
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(a + b)
})
input.onButtonPressed(Button.B, function () {
    b += 1
    basic.showNumber(b)
})
input.onPinPressed(TouchPin.P1, function () {
    b = b - 1
    basic.showNumber(b)
})
input.onGesture(Gesture.Shake, function () {
    a = 0
    b = 0
    basic.clearScreen()
})
