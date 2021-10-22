from tqdm import tqdm

filename = "./Data/bio-diseasome/bio-diseasome.mtx"
file = open(filename, "r")

comment_info = file.readline()

print(comment_info)

data_info = file.readline()

num_1 = int(data_info.split(" ")[0])
num_2 = int(data_info.split(" ")[1])
edge_count = int(data_info.split(" ")[2])


matrix = [[-1 for i in range(num_1)] for j in range(num_1)]

for lines in range(edge_count):
    edge = file.readline()
    start_node = int(edge.split(" ")[0])
    end_node = int(edge.split(" ")[1])

    if( matrix[start_node-1][end_node-1]==-1):
        matrix[start_node-1][end_node-1] = 1
        matrix[end_node-1][start_node-1] = 1

for i in range(num_1):
    for j in range(num_1):
        if(matrix[i][j] == -1):
            matrix[i][j] = 0

writeFile = "."+ filename.split(".")[1]+"-modified-matrix.csv"
writeAccess = open(writeFile, "w")

writeAccess.write("xval,yval,value\n")

for i in range(num_1):
    for j in range(num_1):
        writeAccess.write(str(i+1)+","+str(j+1)+","+str(matrix[i][j])+"\n")

writeAccess.close()