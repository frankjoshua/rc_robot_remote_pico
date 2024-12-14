class MotorController:
    def __init__(self, serial):
        self.serial = serial

    def update(self, left, right):
        """
        Updates the motor speeds based on the provided left and right values.

        Args:
            left (float): Left motor speed in the range [-1, 1].
            right (float): Right motor speed in the range [-1, 1].
        """
        print("Left:", left, "Right:", right)

        # Check if both motors should be shut down
        if left == 0 and right == 0:
            self.serial.write(bytes([0]))
            return

        # Map the input values to the appropriate byte ranges
        left_speed = self._map_motor1_speed(left)
        right_speed = self._map_motor2_speed(right)

        # Send both motor commands in a single write operation
        self.serial.write(bytes([left_speed, right_speed]))

    def _map_motor1_speed(self, value):
        """
        Maps a value in the range [-1, 1] to the range [1, 127] for Motor 1.

        Args:
            value (float): Desired speed in the range [-1, 1].

        Returns:
            int: Mapped byte value for Motor 1.
        """
        # Clamp the value to ensure it's within [-1, 1]
        value = max(-1.0, min(1.0, value))
        
        # Mapping:
        # -1 -> 1 (Full Reverse)
        #  0 -> 64 (Stop)
        #  1 -> 127 (Full Forward)
        mapped_value = int((value + 1) * 63) + 1
        return mapped_value

    def _map_motor2_speed(self, value):
        """
        Maps a value in the range [-1, 1] to the range [128, 255] for Motor 2.

        Args:
            value (float): Desired speed in the range [-1, 1].

        Returns:
            int: Mapped byte value for Motor 2.
        """
        # Clamp the value to ensure it's within [-1, 1]
        value = max(-1.0, min(1.0, value))
        
        # Mapping:
        # -1 -> 128 (Full Reverse)
        #  0 -> 192 (Stop)
        #  1 -> 255 (Full Forward)
        mapped_value = int((value + 1) * 63.5) + 128
        return mapped_value
