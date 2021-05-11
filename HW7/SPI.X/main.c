#include<xc.h>           // processor SFR definitions
#include<sys/attribs.h>  // __ISR macro
#include "SPI.h" // Include SPI init and io
#include <stdio.h>
#include <math.h>


#define PI 3.14159265358979323846
void delay();
// DEVCFG0
#pragma config DEBUG = OFF // disable debugging
#pragma config JTAGEN = OFF // disable jtag
#pragma config ICESEL = ICS_PGx1 // use PGED1 and PGEC1
#pragma config PWP = OFF // disable flash write protect
#pragma config BWP = OFF // disable boot write protect
#pragma config CP = OFF // disable code protect

// DEVCFG1
#pragma config FNOSC = FRCPLL // use internal oscillator with pll
#pragma config FSOSCEN = OFF // disable secondary oscillator
#pragma config IESO = OFF // disable switching clocks
#pragma config POSCMOD =  OFF// Internal RC
#pragma config OSCIOFNC = OFF // disable clock output
#pragma config FPBDIV = DIV_1 // divide sysclk freq by 1 for peripheral bus clock
#pragma config FCKSM = CSDCMD // disable clock switch and FSCM
#pragma config WDTPS = PS1048576 // use largest wdt
#pragma config WINDIS = OFF // use non-window mode wdt
#pragma config FWDTEN = OFF // wdt disabled
#pragma config FWDTWINSZ = WINSZ_25 // wdt window at 25%

// DEVCFG2 - get the sysclk clock to 48MHz from the 8MHz crystal
#pragma config FPLLIDIV = DIV_2 // divide input clock to be in range 4-5MHz
#pragma config FPLLMUL = MUL_24 // multiply clock after FPLLIDIV
#pragma config FPLLODIV = DIV_2 // divide clock after FPLLMUL to get 48MHz

// DEVCFG3
#pragma config USERID = 0 // some 16bit userid, doesn't matter what
#pragma config PMDL1WAY = OFF // allow multiple reconfigurations
#pragma config IOL1WAY = OFF // allow multiple reconfigurations


int main() {

    __builtin_disable_interrupts(); // disable interrupts while initializing things

    // set the CP0 CONFIG register to indicate that kseg0 is cacheable (0x3)
    __builtin_mtc0(_CP0_CONFIG, _CP0_CONFIG_SELECT, 0xa4210583);

    // 0 data RAM access wait states
    BMXCONbits.BMXWSDRM = 0x0;

    // enable multi vector interrupts
    INTCONbits.MVEC = 0x1;

    // disable JTAG to get pins back
    DDPCONbits.JTAGEN = 0;

    // do your TRIS and LAT commands here
    TRISAbits.TRISA4 = 0;        // Set Pin 12 as an output.
    LATAbits.LATA4 = 0;    // Set Pin as high so the LED turns off.  These pins sink current
    TRISBbits.TRISB4 = 1; //Set Pin connected to LED button as input
    
    initSPI();

    __builtin_enable_interrupts(); 

    double x[100], f[100], y[100]; 
    unsigned short dataB[100],dataA[100], config_bitsB, config_bitsA;
    int i, j;
//    for (j = 0; j <= 100; j++) {
//        x[j] = ((double)j) / 50.0;
//        f[j] = 511 * sin(4.0 * PI * x[j]);
//        f[j] = (unsigned short) f[j];
//
//
//        data[j] = f[j] << 2;
//        config_bits = 0b1111;
//        data[j] = data[j] | (config_bits << 12);
//        
//    }


    //unsigned char i = 0;
    
    while (1) {

//        for (j = 0; j <= 100; j++) {
//            x[j] = ((double) j) / 100.0;
//            f[j] = (511 * sin(4.0 * PI * x[j])) + 512;
//            dataB[j] = (unsigned short) f[j];
//
//
//            dataB[j] = dataB[j] << 2;
//            config_bitsB = 0b1111;
//            dataB[j] = dataB[j] | (config_bitsB << 12);
//
//        // write one byte over SPI1
//
//            LATAbits.LATA0 = 0; // bring CS low
//            spi_io((dataB[j] >> 8)); // write the byte
//            spi_io(dataB[j]);
//            LATAbits.LATA0 = 1; // bring CS high
//        }
        
        y[0] = 0 ;
        for(i = 1; i<=100; i++) {
            if (i <= 50){
                y[i] = y[i-1] + 10;
            }
            else if (i > 50){
                y[i] = y[i-1] - 10;
            }
            
            y[i] = y[i];
            dataA[i] = ((unsigned short) y[i]) + 511;
            dataA[i] = dataA[i] <<  2;
            config_bitsA = 0b0111;
            dataA[i] = dataA[i] | (config_bitsA << 12);
            
            LATAbits.LATA0 = 0; // bring CS low
            spi_io((dataA[i] >> 8)); // write the byte
            spi_io(dataA[i]);
            LATAbits.LATA0 = 1; // bring CS high
            
            delay();
            
        }
            

        
         
//        i++;
//        if (i ==100){
//            i = 0;
//        }
        
//        _CP0_SET_COUNT(0);
//        
//        while (_CP0_GET_COUNT() < 48000000/2 ) {
//            // 1 Hz
//        }
        

        // remember the core timer runs at half the sysclk
        
        

    }
}


void delay(){
            long int time;
            _CP0_SET_COUNT(0);
            time = _CP0_GET_COUNT();
            while(_CP0_GET_COUNT() - time < 2400000){
                ;// do nothing for 1/10th of a second
            }
}

