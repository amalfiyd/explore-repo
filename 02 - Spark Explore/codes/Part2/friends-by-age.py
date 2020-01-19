from pyspark import SparkContext, SparkConf
import collections as cs

def parseLines(line):
    _fields = line.split(',')
    id = _fields[0]
    name = _fields[1]
    age = int(_fields[2])
    fcount = int(_fields[3])
    return (age, fcount)

conf = SparkConf().setMaster('local').setAppName('fake_friends')
sc = SparkContext(conf=conf)

lines = sc.textFile("file:///Volumes/Data/Projects/Explore/03 Spark Explore/fake-friends/fakefriends.csv")
data = lines.map(parseLines)

data2 = data.mapValues(lambda x: (x,1))
sumall = data2.reduceByKey(lambda x,y : (x[0]+y[0], x[1]+y[1]))
averagebyage = sumall.mapValues(lambda x : x[0] / x[1])

for result in averagebyage.collect():
    print(result)
