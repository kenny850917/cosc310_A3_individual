<h1>Individual Assignment 3</h1>
<h2>extended from Group25 Assignment 2</h2>
<h1>Project name: AutoBot</h1>
<h2>Developer: Kenny Ho (25226151)</h2>


<h2>About the project</h2>
Our project is called Autobot and is essentially an AI that assists a user in picking a vehicle. This is done by asking the user a series of questions which helps Autobot predict what the user will prefer. Autobot is mainly for users who may have limited knowledge of what type of vehicle they are interested in.

<h2>Navagation for software</h2>
We organized all code in one class (VehicleList) for simplicity and ease of access. VehicleList initiates a database and adds all vehicles available. 
<h2>Code organization</h2>
In VehicleList.py the codes are organized into serveral parts sepearted by comments.
<ul>
<li>Database of cars</li>
<li>Text input for text matching check</li>
<li>FUnction for text finding </li>
<li>methods for compiling </li>
<li>Sentiment analysis function</li>
<li>Named Entity Recognition</li>
</ul>

<h2>Features</h2>
<ul>
 <li>Spelling Check</li>
 The spelling check function takes a input sentence, break down into segments of words and check for spelling errors. It will provide the user with suggestions and let them re-enter the sentence. 
 <i> example </i>
 Currently we support the following features: 
 -Fuel Efficiency 
 -Seating 
 -Price 
 -Type of vehicle
 -Brand
 fuuel
for fuuel did you mean fuel (spelling check here)
 
 <li>Synonyms</li>
 The algorithm takes a word and will provide similar synonyms based on the nltk packet imported from python library.
 The function also takes user input and talk conversation with synonyms.
  <i> example </i>
  w1 = wordnet.synset('car.n.01') # n here denotes the tag noun
w2 = wordnet.synset('train.n.01')
print(w1.wup_similarity(w2))( this is a testing line to compare the similarity of both words.) value closer to 1 is the better synonym.)
// output
{'automobile', 'motorcar', 'railway_car', 'auto', 'railroad_car', 'cable_car', 'gondola', 'railcar', 'elevator_car', 'car', 'machine'}
set()
0.6666666666666666 (the synonym check mentioned above)

<li>Sentiment analysis</li>
The system can detects words and phases from sentence and give it a float value from 1.0 to -1.0 which represent positive or negative sentiment. 
 <i> example </i>
 How is your day going?
Doing alright, went to down town with friend the other day to have icecream
[] (the process uses sentiment analysis + named entity recognition and then perform an output.)
 . 
I can tell you're having a good day, getting a new car would be nice <i>(this is the output)</i>

<li>Named Entity Recognition</li>
 After the implementation of named entity recognition, the program can read a paragraph or text, and recognize the following tags:
  <ol>
  <li>geo = Geographical Entity</li>
  <li>org = Organization</li>
  <li>per = Person</li>
  <li>gpe = Geopolitical Entity</li>
  <li>tim = Time indicator</li>
  <li>art = Artifact</li>
  <li>eve = Event</li>
  <li>nat = Natural Phenomenon</li> 
  </ol>
  <i> example </i>
  Hi, what is your name?:Kenny <i>(user input)</i>
[Tree('PERSON', [('Kenny', 'NNP')])] (print out to see clearfication)

  
</ul>


