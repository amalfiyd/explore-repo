from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("popular-superhero")
sc = SparkContext(conf=conf)

def namesDict(line):
    temp = line.split('"')
    shID = int(temp[0].strip())
    shName = temp[1].strip().replace('"', '').encode('utf-8')

    return (shID, shName)

def coOccurences(line):
    temp = line.split()
    return (int(temp[0]), len(temp) - 1)

namesRdd = sc.textFile("file:///Volumes/Data/Projects/Explore/03 Spark Explore/marvel/Marvel-Names.txt")
namesRdd = namesRdd.map(namesDict)

graphRdd = sc.textFile("file:///Volumes/Data/Projects/Explore/03 Spark Explore/marvel/Marvel-Graph.txt")
coOccurencesRdd = graphRdd.map(coOccurences)
totalFriendsByChar = coOccurencesRdd.reduceByKey(lambda x, y: x + y)

mostPopular = totalFriendsByChar.map(lambda x: (x[1], x[0])).max()
mostPopularName = namesRdd.lookup(mostPopular[1])

