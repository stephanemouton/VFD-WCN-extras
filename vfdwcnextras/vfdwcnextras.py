# VFD-WCN extra services module
from enum import Enum

DISPLAY_WIDTH = 20
PROGRESS_CHAR = 219
# Other possible value to consider as a future configuration parameter
# PROGRESS_CHAR = 177

class DisplayAlignment(Enum):
    left = 0
    center = 1
    right = 2


class BA6XCounter:
    def __init__(self, device, start_value=0, increment=1, padding=0, caption='', alignment=DisplayAlignment.left):
        self.__device = device
        self.__start_value = start_value
        self.__current_value = start_value
        self.__increment = increment
        self.__padding = padding
        self.__caption = caption
        self.__alignment = alignment
        self.__text_counter = ''
        self.__text_caption = ''

        self.__device.clearscreen()
        self.__display()
        self.__display_caption()

    def __display(self):
        self.__device.poscur(1, 1)
        self.__text_counter = ('{:0' + str(self.__padding) + '}').format(self.__current_value)
        if self.__alignment == DisplayAlignment.left:
            self.__text_counter = '{:<20}'.format(self.__text_counter)
        elif self.__alignment == DisplayAlignment.center:
            self.__text_counter = '{:^20}'.format(self.__text_counter)
        else:  # Align on right
            self.__text_counter = '{:>20}'.format(self.__text_counter)

        self.__device.write_msg(self.__text_counter)

    def __display_caption(self):
        self.__device.poscur(2, 1)
        if self.__alignment == DisplayAlignment.left:
            self.__text_caption = '{:<20}'.format(self.__caption)
        elif self.__alignment == DisplayAlignment.center:
            self.__text_caption = '{:^20}'.format(self.__caption)
        else:  # Align on right
            self.__text_caption = '{:>20}'.format(self.__caption)

        self.__device.write_msg(self.__text_caption)

    def reset(self):
        self.__device.clearscreen()
        self.__current_value = self.__start_value
        self.__display()
        self.__display_caption()

    def increment(self):
        self.__current_value += self.__increment
        self.__display()

    def set_start_value(self, value):
        self.__start_value = value

    def set_increment(self, increment):
        self.__increment = increment

    def set_padding(self, padding):
        self.__padding = padding

    def set_alignment(self, alignment):
        self.__alignment = alignment

    def set_caption(self, caption):
        self.__caption = caption
        self.__display_caption()


class BA6XProgressBar:
    def __init__(self, device, start_value=0, percentage=True, caption='', alignment=DisplayAlignment.center):
        self.__device = device
        self.__current_value = start_value
        self.__percentage = percentage
        self.__caption = caption
        self.__alignment = alignment
        self.__progress_bar = ''
        self.__text_caption = ''

        self.__device.clearscreen()
        self.__set_current_value(start_value)
        self.__display()
        self.__display_caption()

    def __set_current_value(self, new_value):
        self.__current_value = int(new_value)
        self.__current_value %= 101

    def __display(self):
        self.__device.poscur(1, 1)
        rounded_value = round(self.__current_value / 5)
        display_string = chr(PROGRESS_CHAR) * rounded_value
        display_string += ' ' * (20 - rounded_value)

        if self.__percentage:
            percent = '[' + str(self.__current_value) + '%]'
            start_percent = int((20 - len(percent)) / 2)
            display_string = display_string[:start_percent] + \
                             percent + \
                             display_string[start_percent + len(percent):]

        self.__progress_bar = display_string
        # self.__device.write_msg(self.__progress_bar)

        for ch in self.__progress_bar:
            self.__device.printchr(ord(ch))

    def __display_caption(self):
        self.__device.poscur(2, 1)
        if self.__alignment == DisplayAlignment.left:
            self.__text_caption = '{:<20}'.format(self.__caption)
        elif self.__alignment == DisplayAlignment.center:
            self.__text_caption = '{:^20}'.format(self.__caption)
        else:  # Align on right
            self.__text_caption = '{:>20}'.format(self.__caption)

        self.__device.write_msg(self.__text_caption)

    def reset(self):
        self.__device.clearscreen()
        self.__current_value = 0
        self.__display()
        self.__display_caption()

    def display_value(self, value):
        self.__set_current_value(value)
        self.__display()

    def set_percentage(self, percentage):
        self.__percentage = percentage

    def set_alignment(self, alignment):
        self.__alignment = alignment

    def set_caption(self, caption):
        self.__caption = caption
        self.__display_caption()
