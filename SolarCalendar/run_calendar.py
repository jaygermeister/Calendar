#!/usr/bin/env python3

from solar_calendar.calendar import SolarCalendar
from datetime import datetime

def main():
    calendar = SolarCalendar()
    current_date = datetime.now()
    
    print("\n=== Solar Calendar System ===")
    print(f"Current Date: {current_date.strftime('%Y-%m-%d')}")
    
    # Get current constellation
    constellation = calendar.get_current_constellation()
    print(f"\nCurrent Constellation: {constellation}")
    
    # Get current month info
    current_month = calendar.get_current_month()
    print(f"Current Month: {current_month}")

if __name__ == "__main__":
    main() 