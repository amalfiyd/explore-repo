from pyspark import SparkContext, SparkConf
import collections as cs

conf = SparkConf().setMaster("local").setAppName("Test Explore")
sc = SparkContext.getOrCreate(conf=conf)

def thefunction(z):
    return z * z

lines = sc.textFile("file:///Volumes/Data/Projects/Explore/03 Spark Explore/ml-100k/u.user")
ratings = lines.map(lambda x: (x.split("|")[3], int(x.split("|")[1])))

# rdd.map(thefunction).saveAsTextFile("tests")