import os
import sys


dir_full_path=sys.argv[1]
path= os.path.dirname(dir_full_path)
dir_list=os.listdir(path)
for i in range(len(dir_list)):
    source_path= os.path.join(path+"/"+dir_list[i]+"/")
    image_path = os.path.join(path +"/cnt/"+dir_list[i]+"/")
    if not os.path.isdir(image_path):
        os.makedirs(image_path)
    file_list= os.listdir(source_path)
    for j in range(len(file_list)) :
        base_name= os.path.splitext(os.path.basename(file_list[j]))[0]
        outputfilename= os.path.join(image_path,base_name)
        os.system('flawfinder --dataonly --quiet '+ source_path + file_list[j] +" >>" + outputfilename+".txt")
        os.system('grep -c "78" '+ outputfilename+ ".txt >>"+ outputfilename)
        os.system('grep -c "120" '+ outputfilename+".txt >>"+ outputfilename)
        os.system('grep -c "126" '+ outputfilename+".txt >>"+ outputfilename)
        os.system('grep -c "134" '+ outputfilename+".txt >>"+ outputfilename)
        os.system('grep -c "190" '+ outputfilename+".txt >>"+ outputfilename)
        os.system('grep -c "327" '+ outputfilename+".txt >>"+ outputfilename)
        os.system('grep -c "377" '+ outputfilename+".txt >>"+ outputfilename)
        os.system('grep -c "676" '+ outputfilename+".txt >>"+ outputfilename)
        os.system('grep -c "785" '+ outputfilename+".txt >>"+ outputfilename)
        print(outputfilename + " created")
