#!/bin/bash

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar  -files /home/rishixtreme/ds222/mapper_test.py,/home/rishixtreme/ds222/reducer_test.py -mapper /home/rishixtreme/ds222/mapper_test.py -reducer /home/rishixtreme/ds222/reducer_test.py -cacheFile /user/rishixtreme/out_conditional/part-00000#conditional -cacheFile /user/rishixtreme/out_prior2/part-00000#prior -input /user/ds222/assignment-1/DBPedia.verysmall/verysmall_test.txt -output /user/rishixtreme/out_posterior
