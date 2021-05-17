#ifndef UART_H__
#define UART_H__


#include<xc.h> // processor SFR definitions

void UARTinit();
void ReadUART1(char * string, int maxLength);
void WriteUART1(const char * string);


#endif