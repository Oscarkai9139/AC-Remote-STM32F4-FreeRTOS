/*
 * printf.h
 *
 *  Created on: Apr 26, 2021
 *      Author: wandog
 */

#ifndef INC_PRINTF_H_
#define INC_PRINTF_H_
#include <stdio.h>
#include <string.h>
#include "main.h"

#ifdef __GNUC__
/* With GCC, small printf (option LD Linker->Libraries->Small printf
   set to 'Yes') calls __io_putchar() */


#define PUTCHAR_PROTOTYPE int __io_putchar(int ch)

#else
#define PUTCHAR_PROTOTYPE int fputc(int ch, FILE *f)
#endif /* __GNUC__ */
/**
  * @brief  Retargets the C library printf function to the USART.
  * @param  None
  * @retval None
  */

PUTCHAR_PROTOTYPE
{
HAL_UART_Transmit(&huart4, (uint8_t *)&ch, 1, 0xFFFF);
return ch;
}


#endif /* INC_PRINTF_H_ */
