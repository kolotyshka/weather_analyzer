import pandas as pd
import numpy as np
import asyncio

from numpy.ma.core import anomalies


class WeatherData:

    def __init__(self, days = 5):
        self.days = days
        self.df = self.generate_data()

    def generate_data(self):
        temperatures = np.random.randint(0, 41, self.days)
        humidity = np.random.randint(0, 101, self.days)
        data = {
            'Day': [f"День {i+1}" for i in range(self.days)],
            'Temperature': temperatures,
            'Humidity': humidity
        }
        return pd.DataFrame(data)

    async def display_data(self):
        for _, row in self.df.iterrows():
            await asyncio.sleep(0.5)
            print(f"День: {row['Day']}, Температура: {row['Temperature']}°С, "
                  f"Влажность: {row['Humidity']}%")

    def find_anomalies(self):
        anomalies = self.df[
            (self.df['Temperature'] > 35) | (self.df['Humidity'] > 80)
        ]
        return anomalies

    async  def analyze_data(self):
        await self.display_data()
        anomalies = self.find_anomalies()
        print("\nАномалии (температура > 35°C или влажность > 80%):")
        for _, row in anomalies.iterrows():
            print(f"День: {row['Day']}, Температура: {row['Temperature']}°C, "
                  f"Влажность: {row['Humidity']}%")
        avg_temp = self.df['Temperature'].mean()
        avg_hum = self.df['Humidity'].mean()
        print(f"\nСредняя температура: {avg_temp:.1f}°C")
        print(f"Средняя влажность: {avg_hum:.1f}%")