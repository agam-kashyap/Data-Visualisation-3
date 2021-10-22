from tqdm import tqdm

filename = "./Data/bio-diseasome/bio-diseasome.mtx"
file = open(filename, "r")

comment_info = file.readline()

print(comment_info)

data_info = file.readline()

num_1 = int(data_info.split(" ")[0])
num_2 = int(data_info.split(" ")[1])
edge_count = int(data_info.split(" ")[2])

nodes_array = []
edge_list = []

for lines in tqdm(range(edge_count)):
    edge = file.readline()
    start_node = int(edge.split(" ")[0])
    end_node = int(edge.split(" ")[1])

    if(start_node not in nodes_array): nodes_array.append(start_node)
    if(end_node not in nodes_array): nodes_array.append(end_node)

    edge_list.append([start_node, end_node])

writeFile = "."+ filename.split(".")[1]+"-modified.json"
writeAccess = open(writeFile, "w")

writeAccess.write("{ \"nodes\": [\n ")

nodes_array = sorted(nodes_array)
for i in range(len(nodes_array)):
    if(i+1 == len(nodes_array)): temp = "\t { \"id\": " + str(nodes_array[i]) +" }\n"
    else : temp = "\t { \"id\": " + str(nodes_array[i]) +" },\n"
    writeAccess.write(temp)

writeAccess.write("  ],\n  \"links\": [\n")

for i in range(len(edge_list)):
    if i+1 == len(edge_list): temp = "\t { \"source\": " + str(edge_list[i][0]) + ", \"target\": " + str(edge_list[i][1]) +" }\n"
    else : temp = "\t { \"source\": " + str(edge_list[i][0]) + ", \"target\": " + str(edge_list[i][1]) +" },\n"
    writeAccess.write(temp)

writeAccess.write(" ]}")