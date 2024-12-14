import board
import busio

class SerialRelay:
    def __init__(self, baudrate=9600):
        # Example usage
        # Specify the pins for input and output UARTs
        input_rx = board.GP1  # Replace with actual pin numbers
        input_tx = board.GP0  # Replace with actual pin numbers
        output_rx = board.GP9  # Replace with actual pin numbers
        output_tx = board.GP8  # Replace with actual pin numbers
        # Initialize the input UART (RX/TX pins)
        self.input_uart = busio.UART(input_tx, input_rx, baudrate=baudrate)
        
        # Initialize the output UART (RX/TX pins)
        self.output_uart = busio.UART(output_tx, output_rx, baudrate=baudrate)

    def update(self):
        # Read from input UART
        data = self.input_uart.read(32)  # Adjust the number of bytes as needed
        if data:
            # Write to output UART
            self.output_uart.write(data)

    def write(self, data):
        self.output_uart.write(data)


