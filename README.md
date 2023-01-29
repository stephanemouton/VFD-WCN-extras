# VFD-WCN-extras
Library of extra features for WIncor-Nixdorf BA6X displays.

The library is an add-on on top of [VFD-WCN](https://github.com/stephanemouton/VFD-WCN) library.

It adds display services at a higher level of abstraction.

## Installation

* VFD-WCN library must be installed.

## Services

### Counter

The BA6XCounter Class manages details to help display a counter easily. Parameters are the following:
* start_value: initial value to start counter (default: 0)
* increment (default: 1)
* padding: amount of zeros to fill before counter value (default: 0)
* caption: text to be displayed below counter
* alignment: defaut is left (see DisplayAlignment)

Main available methods are:
* increment: triggers display
* reset: restart counter

Counter properties can be changed using setters methods. Changing caption triggers display.

### Progress bar

The goal of BA6XProgressBar is to help you use a progress bar quickly and, I hope, conveniently.
Value displayed is a percentage [0..100]. Progress bar properties are:
* start_value: initial value to start progressbar (default: 0)
* percentage: display percentage superimposed on progress bar? (default is True)
* caption: text to be displayed below progress bar
* alignment: default is center (see DisplayAlignment)

Main available methods are:
* display_value: well ... sort of display value between 0 and 100 ;-)
* reset: restart progress bar

Progress bar properties can be changed using setters methods. Changing caption triggers display.
