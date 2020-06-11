import csv
begin = 0.00
end = 0.01
increment = 0.1
files = []
bucketname = input("Enter the name of your bucket : ")
videoName = input("Enter the name of your video + Extension : ")
try :
    duration = int(input("Enter the video duration in seconds : "))*10
except Exception as e:
    print("Error in the duration",type(e).__name__)
    exit(0)
labelName = input("Enter your label : ") 
bucket = "gs://" + bucketname + "/" + videoName + "," + labelName
files.append((bucket + "," + str(begin) + "," + str(end)))
for i in range(0,duration):
    begin += increment
    end += increment
    objects  = bucket + "," + str(round(begin,2)) + "," + str(round(end,2))
    files.append(objects)
with open(videoName+".csv","w") as myCsv:
    writer = csv.writer(myCsv,delimiter="\n")
    writer.writerow(files)

