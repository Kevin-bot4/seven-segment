# Seven Segment

## Hardware Setup

### Part List

- 1 x TDCR1060M Clock Display
- 1 x 4116R-1-221-LF Resistor Array
- 4 x 330Ω Resistors
- 1 x 10kΩ Resistor
- 1 x Raspberry Pi
- 1 x Push button
- 2 x LEDs
- 1 x 40 pin Ribbon Cable-to-breadboard adapter
- 1 x 40 Pin Ribbon Cable

### Schematics

![Schematics](./../res/Single_seven_segment_4.jpg)

## Software

To run the program as a clock:

1. Change directory to this one (where README.md file is),
2. Execute:
```
python -m seven-segment clock
```
or to get the usage help information:
```
python -m seven-segment -h
```
