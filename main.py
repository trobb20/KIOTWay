import RPi.GPIO as GPIO
import logging
import time

GPIO.setmode(GPIO.BOARD)
logging.basicConfig(filename='log.txt', level=logging.DEBUG)


class Solenoid:
    def __init__(self, name: str, pin_num: int):
        """
        :param name: Name of the solenoid
        :param pin_num: Board number for the signal pin of the solenoid
        :rtype: Solenoid object
        """
        if type(name) != str:
            logging.error('Name needs to be a string.')
            name = 'default_name'
        if type(pin_num) != int or not (0 < pin_num < 40):
            logging.error('Pin num invalid. Setting to pin 7 (GPIO4)')
            pin_num = 7

        self.pin_num = pin_num
        self.name = name
        GPIO.setup(self.pin_num, GPIO.OUT)
        logging.debug('Setup solenoid %s on pin %d' % (name, pin_num))

    def open(self) -> None:
        """
        Opens a solenoid
        :return: None
        """
        GPIO.output(self.pin_num, GPIO.HIGH)
        logging.debug('Opened solenoid %s on pin %d'%(self.name, self.pin_num))

    def close(self) -> None:
        """
        Closes a solenoid
        :return:
        """
        GPIO.output(self.pin_num, GPIO.LOW)
        logging.debug('Closed solenoid %s on pin %d'%(self.name, self.pin_num))

    def actuate(self, delay_ms: int) -> None:
        """
        Turns a solenoid on and off
        :param delay_ms: time to delay between on and off in milliseconds
        :return: None
        """
        logging.info('Actuating solenoid %s on pin %d for %f milliseconds' % (self.name, self.pin_num, float(delay_ms)))
        logging.debug('Starting actuation at %s' % (str(time.time())))
        self.open()
        time.sleep(delay_ms / 1000)
        self.close()
        logging.debug('Finished actuation at %s' % (str(time.time())))


def main():
    while True:
        tank_solenoid = Solenoid('tank', 7)
        tank_solenoid.actuate(500)
        time.sleep(2)


if __name__ == '__main__':
    main()
