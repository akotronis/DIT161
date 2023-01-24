# General

This project is the project of 1st semester (2022-2023) course **Data Mining** of the postgraduate program **_Informatics and Telematics_** of **Harokopio University**.

- Analysis on U.S. International Air Traffic data (1990-2020) [datasets](https://www.kaggle.com/datasets/parulpandey/us-international-air-traffic-data?resource=download)
  - Data processing, transformation, Fact/Dimension tables
  - Analysis of 4 Business Scenarios
- Analysis on Air Traffic Passenger Statistics [dataset](https://catalog.data.gov/dataset/air-traffic-passenger-statistics)
  - Classification, Regression, Outlier analysis

# Files

- Main Project: [Jupyter notebook](https://github.com/akotronis/DIT161/blob/master/DIT161-Project.ipynb)
- Presentation 1 (Static): [Jupyter notebook](https://github.com/akotronis/DIT161/blob/master/DIT161-Presentation.ipynb)
- Presentation 2 (Dynamic): A `steamlit` app for dynamic visualization of 4 business scenarios

# Environment setup

- `>>> virtualenv − p python3 .venv`
- `>>> source .venv/bin/activate`
- `>>> pip3 install −r requirements.txt`

### Main Project (Jupyter)

- `>>> python3 -m ipykernel install --user --name=.venv` (`.venv` will appear in jupyter _Kernel_ &rarr; _Change kernel_ menu)

### Presentation 2 (`streamlit`)

- From root folder `>>> streamlit run src/app.py`
