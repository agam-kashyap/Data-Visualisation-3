from numpy import matrix
import plotly.graph_objects as go
import math

filename = "./Data/bio-diseasome/bio-diseasome.mtx"
file = open(filename, "r")
comment_info = file.readline()
print(comment_info)
data_info = file.readline()


n = int(data_info.split(" ")[0])
num_2 = int(data_info.split(" ")[1])
edge_count = int(data_info.split(" ")[2])
# one angle = 360/n
centerX = 0
centerY = 0

radius = 20
coordinatesX = []
coordinatesY = []

alpha = 2 * math.pi/n

for i in range(n):
    x2 = radius * math.cos((i)*alpha)
    y2 = radius * math.sin((i)*alpha)
    coordinatesX.append(x2)
    coordinatesY.append(y2)

node_trace = go.Scatter(
    x = coordinatesX,
    y = coordinatesY,

    mode = 'markers',
    hoverinfo='text',
    marker = dict(
        size = 5
    )
)

edgeX = []
edgeY = []

edgeS = []
edgeE = []


adj_matrix = [[0 for i in range(516)]for j in range(516)]

for lines in range(edge_count):
    edge = file.readline()
    start_node = int(edge.split(" ")[0])
    end_node = int(edge.split(" ")[1])
    edgeS.append(start_node)
    edgeE.append(end_node)
    adj_matrix[start_node-1][end_node-1]=1
    adj_matrix[end_node-1][start_node-1]=1

for i in range(len(edgeS)):
    startNode = edgeS[i]
    endNode = edgeE[i]

    startNode_x = coordinatesX[startNode-1]
    startNode_y = coordinatesY[startNode-1]
    endNode_x = coordinatesX[endNode-1]
    endNode_y = coordinatesY[endNode-1]

    edgeX.append(startNode_x)
    edgeX.append(endNode_x)
    edgeX.append(None)
    edgeY.append(startNode_y)
    edgeY.append(endNode_y)
    edgeY.append(None)

edge_trace = go.Scatter(
    x=edgeX, 
    y=edgeY,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_text = []
for node in range(n):
    s = "Node : "+str(node+1)
    s += "\nEnd: "
    for i in range(len(adj_matrix[node])):
        if(adj_matrix[node][i] == 1):
            s = s + " " + str(i+1)+ "\n"
    node_text.append(s)
node_trace.text = node_text


fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='Circular Graph for Network Data',
                titlefont_size=12,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)),
            )

fig.update_layout(width = 1000, height = 1000)
fig.show()