from pyspark import SparkContext, SparkConf
import collections
import re

def normalizeWords(text):
    return re.compile(r'\W+', re.UNICODE).split(text.lower())

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf=conf)

lines = sc.textFile("file:///Volumes/Data/Projects/Explore/03 Spark Explore/book/Book.txt")
words = lines.flatMap(normalizeWords)
# wordCount = words.countByValue()
wordCount = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
wordCount2 = wordCount.map(lambda x: (x[1], x[0])).sortByKey()

for count, word in wordCount2.collect():
    print(str(word) + " -- " + str(count))
