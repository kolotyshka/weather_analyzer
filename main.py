import asyncio
from weather_data import WeatherData

async def main():
    weather = WeatherData()
    await weather.analyze_data()

if __name__ == "__main__":
    asyncio.run(main())