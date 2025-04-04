"""
Planetary System Module

This module provides functionality for working with planets in the Solar Calendar & Tarot System.
It includes classes and functions for calculating planetary positions, aspects, and influences.
"""

import datetime
import math
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional, Union


class Element(Enum):
    """Elements associated with planets and constellations."""
    FIRE = "Fire"
    EARTH = "Earth"
    AIR = "Air"
    WATER = "Water"
    ETHER = "Ether"


class Planet(Enum):
    """Planets in the solar system."""
    SUN = "Sun"
    MOON = "Moon"
    MERCURY = "Mercury"
    VENUS = "Venus"
    MARS = "Mars"
    JUPITER = "Jupiter"
    SATURN = "Saturn"
    URANUS = "Uranus"
    NEPTUNE = "Neptune"
    PLUTO = "Pluto"


class DayOfWeek(Enum):
    """Days of the week with their planetary rulers."""
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class Aspect(Enum):
    """Astrological aspects between planets."""
    CONJUNCTION = "Conjunction"
    SEXTILE = "Sextile"
    SQUARE = "Square"
    TRINE = "Trine"
    OPPOSITION = "Opposition"


class Sephirah(Enum):
    """Sephirot of the Kabbalah Tree of Life."""
    KETER = "Keter"
    CHOKHMAH = "Chokhmah"
    BINAH = "Binah"
    CHESED = "Chesed"
    GEVURAH = "Gevurah"
    TIFERET = "Tiferet"
    NETZACH = "Netzach"
    HOD = "Hod"
    YESOD = "Yesod"
    MALKHUT = "Malkhut"


@dataclass
class PlanetaryPosition:
    """Represents a planet's position in the zodiac."""
    planet: Planet
    degree: float
    sign: str
    house: int
    is_retrograde: bool = False


@dataclass
class PlanetaryHour:
    """Represents a planetary hour of the day."""
    planet: Planet
    start_time: datetime.time
    end_time: datetime.time


@dataclass
class PlanetaryDay:
    """Represents a planetary day of the week."""
    day: DayOfWeek
    planet: Planet
    element: Element


@dataclass
class SephirahInfo:
    """Represents information about a Sephirah on the Tree of Life."""
    sephirah: Sephirah
    planet: Optional[Planet]
    element: Element
    tarot_cards: List[str]
    meaning: str
    hebrew_letter: str
    number: int
    color: str
    symbol: str


