import pandas as pd
import plotty.graph_objects as go
import csv

df=pd.read_csv("CR-107 data.csv")
student_df=df.loc[df["student_id"]=="TRL_987"]
fig=go.Figure(go.Bar(
    x=student_df.groupby("level")["attempt"].mean(),
    y=['level1','level2','level3','level4'],
    orientation='h'
))
fig.show()