import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
df = pd.read_csv('../Data/Sickle/AH_Sickle_Cell_Disease_Provisional_Death_Counts_2019-2021.csv')
fig = px.treemap(df, path=[px.Constant("All Deaths"),'Date of Death Year','Quarter', 'Race or Hispanic Origin', 'Age Group'], values='SCD_Multi',
                  color='SCD_Multi', hover_data=['SCD_Multi'],
                  color_continuous_scale='Tealgrn', title='Sickle Cell Disease Provisional Death Counts')

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()