class PlanetarySystem:
    """Main class for planetary calculations and information."""
    
    def __init__(self):
        """Initialize the planetary system with default values."""
        self._initialize_planet_data()
        self._initialize_day_rulers()
        self._initialize_hour_sequence()
        self._initialize_sephirot()
    
    def _initialize_planet_data(self):
        """Initialize data for each planet."""
        self.planet_data = {
            Planet.SUN: {
                "element": Element.FIRE,
                "day": DayOfWeek.SUNDAY,
                "tarot_cards": ["The Sun", "The Emperor"],
                "influence": "Vitality, creativity, self-expression",
                "associated_constellation": "Leo",
                "jaygerian_period": "Radiance (July 23 - August 22)",
                "symbol": "☀️",
                "sephirah": Sephirah.TIFERET
            },
            Planet.MOON: {
                "element": Element.WATER,
                "day": DayOfWeek.MONDAY,
                "tarot_cards": ["The Moon", "The High Priestess"],
                "influence": "Emotions, intuition, cycles",
                "associated_constellation": "Cancer",
                "jaygerian_period": "Solis (June 13 - July 22)",
                "symbol": "🌙",
                "sephirah": Sephirah.YESOD
            },
            Planet.MERCURY: {
                "element": Element.AIR,
                "day": DayOfWeek.WEDNESDAY,
                "tarot_cards": ["The Magician", "The Hermit"],
                "influence": "Communication, intellect, adaptability",
                "associated_constellation": "Gemini",
                "jaygerian_period": "Zephyr (May 16 - June 12)",
                "symbol": "☿",
                "sephirah": Sephirah.HOD
            },
            Planet.VENUS: {
                "element": Element.EARTH,
                "day": DayOfWeek.FRIDAY,
                "tarot_cards": ["The Empress", "The Lovers"],
                "influence": "Love, beauty, harmony",
                "associated_constellation": "Taurus",
                "jaygerian_period": "Blossom (April 18 - May 15)",
                "symbol": "♀",
                "sephirah": Sephirah.NETZACH
            },
            Planet.MARS: {
                "element": Element.FIRE,
                "day": DayOfWeek.TUESDAY,
                "tarot_cards": ["The Tower", "The Chariot"],
                "influence": "Action, courage, passion",
                "associated_constellation": "Aries",
                "jaygerian_period": "Aurora (March 21 - April 17)",
                "symbol": "♂",
                "sephirah": Sephirah.GEVURAH
            },
            Planet.JUPITER: {
                "element": Element.AIR,
                "day": DayOfWeek.THURSDAY,
                "tarot_cards": ["The Wheel of Fortune", "The Hierophant"],
                "influence": "Expansion, wisdom, opportunity",
                "associated_constellation": "Sagittarius",
                "jaygerian_period": "Yule (December 21 - January 19)",
                "symbol": "♃",
                "sephirah": Sephirah.CHESED
            },
            Planet.SATURN: {
                "element": Element.EARTH,
                "day": DayOfWeek.SATURDAY,
                "tarot_cards": ["The World", "The Hanged Man"],
                "influence": "Structure, discipline, time",
                "associated_constellation": "Capricornus",
                "jaygerian_period": "Hearth (January 20 - February 17)",
                "symbol": "♄",
                "sephirah": Sephirah.BINAH
            },
            Planet.URANUS: {
                "element": Element.AIR,
                "tarot_cards": ["The Fool", "The Star"],
                "influence": "Innovation, awakening, disruption",
                "associated_constellation": "Aquarius",
                "jaygerian_period": "Twilight (February 18 - March 19)",
                "symbol": "⛢",
                "sephirah": Sephirah.CHOKHMAH
            },
            Planet.NEPTUNE: {
                "element": Element.WATER,
                "tarot_cards": ["The Hanged Man", "The Moon"],
                "influence": "Dreams, spirituality, illusion",
                "associated_constellation": "Pisces",
                "jaygerian_period": "Eclipse (March 1 - March 20)",
                "symbol": "♆",
                "sephirah": Sephirah.KETER
            },
            Planet.PLUTO: {
                "element": Element.WATER,
                "tarot_cards": ["Death", "The Tower"],
                "influence": "Transformation, power, regeneration",
                "associated_constellation": "Scorpius",
                "jaygerian_period": "Frost (November 23 - December 20)",
                "symbol": "♇",
                "sephirah": Sephirah.MALKHUT
            }
        }
    
    def _initialize_day_rulers(self):
        """Initialize the planetary rulers for each day of the week."""
        self.day_rulers = {
            DayOfWeek.SUNDAY: Planet.SUN,
            DayOfWeek.MONDAY: Planet.MOON,
            DayOfWeek.TUESDAY: Planet.MARS,
            DayOfWeek.WEDNESDAY: Planet.MERCURY,
            DayOfWeek.THURSDAY: Planet.JUPITER,
            DayOfWeek.FRIDAY: Planet.VENUS,
            DayOfWeek.SATURDAY: Planet.SATURN
        }
    
    def _initialize_hour_sequence(self):
        """Initialize the sequence of planetary hours."""
        self.hour_sequence = [
            Planet.SATURN,
            Planet.JUPITER,
            Planet.MARS,
            Planet.SUN,
            Planet.VENUS,
            Planet.MERCURY,
            Planet.MOON
        ]
    
    def _initialize_sephirot(self):
        """Initialize the Sephirot of the Kabbalah Tree of Life."""
        self.sephirot_data = {
            Sephirah.KETER: SephirahInfo(
                sephirah=Sephirah.KETER,
                planet=Planet.NEPTUNE,
                element=Element.ETHER,
                tarot_cards=["The Fool", "The World"],
                meaning="Crown, divine will, pure consciousness",
                hebrew_letter="א",
                number=1,
                color="White",
                symbol="👑"
            ),
            Sephirah.CHOKHMAH: SephirahInfo(
                sephirah=Sephirah.CHOKHMAH,
                planet=Planet.URANUS,
                element=Element.FIRE,
                tarot_cards=["The Magician", "The Emperor"],
                meaning="Wisdom, creative force, masculine energy",
                hebrew_letter="ב",
                number=2,
                color="Gray",
                symbol="🧠"
            ),
            Sephirah.BINAH: SephirahInfo(
                sephirah=Sephirah.BINAH,
                planet=Planet.SATURN,
                element=Element.WATER,
                tarot_cards=["The Empress", "The High Priestess"],
                meaning="Understanding, form, feminine energy",
                hebrew_letter="ג",
                number=3,
                color="Black",
                symbol="📚"
            ),
            Sephirah.CHESED: SephirahInfo(
                sephirah=Sephirah.CHESED,
                planet=Planet.JUPITER,
                element=Element.WATER,
                tarot_cards=["The Wheel of Fortune", "The Hierophant"],
                meaning="Mercy, love, abundance",
                hebrew_letter="ד",
                number=4,
                color="Blue",
                symbol="💙"
            ),
            Sephirah.GEVURAH: SephirahInfo(
                sephirah=Sephirah.GEVURAH,
                planet=Planet.MARS,
                element=Element.FIRE,
                tarot_cards=["The Tower", "The Chariot"],
                meaning="Strength, judgment, limitation",
                hebrew_letter="ה",
                number=5,
                color="Red",
                symbol="⚔️"
            ),
            Sephirah.TIFERET: SephirahInfo(
                sephirah=Sephirah.TIFERET,
                planet=Planet.SUN,
                element=Element.AIR,
                tarot_cards=["The Sun", "The Lovers"],
                meaning="Beauty, harmony, balance",
                hebrew_letter="ו",
                number=6,
                color="Yellow",
                symbol="☀️"
            ),
            Sephirah.NETZACH: SephirahInfo(
                sephirah=Sephirah.NETZACH,
                planet=Planet.VENUS,
                element=Element.FIRE,
                tarot_cards=["The Empress", "The Lovers"],
                meaning="Victory, endurance, passion",
                hebrew_letter="ז",
                number=7,
                color="Green",
                symbol="🌿"
            ),
            Sephirah.HOD: SephirahInfo(
                sephirah=Sephirah.HOD,
                planet=Planet.MERCURY,
                element=Element.WATER,
                tarot_cards=["The Magician", "The Hermit"],
                meaning="Splendor, communication, intellect",
                hebrew_letter="ח",
                number=8,
                color="Orange",
                symbol="📝"
            ),
            Sephirah.YESOD: SephirahInfo(
                sephirah=Sephirah.YESOD,
                planet=Planet.MOON,
                element=Element.AIR,
                tarot_cards=["The Moon", "The High Priestess"],
                meaning="Foundation, imagination, connection",
                hebrew_letter="ט",
                number=9,
                color="Purple",
                symbol="🌙"
            ),
            Sephirah.MALKHUT: SephirahInfo(
                sephirah=Sephirah.MALKHUT,
                planet=Planet.PLUTO,
                element=Element.EARTH,
                tarot_cards=["The World", "The Empress"],
                meaning="Kingdom, manifestation, physical world",
                hebrew_letter="י",
                number=10,
                color="Brown",
                symbol="🌍"
            )
        }
    
    def get_planet_info(self, planet: Planet) -> Dict:
        """Get information about a specific planet."""
        return self.planet_data.get(planet, {})
    
    def get_day_ruler(self, day: DayOfWeek) -> Planet:
        """Get the planetary ruler for a specific day of the week."""
        return self.day_rulers.get(day)
    
    def get_planetary_hours(self, date: datetime.date) -> List[PlanetaryHour]:
        """
        Calculate the planetary hours for a specific date.
        
        Args:
            date: The date to calculate planetary hours for.
            
        Returns:
            A list of PlanetaryHour objects for the 24-hour period.
        """
        # This is a simplified calculation. In a real implementation,
        # you would use astronomical calculations to determine sunrise and sunset.
        sunrise = datetime.time(6, 0)  # Simplified sunrise at 6:00 AM
        sunset = datetime.time(18, 0)  # Simplified sunset at 6:00 PM
        
        # Calculate the length of day and night hours
        day_hours = (sunset.hour - sunrise.hour) + (sunset.minute - sunrise.minute) / 60
        night_hours = 24 - day_hours
        
        # Calculate the length of each planetary hour
        day_hour_length = day_hours / 12  # 12 planetary hours during the day
        night_hour_length = night_hours / 12  # 12 planetary hours during the night
        
        # Determine the first planetary hour based on the day of the week
        day_index = date.weekday()
        first_hour_planet = self.hour_sequence[day_index]
        
        # Create the list of planetary hours
        hours = []
        current_time = datetime.datetime.combine(date, sunrise)
        
        # Day hours
        for i in range(12):
            planet_index = (day_index + i) % 7
            planet = self.hour_sequence[planet_index]
            
            start_time = current_time.time()
            end_time = (current_time + datetime.timedelta(hours=day_hour_length)).time()
            
            hours.append(PlanetaryHour(planet, start_time, end_time))
            current_time += datetime.timedelta(hours=day_hour_length)
        
        # Night hours
        for i in range(12):
            planet_index = (day_index + 12 + i) % 7
            planet = self.hour_sequence[planet_index]
            
            start_time = current_time.time()
            end_time = (current_time + datetime.timedelta(hours=night_hour_length)).time()
            
            hours.append(PlanetaryHour(planet, start_time, end_time))
            current_time += datetime.timedelta(hours=night_hour_length)
        
        return hours
    
    def calculate_aspect(self, planet1_pos: PlanetaryPosition, planet2_pos: PlanetaryPosition) -> Optional[Aspect]:
        """
        Calculate the aspect between two planets.
        
        Args:
            planet1_pos: The position of the first planet.
            planet2_pos: The position of the second planet.
            
        Returns:
            The aspect between the two planets, or None if no significant aspect exists.
        """
        # Calculate the angular distance between the two planets
        angle = abs(planet1_pos.degree - planet2_pos.degree)
        
        # Check for aspects (with a 5-degree orb)
        orb = 5
        
        if angle <= orb or angle >= 360 - orb:
            return Aspect.CONJUNCTION
        elif 55 <= angle <= 65 or 295 <= angle <= 305:
            return Aspect.SEXTILE
        elif 85 <= angle <= 95 or 265 <= angle <= 275:
            return Aspect.SQUARE
        elif 115 <= angle <= 125 or 235 <= angle <= 245:
            return Aspect.TRINE
        elif 175 <= angle <= 185:
            return Aspect.OPPOSITION
        
        return None
    
    def is_retrograde(self, planet: Planet, date: datetime.date) -> bool:
        """
        Determine if a planet is retrograde on a specific date.
        
        Args:
            planet: The planet to check.
            date: The date to check.
            
        Returns:
            True if the planet is retrograde, False otherwise.
        """
        # This is a simplified implementation. In a real system,
        # you would use astronomical calculations to determine retrograde periods.
        
        # Example retrograde periods (simplified)
        retrograde_periods = {
            Planet.MERCURY: [
                (datetime.date(2023, 4, 21), datetime.date(2023, 5, 14)),
                (datetime.date(2023, 8, 23), datetime.date(2023, 9, 15)),
                (datetime.date(2023, 12, 13), datetime.date(2024, 1, 1))
            ],
            Planet.VENUS: [
                (datetime.date(2023, 7, 23), datetime.date(2023, 9, 3))
            ],
            Planet.MARS: [
                (datetime.date(2022, 10, 30), datetime.date(2023, 1, 12))
            ],
            Planet.JUPITER: [
                (datetime.date(2023, 9, 4), datetime.date(2023, 12, 31))
            ],
            Planet.SATURN: [
                (datetime.date(2023, 6, 17), datetime.date(2023, 11, 4))
            ]
        }
        
        if planet not in retrograde_periods:
            return False
        
        for start_date, end_date in retrograde_periods[planet]:
            if start_date <= date <= end_date:
                return True
        
        return False
    
    def get_planetary_day(self, date: datetime.date) -> PlanetaryDay:
        """
        Get the planetary day for a specific date.
        
        Args:
            date: The date to get the planetary day for.
            
        Returns:
            A PlanetaryDay object representing the planetary day.
        """
        day_of_week = DayOfWeek(date.strftime("%A").upper())
        planet = self.get_day_ruler(day_of_week)
        element = self.planet_data[planet]["element"]
        
        return PlanetaryDay(day_of_week, planet, element)
    
    def get_planetary_hour(self, date_time: datetime.datetime) -> PlanetaryHour:
        """
        Get the planetary hour for a specific date and time.
        
        Args:
            date_time: The date and time to get the planetary hour for.
            
        Returns:
            A PlanetaryHour object representing the current planetary hour.
        """
        hours = self.get_planetary_hours(date_time.date())
        
        for hour in hours:
            if hour.start_time <= date_time.time() < hour.end_time:
                return hour
        
        # If we get here, we're in the last hour of the day
        return hours[-1]
    
    def get_planet_for_date(self, date: datetime.date) -> Planet:
        """
        Get the planet associated with a specific date in the Jaygerian calendar.
        
        Args:
            date: The date to get the planet for.
            
        Returns:
            The planet associated with the date.
        """
        # This is a simplified implementation. In a real system,
        # you would use the Jaygerian calendar to determine the planet.
        
        # Example mapping of Jaygerian months to planets
        month_to_planet = {
            "Aurora": Planet.MARS,
            "Blossom": Planet.VENUS,
            "Zephyr": Planet.MERCURY,
            "Solis": Planet.MOON,
            "Radiance": Planet.SUN,
            "Ember": Planet.MARS,
            "Harvest": Planet.VENUS,
            "Equinox": Planet.MERCURY,
            "Frost": Planet.PLUTO,
            "Yule": Planet.JUPITER,
            "Hearth": Planet.SATURN,
            "Twilight": Planet.URANUS,
            "Eclipse": Planet.NEPTUNE
        }
        
        # In a real implementation, you would convert the date to the Jaygerian calendar
        # and look up the planet based on the month.
        
        # For now, we'll return a default planet
        return Planet.SUN
    
    def get_sephirah_info(self, sephirah: Sephirah) -> SephirahInfo:
        """
        Get information about a specific Sephirah.
        
        Args:
            sephirah: The Sephirah to get information for.
            
        Returns:
            A SephirahInfo object containing information about the Sephirah.
        """
        return self.sephirot_data.get(sephirah)
    
    def get_sephirah_for_planet(self, planet: Planet) -> Optional[Sephirah]:
        """
        Get the Sephirah associated with a specific planet.
        
        Args:
            planet: The planet to get the Sephirah for.
            
        Returns:
            The Sephirah associated with the planet, or None if no Sephirah is associated.
        """
        for sephirah, info in self.sephirot_data.items():
            if info.planet == planet:
                return sephirah
        
        return None
    
    def get_planet_for_sephirah(self, sephirah: Sephirah) -> Optional[Planet]:
        """
        Get the planet associated with a specific Sephirah.
        
        Args:
            sephirah: The Sephirah to get the planet for.
            
        Returns:
            The planet associated with the Sephirah, or None if no planet is associated.
        """
        info = self.sephirot_data.get(sephirah)
        if info:
            return info.planet
        
        return None
    
    def get_path_between_sephirot(self, sephirah1: Sephirah, sephirah2: Sephirah) -> List[str]:
        """
        Get the Hebrew letters that form the path between two Sephirot.
        
        Args:
            sephirah1: The first Sephirah.
            sephirah2: The second Sephirah.
            
        Returns:
            A list of Hebrew letters that form the path between the two Sephirot.
        """
        # This is a simplified implementation. In a real system,
        # you would use the actual paths on the Tree of Life.
        
        # Example paths (simplified)
        paths = {
            (Sephirah.KETER, Sephirah.CHOKHMAH): ["א", "ב"],
            (Sephirah.KETER, Sephirah.BINAH): ["א", "ג"],
            (Sephirah.CHOKHMAH, Sephirah.BINAH): ["ב", "ג"],
            (Sephirah.CHOKHMAH, Sephirah.CHESED): ["ב", "ד"],
            (Sephirah.CHOKHMAH, Sephirah.TIFERET): ["ב", "ו"],
            (Sephirah.BINAH, Sephirah.GEVURAH): ["ג", "ה"],
            (Sephirah.BINAH, Sephirah.TIFERET): ["ג", "ו"],
            (Sephirah.CHESED, Sephirah.GEVURAH): ["ד", "ה"],
            (Sephirah.CHESED, Sephirah.TIFERET): ["ד", "ו"],
            (Sephirah.CHESED, Sephirah.NETZACH): ["ד", "ז"],
            (Sephirah.GEVURAH, Sephirah.TIFERET): ["ה", "ו"],
            (Sephirah.GEVURAH, Sephirah.HOD): ["ה", "ח"],
            (Sephirah.TIFERET, Sephirah.NETZACH): ["ו", "ז"],
            (Sephirah.TIFERET, Sephirah.HOD): ["ו", "ח"],
            (Sephirah.TIFERET, Sephirah.YESOD): ["ו", "ט"],
            (Sephirah.NETZACH, Sephirah.HOD): ["ז", "ח"],
            (Sephirah.NETZACH, Sephirah.YESOD): ["ז", "ט"],
            (Sephirah.NETZACH, Sephirah.MALKHUT): ["ז", "י"],
            (Sephirah.HOD, Sephirah.YESOD): ["ח", "ט"],
            (Sephirah.HOD, Sephirah.MALKHUT): ["ח", "י"],
            (Sephirah.YESOD, Sephirah.MALKHUT): ["ט", "י"]
        }
        
        # Check if the path exists
        if (sephirah1, sephirah2) in paths:
            return paths[(sephirah1, sephirah2)]
        elif (sephirah2, sephirah1) in paths:
            return paths[(sephirah2, sephirah1)]
        
        # If no direct path exists, return an empty list
        return []
    
    def get_sephirah_for_date(self, date: datetime.date) -> Sephirah:
        """
        Get the Sephirah associated with a specific date in the Jaygerian calendar.
        
        Args:
            date: The date to get the Sephirah for.
            
        Returns:
            The Sephirah associated with the date.
        """
        # This is a simplified implementation. In a real system,
        # you would use the Jaygerian calendar to determine the Sephirah.
        
        # Example mapping of Jaygerian months to Sephirot
        month_to_sephirah = {
            "Aurora": Sephirah.GEVURAH,
            "Blossom": Sephirah.NETZACH,
            "Zephyr": Sephirah.HOD,
            "Solis": Sephirah.YESOD,
            "Radiance": Sephirah.TIFERET,
            "Ember": Sephirah.GEVURAH,
            "Harvest": Sephirah.NETZACH,
            "Equinox": Sephirah.HOD,
            "Frost": Sephirah.MALKHUT,
            "Yule": Sephirah.CHESED,
            "Hearth": Sephirah.BINAH,
            "Twilight": Sephirah.CHOKHMAH,
            "Eclipse": Sephirah.KETER
        }
        
        # In a real implementation, you would convert the date to the Jaygerian calendar
        # and look up the Sephirah based on the month.
        
        # For now, we'll return a default Sephirah
        return Sephirah.TIFERET


