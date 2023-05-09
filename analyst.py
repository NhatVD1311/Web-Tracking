import json
import csv
sum = 0
data_new = []
data_final = []
with open('lightbeamData1.json') as json_file:
    data = json.load(json_file)
    file = open("lightbeamData1.csv", "w+")
    csv_file = csv.writer(file)
    for i in data:
        t = data[i]
        if t['firstParty'] == True:
            for j in t['thirdParties']:
                data_new.append(j)
    #print(data_final)
    for p in data_new:
        data_final.append(p.split(".")[-2] + "." + p.split(".")[-1])
    data_no_dup = list(dict.fromkeys(data_final))
    my_dict = {i:data_final.count(i) for i in data_final}
    for i in data_new:
        sum = sum + 1
    # file.writelines(["Tong so domain: ", str(sum), "\n"])
    # for i in data_new:
    #     #count = 0
    #     #count=count+1
    #     file.writelines(["So lan xuat hien domain: ", str(i), " là: ", str(data_new.count(i)), " - Chiem: ", str(data_new.count(i)/sum*100), "%\n"])
    #str = {"So lan xuat hien domain: " + str(i) + " là: " + str(data_final.count(i)) + " - Chiem: " + str(data_final.count(i)/sum*100) + "%\n" for i in data_final}
    csv_file.writerow(["Domain", "So luong", "Chiem(%)"])
    for j in data_no_dup:
        csv_file.writerow([str(j), str(data_final.count(j)), str(data_final.count(j)/sum*100)])
    file.close()