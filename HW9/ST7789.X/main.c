#include<xc.h>           // processor SFR definitions
#include<sys/attribs.h>  // __ISR macro
#include <stdio.h>
#include <math.h>
#include "spi.h" // Include SPI library
#include "ST7789.h"
#include "font.h"

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
    TRISAbits.TRISA4 = 0; // Set Pin 12 as an output.
    LATAbits.LATA4 = 0; // Set Pin as low so the LED turns off.  These pins sink current
    TRISBbits.TRISB4 = 1; //Set Pin connected to LED button as input


    //    // I2C init for IO
    //    i2c_master_setup();
    //    unsigned char write_add = 0b01000000;
    //    unsigned char regIODIRA = 0x00;
    //    unsigned char regIODIRB = 0x01;
    //    unsigned char valIODIRA = 0x00;
    //    unsigned char valIODIRB = 0xFF;
    //    
    //    setPin(write_add, regIODIRA, valIODIRA); 
    //    setPin(write_add, regIODIRB, valIODIRB); 
    initSPI();
    LCD_init();

    __builtin_enable_interrupts();
    LCD_clearScreen(BLUE);


    float tstart, tend, FPS;

    char m[30];
    int num = 0;
    int i = 0;
    unsigned short x = 28;
    unsigned short y = 32;
    unsigned short xf = 35;
    unsigned short yf = 64;
    unsigned short xBar = 28;
    unsigned short yBar = 48;


    while (1) {

        //LCD_drawPixel(28,32,WHITE);
        // 
        //drawChar(x,y,WHITE, 'H');
        tstart = _CP0_GET_COUNT();
        sprintf(m, "Hello World! %d   ", num);
        drawString(x, y, WHITE, m);
        tend = _CP0_GET_COUNT();
        FPS = 24000000 / (tend - tstart) ;
        sprintf(m, "FPS: %f", FPS);
        drawString(xf, yf, WHITE, m);
        drawBar(xBar, yBar, GREEN, WHITE, num);
        num++;
        if (num == 100) {
            num = 00;
        }
        
        LATAbits.LATA4 = 1; //Turn LED ON
        delay(); // do nothing for half a second
        LATAbits.LATA4 = 0; // Turn LED OFF
        delay(); // do nothing for half a second
    }
}

void delay() {
    long int time;
    _CP0_SET_COUNT(0);
    time = _CP0_GET_COUNT();
    while (_CP0_GET_COUNT() - time < 2400000) {
        ; // do nothing for 1/10th of a second
    }
}

