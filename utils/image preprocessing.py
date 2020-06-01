# crop dogs images

import numpy as np # linear algebra
import xml.etree.ElementTree as ET # for parsing XML
import matplotlib.pyplot as plt # to show images
from PIL import Image # to read images
import os
import glob


root_images="D:\\AI\\GAN\\input\\all-dogs\\all-dogs\\"
root_annots="D:\\AI\\GAN\\input\\annotation\\annotation\\"

all_images=os.listdir("D:\\AI\\GAN\\input\\all-dogs\\all-dogs\\")
print(f"Total images : {len(all_images)}")

breeds = glob.glob('D:\\AI\\GAN\\input\\annotation\\annotation\\*')
print(breeds[:1])
#%%

annotation=[]
for b in breeds:
    annotation+=glob.glob(b)
print(f"Total annotation : {len(annotation)}")

breed_map={}
for annot in annotation:
    breed=annot.split("\\")[-1]
    index=breed.split("-")[0]
    breed_map.setdefault(index,breed)
    
print(f"Total Breeds : {len(breed_map)}")
print(breed)
print(index)
dict(list(breed_map.items())[0:2])
#%%
def bounding_box(all_images):
    bpath=root_annots+str(breed_map[all_images.split("_")[0]])+"/"+str(all_images.split(".")[0])
    tree = ET.parse(bpath)
    root = tree.getroot()
    objects = root.findall('object')
    for o in objects:
        bndbox = o.find('bndbox') # reading bound box
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        
    return (xmin,ymin,xmax,ymax)


#%%
import sys, gc

for k in range(7500,8000,50):
    for i,image in enumerate(all_images[k:k+50]):
        bbox=bounding_box(image)
        im=Image.open(os.path.join(root_images,image))
        im=im.crop(bbox)
        im=im.resize((64,64), Image.ANTIALIAS)
        plt.axis("off")
        plt.imshow(im)
        plt.savefig("D:\\AI\\GAN\\input\\sam\\resize{}".format(i+k), bbox_inches='tight')
    gc.disable()
    #gc.collect()
    del(im)