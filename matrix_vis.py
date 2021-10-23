import plotly.graph_objects as go
import plotly.express as px

filename = "./Data/bio-diseasome/bio-diseasome-modified-matrix.csv"
file = open(filename, "r")

info = file.readline()
print(info)

data = [[-1 for i in range(516)] for j in range(516)]

for i in range(516):
    for j in range(516):
        line = file.readline().split(",")
        x = int(line[0])
        y = int(line[1])
        v = int(line[2])
        # if v==0:
        #     data[x-1][y-1] = None
        # else:
        data[x-1][y-1] = v

X = [i+1 for i in range(516)]
Y = [i+1 for i in range(516)]

# fig = go.Figure(data=go.Heatmap(
#                    z=data,
#                    x=X,
#                    y=Y,
#                    colorscale = [[0.0, '#FFFFFF'], [1.0, '#FF0012']]))

fig = px.imshow(data,
                labels=dict(x="Start Node", y="End Node", color="Edge Connectivity"),
                x=X,
                y=Y,
                color_continuous_scale='BuGn',
                zmin=0,
                zmax=1
               )
fig.update_layout(coloraxis_colorbar=dict(
    # thicknessmode="pixels", thickness=50,
    lenmode="pixels", len=200,
    # yanchor="top", y=1,
    # ticks="outside",
    tickvals=[0,1],
    ticktext=["No", "Yes"],
),
title='Matrix Visualisation for Node-Link Diagram',
width=1000)
fig.show()
