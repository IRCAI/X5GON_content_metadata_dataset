# Content Metadata Dataset from X5GON Project
This repository contains a dataset that has relevant metadata relating to majority of the Open Educational Resources indexed in X5GON project.

## Content data
These data can be found at [`datasets/v1/x5gon_metadata.tsv`](datasets/v1/x5gon_metadata.tsv)

## Dataset Composition

This dataset consists of 90,789 Open Educational Resources that are indexed in X5GON repository. The metadata consists 
of *six* informative columns. 

| Column Name | Description  |                                                                         Details                                                                         |
|-------------|--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------:|
| `id`        |  Material ID | This ID uniquely identifies the material in the X5GON database. This ID can be used to query more information from the X5GON API endpoint        |
| `title`     | Title        | The title of the OER material.                                                                                                                          |
| `type`      | Content Type | Specifies the modality of the OER material. Example types are video, audio, pdf, text etc...                                                            |
| `language`  | Language     | The primary language used in authoring the learning resource. This field is useful when identifying materials for different languages.                  |
| `keywords`  | Keywords     | A set of keywords extracted from material contents using Artificial Intelligence. The keywords are separated using "&#124;&#124;&#124;" .                            |
| `concepts`  | Concepts     | A set of Wikipedia Concepts extracted from material contents using Artificial Intelligence. The Wikipedia URLs of concepts are separated using "&#124;&#124;&#124;" |


## `x5gon_content_metadata_dataset` package

This repository also contains the `x5gon_content_metadata_dataset` package which contains all the helper functions that 
are required to loading and using the dataset seamlessly. The package currently contains the `load_dataset` function in 
the `x5gon_content_metadata_dataset.io` module. The following code snippet is an example of how the dataset can be 
loaded in Python programming language using the helper module. 

```python
# Import load_dataset function
from x5gon_content_metadata_dataset.io import load_dataset

# Load the x5gon_metadata.tsv dataset 
data = load_dataset("path/to/x5gon_metadata.tsv")
```
#### Google Colab Notebook

This [link](https://colab.research.google.com/drive/1-sv0m0JuV2gzec_QKChElf2sYyuSjLTy?usp=sharing) provides access to a 
Google Colab document that demonstrates how the dataset has been loaded in to the python environment.


## Supplementary Resources

The metadata in the dataset can be used to extract more information from the X5GON platform API endpoints. There are two
API endpoints that can be used. 

1. X5GON Rest API  : [https://platform.x5gon.org/products/feed#api](https://platform.x5gon.org/products/feed#api)
2. X5GON models API: [http://wp3.x5gon.org/lamapidoc](http://wp3.x5gon.org/lamapidoc)

You can visit the [tutorial colab notebook](https://colab.research.google.com/drive/1_Fb2wCVZlc810POJsy5zG4I3HgKfdQ1i) to see the API endpoints in action.

## License:

This work is licensed under a Creative Commons Attribution 4.0 International License. The full license details are found [here](https://creativecommons.org/licenses/by/4.0/).

## Authors

This dataset and support materials are created by
- Sahan Bulathwela
- Walid Ben Romdhane