from tqdm import tqdm

filename = "./Data/Sickle/AH_Sickle_Cell_Disease_Provisional_Death_Counts_2019-2021.csv"

file = open(filename, "r")

column_name = file.readline()

DateAsOf = []       # Data of analysis
DateOfDeath = []    # Date of death year
Quarter = []        # Data of death quarter
Race = []           # Race or Hispanic origin
Age = []            # Age group
SCD_Underlying = [] # Deaths with Sickle Cell Disease listed as underlying cause of death
SCD_Multi = []      # Deaths with Sickle Cell Disease listed as underlying or contributing cause of death
SCD = []            # Deaths with Sickle Cell Disease and COVID-19

while True: 
    # Get next line from file
    line = file.readline().split(",")
    
    if len(line)<2:
        break
    
    dAf = line[0]
    dOD = line[1]
    q = line[2]
    r = line[3]
    a = line[4]
    # <5 , 5-14, 15-19, 20-24, 25-39, 40-59, 60+ 
    scd_u = line[5]
    scd_m = line[6]
    scd = line[7]

    DateAsOf.append(dAf)
    DateOfDeath.append(dOD)
    Quarter.append(q)
    Race.append(r)
    Age.append(a)
    SCD_Underlying.append(int(scd_u))
    SCD_Multi.append(int(scd_m))
    SCD.append(int(scd))

file.close()

# Race Based division
writeRaceFile = "."+ filename.split(".")[1]+"-race-modified.json"
writeAccess = open(writeRaceFile, "w")

## name : "<Race Name>"
# {
#       children: [
#                  {"SCD": <scd>, "name": <id>},
#                   ]
# }

UniqueRace = []
for i in Race:
    if i not in UniqueRace:
        UniqueRace.append(i)

UniqueAge = []
for i in Age:
    if i not in UniqueAge:
        UniqueAge.append(i)

UniqueQuarter = []
for i in Quarter:
    if i not in UniqueQuarter:
        UniqueQuarter.append(i)

writeString = "{\"race\":\n"
writeString += "\t{\"name\": \"Race\", \"children\": [\n"
for i in UniqueRace:
    writeString+= "\t\t{"
    writeString+= "\"name\": "+"\""+ i + "\"" +", \"children\":[\n"

    for j in range(len(SCD)):
        if(Race[j]==i):
            writeString+= "\t\t\t{\"scd\": "+ str(SCD[j]) + ",\"name\": "+ str(j) + ",\"scd_underlying\": " +str(SCD_Underlying[j]) + ",\"scd_multi\": " +str(SCD_Multi[j]) + "},\n"
    writeString = writeString[:-2]
    writeString+= "]},\n"

writeString = writeString[:-2]
writeString += "\n\t]},\n"

writeString += "\"age\":\n"
writeString += "\t{\"name\": \"Age\", \"children\": [\n"
for i in UniqueAge:
    writeString+= "\t\t{"
    writeString+= "\"name\": "+"\""+ i + "\"" +", \"children\":[\n"

    for j in range(len(SCD)):
        if(Age[j]==i):
            writeString+= "\t\t\t{\"scd\": "+ str(SCD[j]) + ",\"name\": "+ str(j) + ",\"scd_underlying\": " +str(SCD_Underlying[j]) + ",\"scd_multi\": " +str(SCD_Multi[j]) + "},\n"
    writeString = writeString[:-2]
    writeString+= "]},\n"

writeString = writeString[:-2]
writeString += "\n\t]},\n"

writeString += "\"quarter\":\n"
writeString += "\t{\"name\": \"Quarter\", \"children\": [\n"
for i in UniqueQuarter:
    writeString+= "\t\t{"
    writeString+= "\"name\": "+"\""+ i + "\"" +", \"children\":[\n"

    for j in range(len(SCD)):
        if(Quarter[j]==i):
            writeString+= "\t\t\t{\"scd\": "+ str(SCD[j]) + ",\"name\": "+ str(j) + ",\"scd_underlying\": " +str(SCD_Underlying[j]) + ",\"scd_multi\": " +str(SCD_Multi[j]) + "},\n"
    writeString = writeString[:-2]
    writeString+= "]},\n"

writeString = writeString[:-2]
writeString += "\n\t]}\n"

writeString += "}" 

writeAccess.write(writeString)
writeAccess.close()