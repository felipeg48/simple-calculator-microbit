a = 0
b = 0

def on_pin_pressed_p0():
    global a
    a = a - 1
    basic.show_number(a)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global a
    a += 1
    basic.show_number(a)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(a + b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global b
    b += 1
    basic.show_number(b)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global b
    b = b - 1
    basic.show_number(b)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_gesture_shake():
    global a, b
    a = 0
    b = 0
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
