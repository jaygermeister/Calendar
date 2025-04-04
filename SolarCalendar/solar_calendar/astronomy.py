from datetime import datetime, timedelta
import ephem
import pytz
from typing import List, Dict

class AstronomicalEvents:
    def __init__(self):
        self.observer = ephem.Observer()
        self.observer.lat = '0'  # Default to equator
        self.observer.lon = '0'  # Default to prime meridian
        
    def get_upcoming_events(self, days_ahead: int = 30) -> List[Dict]:
        """Get upcoming astronomical events within the specified number of days."""
        events = []
        current_date = datetime.now()
        if current_date.tzinfo is None:
            current_date = current_date.replace(tzinfo=pytz.UTC)
        end_date = current_date + timedelta(days=days_ahead)
        
        # Calculate equinoxes and solstices
        events.extend(self._get_equinox_solstice_events(current_date, end_date))
        
        # Add other astronomical events (to be implemented)
        # - Lunar phases
        # - Eclipses
        # - Planetary alignments
        
        return sorted(events, key=lambda x: x['date'])
    
    def _get_equinox_solstice_events(self, start_date: datetime, end_date: datetime) -> List[Dict]:
        """Calculate equinox and solstice events between two dates."""
        if start_date.tzinfo is None:
            start_date = start_date.replace(tzinfo=pytz.UTC)
        if end_date.tzinfo is None:
            end_date = end_date.replace(tzinfo=pytz.UTC)
        
        events = []
        current_year = start_date.year
        
        while current_year <= end_date.year:
            # Spring equinox
            spring = ephem.next_vernal_equinox(f'{current_year}/1/1')
            spring_date = spring.datetime().replace(tzinfo=pytz.UTC)
            if start_date <= spring_date <= end_date:
                events.append({
                    'date': spring_date,
                    'type': 'equinox',
                    'name': 'Spring Equinox'
                })
            
            # Summer solstice
            summer = ephem.next_summer_solstice(f'{current_year}/1/1')
            summer_date = summer.datetime().replace(tzinfo=pytz.UTC)
            if start_date <= summer_date <= end_date:
                events.append({
                    'date': summer_date,
                    'type': 'solstice',
                    'name': 'Summer Solstice'
                })
            
            # Autumn equinox
            autumn = ephem.next_autumn_equinox(f'{current_year}/1/1')
            autumn_date = autumn.datetime().replace(tzinfo=pytz.UTC)
            if start_date <= autumn_date <= end_date:
                events.append({
                    'date': autumn_date,
                    'type': 'equinox',
                    'name': 'Autumn Equinox'
                })
            
            # Winter solstice
            winter = ephem.next_winter_solstice(f'{current_year}/1/1')
            winter_date = winter.datetime().replace(tzinfo=pytz.UTC)
            if start_date <= winter_date <= end_date:
                events.append({
                    'date': winter_date,
                    'type': 'solstice',
                    'name': 'Winter Solstice'
                })
            
            current_year += 1
        
        return events
    
    def get_equinox_solstice_dates(self, year: int) -> Dict:
        """Get all equinox and solstice dates for a given year."""
        dates = {
            'spring_equinox': ephem.next_vernal_equinox(f'{year}/1/1').datetime().replace(tzinfo=pytz.UTC),
            'summer_solstice': ephem.next_summer_solstice(f'{year}/1/1').datetime().replace(tzinfo=pytz.UTC),
            'autumn_equinox': ephem.next_autumn_equinox(f'{year}/1/1').datetime().replace(tzinfo=pytz.UTC),
            'winter_solstice': ephem.next_winter_solstice(f'{year}/1/1').datetime().replace(tzinfo=pytz.UTC)
        }
        return dates 

    def get_cross_quarter_dates(self, year: int) -> List[Dict]:
        """Calculate the cross-quarter dates (Imbolc, Beltane, Lughnasadh, Samhain) for a given year."""
        # Get the equinox and solstice dates for the year
        events = self._get_equinox_solstice_events(
            datetime(year, 1, 1, tzinfo=pytz.UTC),
            datetime(year, 12, 31, tzinfo=pytz.UTC)
        )
        
        # Sort events by date
        events.sort(key=lambda x: x['date'])
        
        # Calculate cross-quarter dates as midpoints between solstices and equinoxes
        cross_quarters = []
        for i in range(len(events)):
            current = events[i]
            next_event = events[(i + 1) % len(events)]
            
            # Calculate midpoint between current and next event
            time_diff = next_event['date'] - current['date']
            midpoint = current['date'] + time_diff / 2
            
            # Determine which cross-quarter this is
            if current['name'] == 'Winter Solstice' and next_event['name'] == 'Spring Equinox':
                name = 'Imbolc'
            elif current['name'] == 'Spring Equinox' and next_event['name'] == 'Summer Solstice':
                name = 'Beltane'
            elif current['name'] == 'Summer Solstice' and next_event['name'] == 'Autumn Equinox':
                name = 'Lughnasadh'
            elif current['name'] == 'Autumn Equinox' and next_event['name'] == 'Winter Solstice':
                name = 'Samhain'
            else:
                continue
                
            cross_quarters.append({
                'date': midpoint,
                'type': 'cross_quarter',
                'name': name
            })
        
        return cross_quarters 