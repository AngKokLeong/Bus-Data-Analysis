import numpy as np
import pandas as pd


def generate_bus_synthetic_data(number_of_samples: int, dataframe_column_name: list, trip_duration_data: dict, number_of_passenger_data: dict, distances_data: dict) -> pd.DataFrame:
    # Define the number of samples (bus trips) you want to generate
    num_samples = number_of_samples

    # Define the features you want to include in your synthetic data
    # For example, let's consider the following features:
    # 1. Trip duration (in minutes)
    # 2. Number of passengers
    # 3. Distance traveled (in kilometers)

    # Generate synthetic data for each feature from a normal distribution
    trip_durations = np.random.normal(trip_duration_data["mean"], trip_duration_data["standard_deviation"], size=num_samples)  # Mean = 30 mins, Std. Dev. = 10 mins
    num_passengers = np.random.normal(number_of_passenger_data["mean"], number_of_passenger_data["standard_deviation"], size=num_samples)  # Mean = 20 passengers, Std. Dev. = 5 passengers
    distances = np.random.normal(distances_data["mean"], distances_data["standard_deviation"], size=num_samples)  # Mean = 15 km, Std. Dev. = 5 km

    # Ensure non-negative values for certain features
    trip_durations = np.abs(trip_durations)
    num_passengers = np.abs(num_passengers)
    distances = np.abs(distances)

    #https://www.transitlink.com.sg/eservice/eguide/service_route.php?service=992


    column_name_list: list = dataframe_column_name


    synthetic_dataframe: pd.DataFrame = pd.DataFrame({column_name_list[0]: trip_durations, column_name_list[1]: num_passengers, column_name_list[2]: distances})

    return synthetic_dataframe





bus_870_synthetic_data: pd.DataFrame = generate_bus_synthetic_data( 164, 
                                                                    ["trip_durations", "num_passengers", "distances"],
                                                                    {
                                                                        "mean": 50,
                                                                        "standard_deviation": 1.5
                                                                    },
                                                                    {
                                                                        "mean": 50,
                                                                        "standard_deviation": 15
                                                                    },
                                                                    {
                                                                        "mean": 6.2,
                                                                        "standard_deviation": 0.01
                                                                    }
                                                                   )


bus_992_synthetic_data: pd.DataFrame = generate_bus_synthetic_data( 70, 
                                                                    ["trip_durations", "num_passengers", "distances"],
                                                                    {
                                                                        "mean": 40,
                                                                        "standard_deviation": 1.5
                                                                    },
                                                                    {
                                                                        "mean": 40,
                                                                        "standard_deviation": 10
                                                                    },
                                                                    {
                                                                        "mean": 6,
                                                                        "standard_deviation": 0.01
                                                                    }
                                                                   )

bus_870_synthetic_data.to_csv("bus_870_synthetic_data.csv")
bus_992_synthetic_data.to_csv("bus_992_synthetic_data.csv")