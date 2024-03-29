# topic generator - Python version
# Budi Rahardjo (@rahard) 2021

# configuration
topicfile = "topics.txt"

# read topicfile and count the number of topics
# somebody said, do not slurp, but do it this way
with open(topicfile, 'r+') as f:
    count = 1 
    topic=''
    topics=[]
    for line in f:
        if (line == "--\n"):
            #print(topic)
            #print('{:>6} {}'.format(count, topic))
            topics.append(topic)
            topic=''
            count += 1
        else:
            if (topic != ''):
                # append to previous line with a space
                topic = topic + ' ' + line[:-1]
            else:
                topic = topic + line[:-1] 

# summary
#print("There are", len(topics), "topics")
#print(topics)

def gen_topic():
   import random
   n = random.randint(0,len(topics)-1)
   return(str(n) + ' ' +  topics[n])

#print(gen_topic())

from flask import Flask
app = Flask(__name__)

@app.route("/")
def utama():
    t = gen_topic()
    return t
