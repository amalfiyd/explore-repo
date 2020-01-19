from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("assignment1")
sc = SparkContext(conf=conf)

def parseInput(line):
    temp = line.split(",")
    custID = int(temp[0])
    itemID = int(temp[1])
    value = float(temp[2])
    return (custID, itemID, value)

lines = sc.textFile("file:///Volumes/Data/Projects/Explore/03 Spark Explore/customer-orders/customer-orders.csv")
rddVal = lines.map(parseInput)
custVal = rddVal.map(lambda x: (x[0], x[2]))
totalValByCust = custVal.reduceByKey(lambda x, y: x + y)
totalValByCustSorted = totalValByCust.map(lambda x: (x[1], x[0])).sortByKey()

for totalVal, custID in totalValByCustSorted.collect():
    print(str(custID) + ": " + str(totalVal))