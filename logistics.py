#Uploading the csv
from google.colab import files
data_to_load = files.upload()

import pandas as pd
import plotly.express as px

df = pd.read_csv("escape_velocity.csv")

velocity_list = df["Velocity"].tolist()
escaped_list = df["Escaped"].tolist()

fig = px.scatter(x=velocity_list, y=escaped_list)
fig.show()

#Uploading the csv
from google,colab import files
data_to_load = files.upload()

import pandas as pd 
import plotly.express as px

df = pd,read_csv("escape_velocity/csv")

velocity_list = df["Velocity"].tolist()
escaped_list = df["Escaped"].tolist()

fig = px.scatter(x=velocity_list. y=escaped_list)
fig.show()


