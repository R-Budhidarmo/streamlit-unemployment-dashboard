# Streamlit Dashboard - World Bank Unemployment Rate Data

The dashboard was made using [Streamlit](https://streamlit.io/). For this particular exercise, global unemployment rate data from [World Bank](https://www.worldbank.org/en/home) were used as the basis of this web app. The data were retrieved from [Kaggle](https://www.kaggle.com/datasets/theworldbank/health-nutrition-and-population-statistics). Therefore, it's not meant to show the latest data.
<br>*In the future, I'll do the next version of this web app incorporating [World Bank's official API](https://blogs.worldbank.org/opendata/introducing-wbgapi-new-python-package-accessing-world-bank-data), so watch this space* 

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Acknowledgement](#acknowledgement)

---

## Installation

To run the web app, you will need to install the following libraries: ```streamlit```, ```pandas```, and ```plotly```. If you'd like to perform the EDA as well, you'll also need ```kaggle``` API.
<br> You can also simply download all the required libraries as fololows:

```bash
pip install -r requirements.txt
```

---

## Configuration

None at the moment. This is a simple web app, so there's not need to do anything with the ```~/.streamlit/config.toml``` file to run it.

---

## Usage

There's no need to perform EDA again since the data have been saved in ```/data/unemployment_reshaped.csv``` but if you'd like to, feel free to look at the [Jupyter notebook](https://github.com/R-Budhidarmo/streamlit-unemployment-dashboard/blob/main/EDA.ipynb) & run it.

To run the web app, navigate to your working directory and execute the `app.py` as follows:

```bash
streamlit run app.py
```

On the browser, the web app looks like the screenshots below:

![output1](https://github.com/R-Budhidarmo/streamlit-unemployment-dashboard/blob/main/app_screenshot1.png)
![output2](https://github.com/R-Budhidarmo/streamlit-unemployment-dashboard/blob/main/app_screenshot2.png)

## Acknowledgement

This dashboard was inspired by a [repo](https://github.com/dataprofessor/population-dashboard/tree/master) by @dataprofessor.
