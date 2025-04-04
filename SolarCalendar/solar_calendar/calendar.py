from datetime import datetime, timedelta
import pytz
from typing import List, Dict, Optional
from .astronomy import AstronomicalEvents
from .zodiac import ZodiacCalculator

class SolarCalendar:
    # Constants for astronomical calculations
    GREAT_YEAR_CYCLE = 25772  # Complete precession cycle in years
    CONSTELLATION_AGE = 1982.46  # Years per constellation (25772/13)
    AQUARIUS_START = 1950  # Approximate start of Age of Aquarius
    
    def __init__(self):
        self.astronomy = AstronomicalEvents()
        self.zodiac = ZodiacCalculator()
        
        # Constellation data with accurate astronomical transit dates
        self.constellations = {
            "Scorpius": {"start_date": (11, 23), "end_date": (11, 29), "duration": 6},
            "Ophiuchus": {"start_date": (11, 29), "end_date": (12, 17), "duration": 18},
            "Sagittarius": {"start_date": (12, 17), "end_date": (1, 20), "duration": 33},
            "Capricornus": {"start_date": (1, 20), "end_date": (2, 16), "duration": 28},
            "Aquarius": {"start_date": (2, 16), "end_date": (3, 11), "duration": 24},
            "Pisces": {"start_date": (3, 11), "end_date": (4, 18), "duration": 38},
            "Aries": {"start_date": (4, 18), "end_date": (5, 13), "duration": 25},
            "Taurus": {"start_date": (5, 13), "end_date": (6, 21), "duration": 37},
            "Gemini": {"start_date": (6, 21), "end_date": (7, 20), "duration": 31},
            "Cancer": {"start_date": (7, 20), "end_date": (8, 10), "duration": 21},
            "Leo": {"start_date": (8, 10), "end_date": (9, 16), "duration": 37},
            "Virgo": {"start_date": (9, 16), "end_date": (10, 30), "duration": 45},
            "Libra": {"start_date": (10, 30), "end_date": (11, 23), "duration": 23}
        }
        
        # Month system with 28-day months and special days
        self.months = {
            "special_start": {"name": "Year Day (New Year)", "dates": "March 20", "days": 1, "symbol": "🌟"},
            1: {"name": "Aurora", "dates": "March 21 - April 17", "days": 28, "symbol": "🌅"},
            2: {"name": "Blossom", "dates": "April 18 - May 15", "days": 28, "symbol": "🌸"},
            3: {"name": "Zephyr", "dates": "May 16 - June 12", "days": 28, "symbol": "🌊"},
            4: {"name": "Solis", "dates": "June 13 - July 10", "days": 28, "symbol": "☀️"},
            5: {"name": "Radiance", "dates": "July 11 - August 7", "days": 28, "symbol": "🔆"},
            6: {"name": "Ember", "dates": "August 8 - September 4", "days": 28, "symbol": "🔥"},
            7: {"name": "Harvest", "dates": "September 5 - October 2", "days": 28, "symbol": "🌾"},
            8: {"name": "Equinox", "dates": "October 3 - October 30", "days": 28, "symbol": "⚖️"},
            9: {"name": "Frost", "dates": "October 31 - November 27", "days": 28, "symbol": "❄️"},
            10: {"name": "Yule", "dates": "November 28 - December 25", "days": 28, "symbol": "🎄"},
            11: {"name": "Hearth", "dates": "December 26 - January 22", "days": 28, "symbol": "🏠"},
            12: {"name": "Twilight", "dates": "January 23 - February 19", "days": 28, "symbol": "🌙"},
            13: {"name": "Eclipse", "dates": "February 20 - March 18", "days": 28, "symbol": "🌑"},
            "special_end": {"name": "Year End (Festival Day)", "dates": "March 19", "days": 1, "symbol": "🎉"},
            "leap": {"name": "Leap Day", "dates": "March 19 (leap years only)", "days": 1, "symbol": "⏳"}
        }

        # Month names for formatting dates
        self.month_names = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }

    def get_constellation_era_date(self, date: datetime = None) -> Dict:
        """Calculate the Constellation Era date components."""
        if date is None:
            date = datetime.now(pytz.UTC)
            
        # Calculate Constellation Era year (CE)
        ce_year = date.year - self.AQUARIUS_START
        
        # Calculate position in Great Cycle
        cycle_position = (date.year - self.AQUARIUS_START) % self.GREAT_YEAR_CYCLE
        current_age = "Aquarius"  # We're in the Age of Aquarius
        years_into_age = cycle_position % self.CONSTELLATION_AGE
        years_remaining = self.CONSTELLATION_AGE - years_into_age
        
        # Calculate percentage through current age
        age_percentage = (years_into_age / self.CONSTELLATION_AGE) * 100
        
        return {
            "ce_year": ce_year,
            "current_age": current_age,
            "years_into_age": int(years_into_age),
            "years_remaining": int(years_remaining),
            "age_percentage": round(age_percentage, 2),
            "cycle_position": int(cycle_position),
            "cycle_total": self.GREAT_YEAR_CYCLE
        }

    def is_leap_year(self, year: int) -> bool:
        """Determine if a year is a leap year."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def get_current_month(self) -> Dict:
        """Get the current month based on Gregorian date."""
        current_date = datetime.now()
        if current_date.tzinfo is None:
            current_date = current_date.replace(tzinfo=pytz.UTC)
        return self._get_month_for_date(current_date)
    
    def _get_month_for_date(self, date: datetime) -> Dict:
        """Determine which month a given date falls into."""
        if date.tzinfo is None:
            date = date.replace(tzinfo=pytz.UTC)
        
        # Convert the date to month and day
        month = date.month
        day = date.day
        
        # Check for special days first
        if month == 3 and day == 20:
            return self.months["special_start"]
        elif month == 3 and day == 19:
            if self.is_leap_year(date.year) and date.hour >= 12:  # After noon on leap year
                return self.months["leap"]
            return self.months["special_end"]
            
        # Define the start dates of each month
        month_starts = [
            (3, 21, 1),    # Aurora
            (4, 18, 2),    # Blossom
            (5, 16, 3),    # Zephyr
            (6, 13, 4),    # Solis
            (7, 11, 5),    # Radiance
            (8, 8, 6),     # Ember
            (9, 5, 7),     # Harvest
            (10, 3, 8),    # Equinox
            (10, 31, 9),   # Frost
            (11, 28, 10),  # Yule
            (12, 26, 11),  # Hearth
            (1, 23, 12),   # Twilight
            (2, 20, 13),   # Eclipse
        ]
        
        # Find the correct month
        current_month = 13  # Default to last month
        for start_month, start_day, month_num in month_starts:
            if (month > start_month) or (month == start_month and day >= start_day):
                current_month = month_num
                break
            if month < start_month:
                break
                
        return self.months[current_month]
    
    def get_upcoming_events(self, days_ahead: int = 30) -> List[Dict]:
        """Get upcoming astronomical events."""
        return self.astronomy.get_upcoming_events(days_ahead)
    
    def get_current_zodiac(self) -> Dict:
        """Get current zodiac constellation information."""
        return self.zodiac.get_current_constellation()
    
    def get_month_dates(self, year: int, month: int) -> List[datetime]:
        """Get all dates for a specific month."""
        if month < 1 or month > 13:
            return []
            
        # Get the start date for the month
        month_info = self.months[month]
        start_str = month_info["dates"].split(" - ")[0]
        start_month, start_day = self._parse_date(start_str)
        
        # Create datetime for the start of the month
        if start_month < 3:  # If the month starts in January or February, it's in the next year
            year += 1
        start_date = datetime(year, start_month, start_day, tzinfo=pytz.UTC)
        
        # Generate all dates for the month
        return [start_date + timedelta(days=x) for x in range(28)]
    
    def _parse_date(self, date_str: str) -> tuple:
        """Parse a month-day string into integers."""
        months = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }
        month_str, day_str = date_str.split(" ")
        return months[month_str], int(day_str)
    
    def get_equinox_solstice_dates(self, year: int) -> Dict:
        """Get the dates of equinoxes and solstices for a given year."""
        return self.astronomy.get_equinox_solstice_dates(year)
    
    def get_zodiac_transitions(self, year: int) -> List[Dict]:
        """Get the dates when the sun transitions between zodiac constellations."""
        return self.zodiac.get_transition_dates(year)
    
    def list_months(self) -> Dict:
        """Get the list of all months with their information."""
        return self.months
    
    def rename_month(self, month_number: int, new_name: str) -> bool:
        """Rename a specific month."""
        if 1 <= month_number <= 13:
            self.months[month_number]["name"] = new_name
            return True
        return False

    def get_constellation(self, date):
        """Get the constellation for a given date."""
        month = date.month
        day = date.day
        
        for constellation, dates in self.constellations.items():
            start_month, start_day = dates["start_date"]
            end_month, end_day = dates["end_date"]
            
            # Handle year wrap-around for Sagittarius
            if constellation == "Sagittarius":
                if month == 12 and day >= start_day:
                    return constellation
                if month == 1 and day < end_day:
                    return constellation
            
            # Normal date comparison
            if start_month == month and day >= start_day:
                return constellation
            if end_month == month and day < end_day:
                return constellation
            if start_month < month < end_month:
                return constellation
        
        return None
    
    def format_date(self, month, day):
        """Format a month and day as a readable date string."""
        return f"{self.month_names[month]} {day}" 

    def get_current_constellation(self) -> str:
        """Get the constellation for the current date."""
        current_date = datetime.now()
        month = current_date.month
        day = current_date.day
        
        for constellation, data in self.constellations.items():
            start_month, start_day = data["start_date"]
            end_month, end_day = data["end_date"]
            
            # Handle year wrap-around for Sagittarius
            if start_month > end_month:  # December to January
                if month == start_month and day >= start_day:
                    return constellation
                if month == end_month and day <= end_day:
                    return constellation
            else:
                if (month == start_month and day >= start_day) or \
                   (month == end_month and day <= end_day) or \
                   (start_month < month < end_month):
                    return constellation
        
        return "Scorpius"  # Default if no match found 