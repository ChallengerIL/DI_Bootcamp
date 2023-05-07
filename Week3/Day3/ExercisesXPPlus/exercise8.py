# 1. Given an age in seconds, calculate how old someone would be on:
#   - Earth: orbital period 365.25 Earth days, or 31557600 seconds
#   - Mercury: orbital period 0.2408467 Earth years
#   - Venus: orbital period 0.61519726 Earth years
#   - Mars: orbital period 1.8808158 Earth years
#   - Jupiter: orbital period 11.862615 Earth years
#   - Saturn: orbital period 29.447498 Earth years
#   - Uranus: orbital period 84.016846 Earth years
#   - Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

AGE_SECONDS = 1_000_000_000
SECONDS_IN_A_DAY = 86_400
EARTH_YEAR = 365.25


def calculate_celestial_age(planet: str, age_seconds: int):
    planets_data = {
        "mercury": 0.2408467, "venus": 0.61519726, "earth": 1, "mars": 1.8808158,
        "jupiter": 11.862615, "saturn": 29.447498, "uranus": 84.016846, "neptune": 164.79132,
    }

    if planet.lower() in planets_data:
        return round(((age_seconds / SECONDS_IN_A_DAY) / EARTH_YEAR) * planets_data[planet], 2)

    raise Exception("Unknown Planet! Try again...")


if __name__ == "__main__":
    print(calculate_celestial_age("earth", AGE_SECONDS))
    print(calculate_celestial_age("earth", 31557600))
    print(calculate_celestial_age("mars", AGE_SECONDS))
