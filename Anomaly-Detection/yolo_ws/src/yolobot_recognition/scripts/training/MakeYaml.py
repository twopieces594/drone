import yaml

data = { 'train' : '/home/samuel/Downloads/Worker_Data/train/images/',
         'val' : '/home/samuel/Downloads/Worker_Data/valid/images/',
         'test' : '/home/samuel/Downloads/Worker_Data/test/images',
         'names' : ['Helmet', 'Person', 'Vest'],
         'nc' : 3 }

with open('/home/samuel/Downloads/Worker_Data/Worker_Data.yaml', 'w') as f:
  yaml.dump(data, f)