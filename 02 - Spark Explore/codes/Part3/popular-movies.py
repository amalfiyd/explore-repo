from pyspark import SparkContext, SparkConf

def loadMovieNames():
    movieDict = {}
    with open("/Volumes/Data/Projects/Explore/03 Spark Explore/ml-100k/u.item", 'r', encoding="iso-8859-1") as f:
        for line in f:
            fields = line.split("|")
            movieDict[int(fields[0])] = fields[1]

    return movieDict

def parseContent(line):
    temp = line.split("\t")
    custID = int(temp[0])
    movieID = int(temp[1])
    ratingVal = int(temp[2])
    timestamp = temp[3]

    return (custID, movieID, ratingVal, timestamp)

conf = SparkConf().setMaster("local").setAppName("popular-movies")
sc = SparkContext(conf=conf)

movieDict = sc.broadcast(loadMovieNames())

lines = sc.textFile("file:///Volumes/Data/Projects/Explore/03 Spark Explore/ml-100k/u.data")
rddVals = lines.map(parseContent)
popularMovieRdd = rddVals.map(lambda x: (x[1], 1))
movieCounts = popularMovieRdd.reduceByKey(lambda x, y: x + y)

movieCountsSorted = movieCounts.map(lambda x: (x[1], movieDict.value[x[0]])).sortByKey()

for countVal, movieID in movieCountsSorted.collect():
    print(str(movieID) + ": " + str(countVal))
