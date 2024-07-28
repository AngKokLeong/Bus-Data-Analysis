import numpy
import pandas

def systematic_sampling(dataframe: pandas.DataFrame, every_nth_member: int) -> pandas.DataFrame:

    generated_dataframe_index_based_on_criteria: list = numpy.arange(0, len(dataframe), step=every_nth_member)
    systematic_sampling = dataframe.iloc[generated_dataframe_index_based_on_criteria]

    return systematic_sampling