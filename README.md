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
</ul>

<h2>Features</h2>
<ul>
<li>Sentiment analysis</li>
The system can detects words and phases from sentence and give it a float value from 1.0 to -1.0 which represent positive or negative sentiment. 
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
</ul>


