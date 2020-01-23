import glob 

jpgs = glob.glob('*jpg')
npys = glob.glob('*npy')

npys = set([npy.split('_')[0] for npy in npys])
jpgs = set([jpg.split('_')[0] for jpg in jpgs])

for jpg in jpgs:
    assert jpg in npys
