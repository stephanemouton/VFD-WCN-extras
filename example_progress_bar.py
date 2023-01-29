# Simple example of use of BA6XProgressBar class fo simulate file copy

import time
from vfdwcn import *
from vfdwcnextras.vfdwcnextras import *

factory = WincorNixdorfDisplayFactory()

vfds = factory.get_vfd_wcn(vfdwcn.BA63)
my_vfd = vfds[0]

try:
    # Center aligned example
    start_value = 0
    percentage = True
    caption = 'File copy'
    alignment = DisplayAlignment.center
    my_progress_bar = BA6XProgressBar(my_vfd,
                                      start_value,
                                      percentage,
                                      caption,
                                      alignment)
    for j in range(0, 101):
        my_progress_bar.display_value(j)
        time.sleep(0.5)
        print(j)

except KeyboardInterrupt:
    pass
for vfd in vfds:
    vfd.close()
