# Initiate PySpark on myMackbook air
cd documents
cd spark-3.4.1-bin-hadoop3
bin/pyspark

# Initiate Google CLI on myMacbook air
./google-cloud-sdk/bin/gcloud init
#  authenticate with login to google cloud account


# remove docker container and images
docker container rm -f $(docker container ls -aq)
docker image rm -f $(docker image ls -aq)
# or delete/purge using UI under setting -> debug
# validate 
docker images 
docker ps
docker ps -a


# 2052a we have procs running under java framework, or in R2CE we have SQL query/DB connection under R2CE framework using Falcon under the hood. 
# now, when we move to GCP, we plan to package and run. 
# but what if there is a better way of doing it on GCP, then we will be having another initiave to move to that approach. 
# at this point, it may feel like not possible, but look 3-4 years back R2CE was also a far fetch idea. 
# or look at Hadoop, Mapreduce, Spark and now Flink, the cool thing is to know whats next and be good in whats today. 

