from datetime import datetime, timedelta
import ephem
import pytz
from typing import List, Dict

class ZodiacCalculator:
    def __init__(self):
        self.constellations = [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius",
            "Pisces", "Ophiuchus"
        ]
        self.observer = ephem.Observer()
        self.observer.lat = '0'  # Default to equator
        self.observer.lon = '0'  # Default to prime meridian
        
    def get_current_constellation(self) -> Dict:
        """Get the current zodiac constellation the sun is in."""
        current_date = datetime.now(pytz.UTC)
        return self._get_constellation_for_date(current_date)
    
    def _get_constellation_for_date(self, date: datetime) -> Dict:
        """Determine which constellation the sun is in on a given date."""
        self.observer.date = date
        sun = ephem.Sun(self.observer)
        
        # Calculate the sun's position in the ecliptic
        # This is a simplified version - actual implementation would need
        # more precise calculations based on constellation boundaries
        constellation_index = int((sun.ra * 12) / ephem.pi)
        
        return {
            'name': self.constellations[constellation_index],
            'start_date': date,
            'end_date': date + timedelta(days=28)  # Approximate duration
        }
    
    def get_transition_dates(self, year: int) -> List[Dict]:
        """Get the dates when the sun transitions between constellations."""
        transitions = []
        current_date = datetime(year, 1, 1, tzinfo=pytz.UTC)
        end_date = datetime(year, 12, 31, tzinfo=pytz.UTC)
        
        while current_date <= end_date:
            constellation = self._get_constellation_for_date(current_date)
            transitions.append({
                'date': current_date,
                'from_constellation': constellation['name'],
                'to_constellation': self.constellations[
                    (self.constellations.index(constellation['name']) + 1) % 13
                ]
            })
            current_date += timedelta(days=28)  # Approximate transition period
        
        return transitions
    
    def get_constellation_dates(self, year: int) -> Dict:
        """Get the start and end dates for each constellation in a given year."""
        constellation_dates = {}
        current_date = datetime(year, 1, 1, tzinfo=pytz.UTC)
        
        for constellation in self.constellations:
            start_date = current_date
            end_date = start_date + timedelta(days=28)  # Approximate duration
            constellation_dates[constellation] = {
                'start_date': start_date,
                'end_date': end_date
            }
            current_date = end_date
        
        return constellation_dates 