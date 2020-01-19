from pyspark import SparkContext, SparkConf
import collections as cs

conf = SparkConf().setMaster("local").setAppName("RatingsCounter")
sc = SparkContext.getOrCreate(conf=conf)

lines = sc.textFile("file:///Volumes/Data/Projects/Explore/03 Spark Explore/ml-100k/u.data")
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

sortedResults = cs.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print(str(key) + " " + str(value))

sc.stop()