#!/bin/bash

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar  -files /home/rishixtreme/ds222/mapper.py,/home/rishixtreme/ds222/reducer.py -mapper /home/rishixtreme/ds222/mapper.py -reducer /home/rishixtreme/ds222/reducer.py -input /user/ds222/assignment-1/DBPedia.verysmall/verysmall_train.txt -output /user/rishixtreme/out1

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar  -files /home/rishixtreme/ds222/mapper2.py,/home/rishixtreme/ds222/reducer2.py -mapper /home/rishixtreme/ds222/mapper2.py -reducer /home/rishixtreme/ds222/reducer2.py -input /user/rishixtreme/out1/part-00000 -output /user/rishixtreme/out2

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar  -files /home/rishixtreme/ds222/mapper_prior.py,/home/rishixtreme/ds222/reducer_prior.py -mapper /home/rishixtreme/ds222/mapper_prior.py -reducer /home/rishixtreme/ds222/reducer_prior.py -input /user/ds222/assignment-1/DBPedia.verysmall/verysmall_train.txt -output /user/rishixtreme/out_prior

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar  -files /home/rishixtreme/ds222/mapper_prior2.py,/home/rishixtreme/ds222/reducer_prior2.py -mapper /home/rishixtreme/ds222/mapper_prior2.py -reducer /home/rishixtreme/ds222/reducer_prior2.py -input /user/rishixtreme/out_prior/part-00000 -input /user/rishixtreme/out_prior -output /user/rishixtreme/out_prior2

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar  -files /home/rishixtreme/ds222/mapper_conditional.py,/home/rishixtreme/ds222/reducer_conditional.py -mapper /home/rishixtreme/ds222/mapper_conditional.py -reducer /home/rishixtreme/ds222/reducer_conditional.py -input /user/rishixtreme/out1/part-00000 -input /user/rishixtreme/out2/part-00000 -output /user/rishixtreme/out_conditional
