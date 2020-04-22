import sys
import pandas
from DTL import Node
from ID3 import ID3
from C45 import C45 
from sklearn import preprocessing
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#recursion depth
#sys.setrecursionlimit(1500)

# Load Datasets
iris_datasets = load_iris()
tennis_datasets = pandas.read_csv("play_tennis.csv")

#pre-process tennis_datasets
label_encoder = preprocessing.LabelEncoder()
tennis_datasets = tennis_datasets[['outlook', 'temp', 'humidity', 'wind', 'play']]
for attribute in tennis_datasets:
    tennis_datasets[attribute] = label_encoder.fit_transform(tennis_datasets[attribute])

tennis_outlook = tennis_datasets['outlook'].values
tennis_temp = tennis_datasets['temp'].values
tennis_humidity = tennis_datasets['humidity'].values
tennis_wind = tennis_datasets['wind'].values

tennis_targets = tennis_datasets['play'].values
tennis_instances = []

for i in range(len(tennis_datasets)):
    tennis_instances.append([tennis_outlook[i],
                            tennis_temp[i],
                            tennis_humidity[i],
                            tennis_wind[i]])

#splitting tennis_datasets
tennis_train_instances, tennis_test_instances, tennis_train_targets, tennis_test_targets = train_test_split(tennis_instances, tennis_targets, test_size=0.2, random_state=42)

#pre-process iris datasets
iris_instances = iris_datasets.data
iris_targets = iris_datasets.target

iris_train_instances, iris_test_instances, iris_train_targets, iris_test_targets = train_test_split(iris_instances, iris_targets, test_size=0.9, random_state=42)

#testing kode
test_instances = [[1, 1], [0, 0]]
test_targets = []

id = ID3(tennis_train_instances,tennis_train_targets)
id.fit(id.instances,id.targets)
print("Predicted : ", id.predict(tennis_train_instances))
print("Actual : ", tennis_train_targets)

# Node testing
""" instances = [[0, 1, 2], [2, 1, 0]]
targets = [1, 0]
rules = ["== 0"] 
root = Node(0, instances, targets)

nodes = [Node(1, [instances[0]], [targets[0]])]
root.set_rule_children(rules, nodes)
child = root.next_node(instances[0])
child.set_rule_children(["== 1"], [Node([instances[1]], [targets[1]])])

some_child = root.next_node(instances[0])
# print(some_child.rule_children)

tennisAttr = []
tennisTarget = tennisData['play'].values

tennisOutlook = tennisData['outlook'].values
tennisTemp = tennisData['temp'].values
tennisHumidity = tennisData['humidity'].values 
tennisWind = tennisData['wind'].values

for i in range(len(tennisData)):
    tennisAttr.append([tennisOutlook[i], tennisTemp[i], tennisHumidity[i], tennisWind[i]])
    
tennisTrain, tennisTest, targetTrain, targetTest = train_test_split(tennisAttr, tennisTarget, test_size=0.1, random_state=42)


id = id3(instances,targets)
# id.fit(id.instances,id.targets)
id.fit(tennisTrain,targetTrain)

# makan[0] = node1
# makan[1] = node2
# makan[3] = node3
print(some_child.rule_children) """
