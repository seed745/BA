#edit a gdml to add the auxtype lines so that it becomes sim ready
from lxml import etree
import numpy as np

tree = etree.parse("/home/jasper/ba/gdml/simple_grid/test_simple_grid.gdml")
root = tree.getroot()

#translation of the indexes from the MRADSIM to detector indexes
det_index = [19,20]
for i in range(1,19):
    det_index.append(i)
det_index += [39,40]
for i in range(21,39):
    det_index.append(i)
print(det_index)

counter = 0
for volume in root.findall(".//volume"):
    name = volume.get("name")
    if "active" in name:   
            new_aux = etree.SubElement(volume, "auxiliary", auxtype ="sensi", auxvalue=f"{det_index[counter]}", auxunit="id")
            counter += 1
    elif "BGO" in name and not "MIR" in name:
            new_aux = etree.SubElement(volume, "auxiliary", auxtype ="sensi", auxvalue=f"41", auxunit="id")
    
    elif "BGO" in name and "MIR" in name:
            new_aux = etree.SubElement(volume, "auxiliary", auxtype ="sensi", auxvalue=f"42", auxunit="id")

tree.write("/home/jasper/ba/gdml/simple_grid/test.gdml",pretty_print=True,xml_declaration = True, encoding = "utf-8")
print("Done!")    
        

        

