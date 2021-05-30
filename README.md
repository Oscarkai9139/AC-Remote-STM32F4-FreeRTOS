# AC-Remote-STM32F4-FreeRTOS
## Project Description
This project is intended to be a device to control any Air conditioning unit with an unkown IR protocol once the protocol of the device has been reverse engineered.

## Board Configurations


| Pins  | Configs  | Label       |
| :---: | :---:    | :---:       |
| PA0   | GPIO_IN  | Blue_Button |
| PD12  | GPIO_OUT | Green_LED   |
| PD13  | GPIO_OUT | Orange_LED  |
| PD14  | GPIO_OUT | Red_LED     |
| PD15  | GPIO_OUT | Blue_LED    |
| PC0   | GPIO_OUT | IR_Transmit |
| PC1   | GPIO_IN  | IR_Receive  |
| PC10   | UART4_TX  | printf.h  |
| PC11   | UART4_RX  | - |
| PD0 | GPIO_IN  | Numpad |
| PD1 | GPIO_IN  | Numpad |
| PD2 | GPIO_IN  | Numpad |
| PD3 | GPIO_IN  | Numpad |
| PB4 | GPIO_OUT | Numpad |
| PB5 | GPIO_OUT | Numpad |
| PB6 | GPIO_OUT | Numpad |
| PB7 | GPIO_OUT | Numpad |
