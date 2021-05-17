#include "imu.h"
#include "i2c_master_noint.h"
#include<xc.h> // processor SFR definitions


void delay(int wait) {
    long int time;
    _CP0_SET_COUNT(0);
    time = _CP0_GET_COUNT();
    while (_CP0_GET_COUNT() - time < wait) {
        ; // do nothing for 1/10th of a second
    }
} 

void imu_setup(){
    unsigned char who = 0;
    
    // read from IMU_WHOAMI
    who = readPin(IMU_ADDR, IMU_WHOAMI); // Reading a pin
    
    if(who != 0b01101001){
        while(1) {
            LATAbits.LATA4 = 1; //Turn LED ON
            delay(60000); // do nothing for half a second
            LATAbits.LATA4 = 0; // Turn LED OFF
            delay(60000); // do nothing for half a second
        }
    }
    
    
    // init IMU_CTRL1_XL
    unsigned char CTRL1config = 0b10000010;
    setPin(IMU_ADDR, IMU_CTRL1_XL, CTRL1config);
    
    
    // init IMU_CTRL2_G
    unsigned char CTRL2config = 0b10001000;
    setPin(IMU_ADDR, IMU_CTRL2_G, CTRL2config);
    
    // init IMU_CTRL3_C
    unsigned char CTRL3config = 0b00000100;
    setPin(IMU_ADDR, IMU_CTRL3_C, CTRL3config);
   
}
void imu_read(signed short * data, unsigned char * data2, int length) {
    int j = 0;
    int i;
//    unsigned char rec[(2*length) + 1];
//    rec = readMultiplePins(IMU_ADDR, reg, (length*2));
    
    for (i = 0; i < (length); i++) {
        data[i] = (data2[j + 1] << 8) | data2[j];
        j = j + 2;
    }

}