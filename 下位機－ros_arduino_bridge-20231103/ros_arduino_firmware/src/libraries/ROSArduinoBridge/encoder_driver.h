/* *************************************************************
   Encoder driver function definitions - by James Nugen
   ************************************************************ */
   
   
#ifdef ARDUINO_ENC_COUNTER
  //below can be changed, but should be PORTD pins; 
  //otherwise additional changes in the code are required
  #define LEFT_ENC_PIN_A PD2  //pin 2
  #define LEFT_ENC_PIN_B PD3  //pin 3
  
  //below can be changed, but should be PORTC pins
  #define RIGHT_ENC_PIN_A PC4  //pin A4
  #define RIGHT_ENC_PIN_B PC5   //pin A5
#elif defined ARDUINO_MY_COUNTER
  //定義引腳
  #define LEFT_A  21 //2
  #define LEFT_B  20 //3
  #define RIGHT_A  18  //5
  #define RIGHT_B  19 //4

  //聲明函式
  //1.初始化函數，設置引腳操作模式，並添加中斷
  void initEncoder();
  //2.中斷函數
  void leftEncoderEventA();
  void leftEncoderEventB();
  void rightEncoderEventA();
  void rightEncoderEventB();
#endif
   
long readEncoder(int i);
void resetEncoder(int i);
void resetEncoders();
