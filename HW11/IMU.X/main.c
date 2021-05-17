#include<xc.h>           // processor SFR definitions
#include<sys/attribs.h>  // __ISR macro
#include <stdio.h>
#include <math.h>
#include "i2c_master_noint.h" // Include SPI init and io
#include "UART.h"
#include "ST7789.h"
#include "font.h"
#include "spi.h"
#include "imu.h"


#define PI 3.14159265358979323846
//void delay();
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
    LATAbits.LATA4 = 0;// Set Pin as low so the LED turns off.  These pins sink current
    TRISBbits.TRISB4 = 1; //Set Pin connected to LED button as input
    
    UARTinit();
    i2c_master_setup();
    initSPI();
    LCD_init();
    LCD_clearScreen(BLUE);
    
    
    imu_setup();
    LATAbits.LATA4 = 1;
   
    
    
     
    
    
    
    
   
    __builtin_enable_interrupts();
    
 
    char m[100];

    // I2C init for IO
    signed short imu[7];
    unsigned char outTemp[14];

    while (1) {
        readMultiplePins(IMU_ADDR, IMU_OUT_TEMP_L , outTemp, 14);
        imu_read(imu, outTemp, 7);
        
        int num1 = imu[4] / 160;
        int num2 = imu[5] /160;
        
        xdrawBar(120, 120, GREEN, BLUE, num1);
        ydrawBar(120, 120, GREEN, BLUE, num2);
        sprintf(m, "g: %d  %d  %d  ", imu[1], imu[2], imu[3]);
        drawString(0, 0, WHITE, m);
        sprintf(m, "a: %d  %d  %d  ", imu[4], imu[5], imu[6]);
        drawString(0, 8, WHITE, m);
        sprintf(m, "t: %d  ", imu[0]);
        drawString(0, 16, WHITE, m);


        LATAbits.LATA4 = 1; //Turn LED ON
        delay(2400000); // do nothing for 1/10th a second
        LATAbits.LATA4 = 0; // Turn LED OFF
        delay(2400000); // do nothing for 1/10th a second
    }
}


