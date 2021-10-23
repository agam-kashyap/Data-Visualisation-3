import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

sickle_df = pd.read_csv("./Data/Sickle/AH_Sickle_Cell_Disease_Provisional_Death_Counts_2019-2021.csv")

# Create dimensions
race_dim = go.parcats.Dimension(
    values=sickle_df["Race or Hispanic Origin"], label="Race"
)

quarter_dim = go.parcats.Dimension(
    values=sickle_df.Quarter, label="Quarter"
)

age_dim = go.parcats.Dimension(
    values=sickle_df["Age Group"], label="Age Group"
) 

scd_under_dim = go.parcats.Dimension(values=sickle_df.SCD_Underlying, label="SCD Underlying", categoryorder='category ascending')

scd_dim = go.parcats.Dimension(values=sickle_df["SCD and COVID-19"], label="SCD and COVID-19", categoryorder='category ascending')

scd_multi_dim = go.parcats.Dimension(values=sickle_df["SCD_Multi"], label="SCD Multi", categoryorder='category ascending')


# Create parcats trace
color = sickle_df.SCD_Underlying

trace1 = go.Parcats(dimensions=[age_dim, race_dim, scd_under_dim, quarter_dim],
        line={'color': color, 'colorscale': px.colors.sequential.Magenta},
        hoveron='category', hoverinfo='count',
        labelfont={'size': 18, 'family': 'Times'},
        tickfont={'size': 16, 'family': 'Times'},
        visible=False,
        arrangement='freeform')


trace2 = go.Parcats(dimensions=[age_dim, race_dim, scd_multi_dim, quarter_dim],
        line={'color': color, 'colorscale': px.colors.sequential.Magenta},
        hoveron='category', hoverinfo='count',
        labelfont={'size': 18, 'family': 'Times'},
        tickfont={'size': 16, 'family': 'Times'},
        visible=True,
        arrangement='freeform')


trace3 = go.Parcats(dimensions=[age_dim, race_dim, scd_dim, quarter_dim],
        line={'color': color, 'colorscale': px.colors.sequential.Magenta},
        hoveron='category', hoverinfo='count',
        labelfont={'size': 18, 'family': 'Times'},
        tickfont={'size': 16, 'family': 'Times'},
        visible=False,
        arrangement='freeform')

trace4 = go.Parcats(dimensions=[age_dim, race_dim, scd_under_dim, scd_multi_dim ,scd_dim, quarter_dim],
        line={'color': color, 'colorscale': px.colors.sequential.Magenta},
        hoveron='category', hoverinfo='count',
        labelfont={'size': 18, 'family': 'Times'},
        tickfont={'size': 16, 'family': 'Times'},
        visible=False,
        arrangement='freeform')

fig = go.Figure()
fig.add_trace(trace1)
fig.add_trace(trace2)
fig.add_trace(trace3)
fig.add_trace(trace4)

fig.update_layout(
    width=1900,
    height =  900
)

# Add dropdown
fig.update_layout(
    updatemenus=[
        dict( active=-1,
         buttons=list([   
            dict(label = 'SCD Underlying',
                 method = 'update',
                 args = [{'visible': [True, False, False, False]},
                         {'title': 'SCD Underlying Only'}]),

            dict(label = 'SCD Multi',
                 method = 'update',
                 args = [{'visible': [False, True, False, False]},
                         {'title': 'SCD Multi Only'}]),
            
            dict(label = 'SCD and COVID-19',
                 method = 'update',
                 args = [{'visible': [False, False, True, False]},
                         {'title': 'SCD and Covid-19 Only'}]),
            

            dict(label = 'All',
                 method = 'update',
                 args = [{'visible': [False, False, False, True]},
                         {'title': 'All'}])
         ]),
        )
    ]
)

fig.show()