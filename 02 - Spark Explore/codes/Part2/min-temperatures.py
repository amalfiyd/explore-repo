from pyspark import SparkContext, SparkConf
import collections

conf = SparkConf().setMaster("local").setAppName("min-temperature")
sc = SparkContext(conf=conf)

def parseLine(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32
    return (stationID, entryType, temperature)


lines = sc.textFile("file:///Volumes/Data/Projects/Explore/03 Spark Explore/weather1800/1800.csv")
parsedLines = lines.map(parseLine)
dataTMIN = parsedLines.filter(lambda x: 'TMIN' in x[1])
dataTMIN2 = dataTMIN.map(lambda x : (x[0],x[2]))
result = dataTMIN2.reduceByKey(lambda x,y : min(x,y))

resultf = result.collect()

for item in resultf:
    print(item)

