import yaml

##if 0:
##    with open('measure_example.yaml') as file:
##        conf = yaml.safe_load(file)
##        print(conf)

file = open('JohnD.yaml')
dict_from_yaml = yaml.safe_load(file)
print(file)
print(dict_from_yaml)
