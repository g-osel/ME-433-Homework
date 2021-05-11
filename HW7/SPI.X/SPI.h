#include<xc.h>           // processor SFR definitions
#include<sys/attribs.h>  // __ISR macro

#ifndef SPI__H__
#define SPI__H__

void initSPI();
unsigned char spi_io(unsigned char o);


#endif // SPI__H__