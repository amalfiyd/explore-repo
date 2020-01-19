from pyspark.sql import Row
from pyspark.sql import SparkSession
import collections

spark = SparkSession.builder.appName("sparksql01").getOrCreate()

def mapper(line):
    temp = line.split(",")
    return Row(ID=int(temp[0]), name=temp[1], age=int(temp[2]), numFriends=int(temp[3]))

lines = spark.sparkContext.textFile("file:///Volumes/Data/Projects/Explore/03 Spark Explore/fake-friends/fakefriends.csv")
rdd = lines.map(mapper)

schema = spark.createDataFrame(rdd).cache()
schema.createOrReplaceTempView("people")

teenagers = spark.sql("select * from people where age >= 13 and age <= 19")
teenagers.show()