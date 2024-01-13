int rs = A1; 
int ls = A0; 
int leftValue;
int rightValue;
int echo = 8; 
int trig = 7; 
int distancia;

void setup() {
  pinMode(rs, INPUT);
  pinMode(ls, INPUT);
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  DDRB = DDRB | 0b00110000;
  DDRD = DDRD | 0b01100000;
}

void forward(){
  PORTB = PORTB | 0b00110000;
}
void turnRight(){
  PORTB = PORTB | 0b00010000;
  PORTB = PORTB & 0b11011111;
}
void turnLeft(){
  PORTB = PORTB | 0b00100000;
  PORTB = PORTB & 0b11101111;
}
void stopMotors(){
  PORTB = PORTB & 0b11001111;
}

void loop() {
  digitalWrite(trig, HIGH);
  digitalWrite(trig, LOW);
  distancia=pulseIn(echo, HIGH);
  if (distancia>500){
  leftValue = digitalRead(ls);
  rightValue = digitalRead(rs);
  PORTD = PORTD & 0b10011111;
    if(leftValue == 1 && rightValue == 0){
    turnLeft();
    PORTD = PORTD | 0b00100000;
  }else if(leftValue == 0 && rightValue == 1 ){
    turnRight();
    PORTD = PORTD | 0b01000000;
  }else if(leftValue == 0 && rightValue == 0){
    forward();
  }else if(leftValue == 1 && rightValue == 1){
    stopMotors();
  }
  }else if(distancia<=500){
    stopMotors();
  }
}