import serial

serial_port = 'COM3'
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate, timeout=1)

def send_command(command):
    ser.write(command.encode())

def handle_message(msg):
    if msg == "chippi":
        send_command('L')
        
    if msg == "chappa":
        send_command('R')