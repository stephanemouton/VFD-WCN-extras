# Example of use of the BA6XCounter class

import time
from vfdwcn import *
from vfdwcnextras.vfdwcnextras import *

factory = WincorNixdorfDisplayFactory()

vfds = factory.get_vfd_wcn(vfdwcn.BA63)
my_vfd = vfds[0]

try:
    # # Left aligned example
    # start_value = 0
    # increment = 1
    # padding = 0
    # caption = 'Twitter Followers'
    # alignment = DisplayAlignment.left
    # my_counter = BA6XCounter(my_vfd,
    #                          start_value,
    #                          increment,
    #                          padding,
    #                          caption,
    #                          alignment)
    # for j in range(0,4326):
    #     my_counter.increment()
    # time.sleep(2)
    #
    # # Center aligned example
    # start_value = 0
    # increment = 30
    # padding = 0
    # caption = 'Altitude'
    # alignment = DisplayAlignment.center
    # my_counter = BA6XCounter(my_vfd,
    #                          start_value,
    #                          increment,
    #                          padding,
    #                          caption,
    #                          alignment)
    # for j in range(0, 1000):
    #     my_counter.increment()
    # time.sleep(2)

    # Right aligned example
    start_value = 0
    increment = 5
    padding = 5
    caption = 'Total amount due'
    alignment = DisplayAlignment.right
    my_counter = BA6XCounter(my_vfd,
                             start_value,
                             increment,
                             padding,
                             caption,
                             alignment)
    for j in range(0, 4000):
        my_counter.increment()

except KeyboardInterrupt:
    pass
for vfd in vfds:
    vfd.close()
