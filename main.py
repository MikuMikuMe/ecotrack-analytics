Creating a comprehensive program like "EcoTrack-Analytics" is quite a broad task, but I'll provide you with a basic foundational Python program that captures the main ideas. This will include data parsing, basic analysis, and error handling to track a company's carbon footprint based on supply chain activities. For simplicity, the data will be simulated and stored in a CSV format.

```python
import csv
import random
import logging

# Logging configuration
logging.basicConfig(filename='ecotrack.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')


class EcoTrackAnalytics:
    def __init__(self, data_file):
        """
        Initialize the EcoTrackAnalytics with a path to CSV data file.
        
        :param data_file: Path to the supply chain data file
        """
        self.data_file = data_file
        self.supply_chain_data = []
        self.carbon_footprint = 0.0

    def load_data(self):
        """
        Load supply chain data from CSV file.
        """
        try:
            with open(self.data_file, 'r') as file:
                reader = csv.DictReader(file)
                self.supply_chain_data = [row for row in reader]
                logging.debug("Data loaded successfully from file."
                              f" Total records: {len(self.supply_chain_data)}")
        except FileNotFoundError:
            logging.error(f"File {self.data_file} not found.")
            raise Exception("The specified data file could not be found.")
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise Exception("An error occurred while loading data.")

    def calculate_carbon_footprint(self):
        """
        Simulate calculation of carbon footprint based on supply chain activities.
        """
        for record in self.supply_chain_data:
            try:
                distance = float(record.get('distance', 0))
                weight = float(record.get('weight', 0))
                mode = record.get('transport_mode', 'truck')

                emissions_factor = self.get_emissions_factor(mode)
                footprint = distance * weight * emissions_factor

                self.carbon_footprint += footprint
            except ValueError as e:
                logging.error(f"Value error while calculating footprint: {e}")
                continue
            except Exception as e:
                logging.error(f"Unexpected error during footprint calculation: {e}")
                continue

        logging.debug(f"Total carbon footprint calculated: {self.carbon_footprint}")

    @staticmethod
    def get_emissions_factor(mode):
        """
        Get emissions factor based on transport mode.
        
        :param mode: Mode of transportation
        :return: Emissions factor
        """
        emissions_factors = {
            'truck': 0.02,
            'train': 0.015,
            'ship': 0.01,
            'plane': 0.05
        }
        return emissions_factors.get(mode.lower(), 0.02)  # Default to truck

    def analyze_data(self):
        """
        Analyze the data to provide insights for reducing carbon footprint.
        """
        try:
            expensive_modes = ['plane']
            reduction_suggestions = []

            for record in self.supply_chain_data:
                if record.get('transport_mode') in expensive_modes:
                    suggestion = f"Consider alternative transport for order ID {record.get('order_id')}"
                    reduction_suggestions.append(suggestion)

            logging.debug(f"Generated {len(reduction_suggestions)} reduction suggestions.")
            return reduction_suggestions
        except Exception as e:
            logging.error(f"Error generating insights: {e}")
            throw Exception("An error occurred while generating insights.")


def main():
    # Assume we have sample data in 'supply_chain_data.csv'
    data_file = 'supply_chain_data.csv'

    # Initialize the tool
    eco_analytics = EcoTrackAnalytics(data_file)

    try:
        # Load the data
        eco_analytics.load_data()

        # Calculate the carbon footprint
        eco_analytics.calculate_carbon_footprint()

        # Analyze data
        suggestions = eco_analytics.analyze_data()
        if suggestions:
            print("Suggestions to reduce carbon footprint:")
            for suggestion in suggestions:
                print(suggestion)

        print(f"Total carbon footprint: {eco_analytics.carbon_footprint:.2f} CO2e")

    except Exception as e:
        print(f"An error occurred in processing: {e}")


if __name__ == "__main__":
    main()
```

### Notes:
- **Data Structure**: This program assumes that you have a CSV file named `supply_chain_data.csv` with columns such as `order_id`, `distance`, `weight`, and `transport_mode`.
- **Error Handling and Logging**: The program includes basic error handling by capturing exceptions and logging them in an external file (`ecotrack.log`). This ensures that the program can handle file-related issues and calculation errors gracefully.
- **Carbon Footprint Calculation**: The carbon footprint calculation is simulated using arbitrary emission factors. These should be updated based on real-world data.
- **Analysis Function**: Provides basic suggestions on transport mode changes for carbon footprint reduction. This can be expanded with more sophisticated analyses.

This program can be expanded by improving the dataset, enhancing the analysis, and integrating with external APIs or databases for real-world application.