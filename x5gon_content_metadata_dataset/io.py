import pandas as pd

SEPARATOR = "|||"


def _split_text(text, sep=SEPARATOR):
    return [t.strip() for t in str(text).split(sep)]


def load_dataset(filepath):
    """Loads the x5gon metadata dataset from the specified path

    Args:
        filepath (str): filepath to the TSV file with metadata dataset

    Returns:
        data (DataFrame): A pandas DataFrame containing the metadata
                          Format of output file:
                                id (int): resource id of OER in the X5GON index. Useful to get more information using the API
                                title (str): Title of the Resource
                                type (str): File Type (can be video, audio, pdf etc...)
                                language (str): Language of the resource
                                keywords ([str]): A list of keywords extracted using AI
                                concepts ([str]): A list of Wikipedia concepts associated with the resource (using AI)
    """
    data = pd.read_csv(filepath, sep="\t")
    data["keywords"] = data["keywords"].apply(_split_text)
    data["concepts"] = data["concepts"].apply(_split_text)

    return data
