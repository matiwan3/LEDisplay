import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the LED panel
# Modify these pin numbers based on your actual connections
A, B, C, D = 23, 24, 25, 8
CLK, LAT, OE, R1, G1, B1, R2, G2, B2 = 11, 10, 9, 17, 22, 27, 5, 6, 13

# Set up GPIO pins
GPIO.setup([A, B, C, D, CLK, LAT, OE, R1, G1, B1, R2, G2, B2], GPIO.OUT)

# Function to turn off all LEDs
def set_all_leds_black():
    GPIO.output(LAT, GPIO.LOW)  # Pull latch low
    GPIO.output(OE, GPIO.LOW)   # Enable output (active low)

    # Shift in zeros to turn off all LEDs
    for _ in range(32 * 64):
        GPIO.output(R1, GPIO.LOW)  # Set RGB pins to low (off)
        GPIO.output(G1, GPIO.LOW)
        GPIO.output(B1, GPIO.LOW)
        GPIO.output(R2, GPIO.LOW)
        GPIO.output(G2, GPIO.LOW)
        GPIO.output(B2, GPIO.LOW)
        GPIO.output(CLK, GPIO.HIGH)
        GPIO.output(CLK, GPIO.LOW)

    GPIO.output(LAT, GPIO.HIGH)  # Pulse the latch to commit the data
    GPIO.output(LAT, GPIO.LOW)

# Set all LEDs to black (off)
set_all_leds_black()

# Cleanup GPIO
GPIO.cleanup()