# Example usage
if __name__ == "__main__":
    planetary_system = PlanetarySystem()
    
    # Get information about the Sun
    sun_info = planetary_system.get_planet_info(Planet.SUN)
    print(f"Sun: {sun_info}")
    
    # Get the planetary ruler for Monday
    monday_ruler = planetary_system.get_day_ruler(DayOfWeek.MONDAY)
    print(f"Monday is ruled by: {monday_ruler.value}")
    
    # Get the planetary day for today
    today = datetime.date.today()
    planetary_day = planetary_system.get_planetary_day(today)
    print(f"Today is {planetary_day.day.value}, ruled by {planetary_day.planet.value}")
    
    # Get the current planetary hour
    now = datetime.datetime.now()
    current_hour = planetary_system.get_planetary_hour(now)
    print(f"The current planetary hour is ruled by {current_hour.planet.value}")
    
    # Check if Mercury is retrograde
    is_mercury_retrograde = planetary_system.is_retrograde(Planet.MERCURY, today)
    print(f"Is Mercury retrograde? {is_mercury_retrograde}")
    
    # Get information about Tiferet
    tiferet_info = planetary_system.get_sephirah_info(Sephirah.TIFERET)
    print(f"Tiferet: {tiferet_info}")
    
    # Get the Sephirah associated with the Sun
    sun_sephirah = planetary_system.get_sephirah_for_planet(Planet.SUN)
    print(f"The Sun is associated with the Sephirah: {sun_sephirah.value}")
    
    # Get the path between Keter and Tiferet
    path = planetary_system.get_path_between_sephirot(Sephirah.KETER, Sephirah.TIFERET)
    print(f"The path between Keter and Tiferet is: {path}") 