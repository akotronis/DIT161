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

Windows terminal:

- `>>> python -m venv venvname`
- `>>> venvname\Scripts\activate`
- `>>> python -m pip install −- upgrade pip` (To avoid potential `psutil` error)
- `>>> python -m pip install −r requirements.txt`

### Main Project (Jupyter)

- [To add kernel to jupyter](https://stackoverflow.com/questions/42449814/running-jupyter-notebook-in-a-virtualenv-installed-sklearn-module-not-available) `>>> python -m ipykernel install --user --name=venvname` (`venvname` will appear in jupyter _Kernel_ &rarr; _Change kernel_ menu and can be a custom name, not necessarily the same as `venvname`)
- To list existing jupyter kernels `>>> jupyter kernelspec list`
- [To change the display name of a kernel](https://stackoverflow.com/questions/45085233/jupyter-kernel-is-there-a-way-to-rename-them)
  - List existing jupyter kernels with the step above to see kernel paths
  - Edit the `display_name` property in the `kernel.json` file of the correspnding path
- To [remove the specific kernel from jupyter](https://stackoverflow.com/questions/42635310/remove-kernel-on-jupyter-notebook) `>>>jupyter kernelspec uninstall venvname`

### Presentation 2 (`streamlit`)

- From root folder `>>> streamlit run src/app.py`
- Visit `http://localhost:8501/` to see the app running
