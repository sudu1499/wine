import os

dir=[
    os.path.join('data','raw'),
    os.path.join('data','processed'),
    'notebooks',
    'svaed_models',
    'src'
]
files=[
    'dvc.ymal',
    'param.yaml',
    '.gitignore',
    os.path.join('src','__init__.py')
]

for dir_ in dir:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass

for file_ in files:
    with open(file_,'w') as f:
        pass
    