# Udacity Data Science Capstone Project: Stock Price Prediction

## Introduction
For this project, the task was to build a stock price predictor that takes daily trading data over a certain date range as input, and outputs projected estimates for given query dates.
As a predictor model, a ARIMA timeseries forecast model was choosen.

The project is divided into three seperate notebooks/apps/scripts:
1. Stock data analysis and model evaluation, located in the `arima_model_selection.ipynb` jupyter notebook.
2. Model creation (obtaining data and model training) and data serialization, located in the `make_model.ipynb` jupyter notebook.
3. Data Visualition of pretrained models via a web app based on Plotly Dash framework (`app.py`)

## Screenshot of the web app
![initial](img/img1.png)

## Requirements
I suggest you to create a separate virtual environment running Python 3 for this project, and install all of the required dependencies there. Run in Terminal/Command Prompt:

```
git clone https://github.com/xseibel/uda_ds_final.git
cd uda_ds_final
python3 -m virtualenv venv
```
In UNIX system: 

```
source venv/bin/activate
```
In Windows: 

```
venv\Scripts\activate
```

To install all of the required packages to this environment, simply run:

```
pip install -r requirements.txt
```

and all of the required `pip` packages, will be installed, and the web app as well as the jupyter notebooks will be able to run.


## How to use the web app

Run this app locally by:
```
python app.py
```
Open http://0.0.0.0:8050/ in your browser, you will a chart with pretrained stock symbols.

## How to use the jupyter notebooks

Run the notebooks locally by:
```
jupyter notebook
```
A browser window will open and you can open one of the notebooks.
See Comments in the notebooks for fruther instructions on how to use them.
