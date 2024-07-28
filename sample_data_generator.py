import numpy, pandas, scipy, math

def generate_confidence_interval_for_t_test_with_unknown_sigma(significance_level: float, sample_mean: float, sample_standard_deviation: float, data_source: pandas.Series) -> dict:
    number_of_samples: int = len(data_source)
    degree_of_freedom: int = number_of_samples - 1
    critical_value: float = scipy.stats.t.ppf(significance_level, degree_of_freedom)

    # Using the t-test and assume population standard deviation is unknown

    lower_bound_confidence_interval:float = sample_mean - (critical_value * (sample_standard_deviation / math.sqrt(number_of_samples)))
    upper_bound_confidence_interval:float = sample_mean + (critical_value * (sample_standard_deviation / math.sqrt(number_of_samples)))

    return {
            "Sample_Mean": sample_mean, 
            "Lower Bound Confidence Interval": lower_bound_confidence_interval, 
            "Upper Bound Confidence Interval": upper_bound_confidence_interval
            }

def generate_confidence_interval_for_z_test_with_known_sigma(significance_level: float, sample_mean: float, standard_deviation: float, data_source: pandas.Series) -> dict:
    number_of_samples: int = len(data_source)
    degree_of_freedom: int = number_of_samples - 1
    z_critical_value: float = scipy.stats.norm.ppf(1-significance_level)

    lower_bound_confidence_interval:float = sample_mean - (z_critical_value * (standard_deviation / math.sqrt(number_of_samples)))
    upper_bound_confidence_interval :float = sample_mean + (z_critical_value * (standard_deviation / math.sqrt(number_of_samples)))

    return {
            "Sample_Mean": sample_mean, 
            "Lower Bound Confidence Interval": lower_bound_confidence_interval, 
            "Upper Bound Confidence Interval": upper_bound_confidence_interval
            }



def systematic_sampling(dataframe: pandas.DataFrame, every_nth_member: int) -> pandas.DataFrame:

    generated_dataframe_index_based_on_criteria: list = numpy.arange(0, len(dataframe), step=every_nth_member)
    systematic_sampling = dataframe.iloc[generated_dataframe_index_based_on_criteria]

    return systematic_sampling

