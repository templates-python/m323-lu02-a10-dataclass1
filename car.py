"""
This module contains the Car dataclass.
"""
from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Car:
    """
    A simple Car class that contains the brand, mileage, and service dates.
    """
    brand: str
    mileage: int
    service_dates: List[str] = field(default_factory=list)
