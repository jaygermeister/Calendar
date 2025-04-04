# Solar System Calendar

A modern calendar system based on astronomical events, featuring:
- 13 months aligned with astronomical events
- Integration with the 13 constellations of the zodiac
- Alignment with equinoxes and solstices
- Periodic astronomical events tracking

## Project Structure

- `solar_calendar/` - Core calendar implementation
  - `calendar.py` - Main calendar class and calculations
  - `astronomy.py` - Astronomical event calculations
  - `zodiac.py` - Zodiac constellation calculations
- `tests/` - Unit tests
- `examples/` - Usage examples
- `docs/` - Documentation

## Features

- Accurate astronomical event calculations
- 13-month calendar system
- Zodiac constellation tracking
- Equinox and solstice alignment
- Customizable calendar views
- Astronomical event predictions

## Requirements

- Python 3.8+
- See requirements.txt for dependencies

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from solar_calendar import SolarCalendar

# Create a new calendar instance
calendar = SolarCalendar()

# Get current month
current_month = calendar.get_current_month()

# Get upcoming astronomical events
events = calendar.get_upcoming_events()

# Get zodiac information
zodiac = calendar.get_current_zodiac()
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 