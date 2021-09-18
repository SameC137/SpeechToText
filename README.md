# African language Speech Recognition - Speech-to-Text

<p>The World Food Program wants to deploy an intelligent form that collects nutritional information of food bought and sold at markets in two different countries in Africa - Ethiopia and Kenya. The design of this intelligent form requires selected people to install an app on their mobile phone, and whenever they buy food, they use their voice to activate the app to register the list of items they just bought in their own language. The intelligent systems in the app are expected to live to transcribe the speech-to-text and organize the information in an easy-to-process way in a database. </p>

## Folder/File structure for branch 

<ul>
    <li>artifacts-contains artifacts such meta files and other artifacts generated through the project</li>
    <li>notebook-contains notebooks for describing the functionality of the the classes to achieve the meta generation and the preprocessing</li>
    <li>scripts-contains scripts for Meta generation, preprocessing and feature extraction</li>
    <li>data.dvc- DVC File for versioning of the data</li>
    <li>requirements.txt- dependencies for code inside this branch</li>
    </ul>

## Data
<ul>
<li>Dataset for Swahili-  https://github.com/getalp/ALFFA_PUBLIC</li></ul>
<br/>

## Data Features
    Input features (X): audio clips of spoken words
    Target labels (y):  text transcript of what was spoken

## Models Used

### Simple RNN
<img src="https://drive.google.com/uc?export=view&id=1eh4Zc880mTXH8cBkEUlUD1HMmsta0kvf"/>

<br/>
<br/>

### Bidirectional RNN
<img src="https://drive.google.com/uc?export=view&id=12KrQ1xzc9ZMcuPg8RezGdUUeyDy6UJKA"/>

<br/>
<br/>

### CNN RNN model
<img src="https://drive.google.com/uc?export=view&id=1unFPcuZBrBW-hiN4cVoqxk--YCEJjbrq"/>
<br/>
<br/>


### Deep speech 2 layers
<img src="https://drive.google.com/uc?export=view&id=1CJEfUxiGkvwpTd98XcSW1rGQ6i8zJg5k"/>
<br/>
<br/>


### Deep Speech with RNN layer Bidirectional
<img src="https://drive.google.com/uc?export=view&id=1Aqk8G5gy3CB3666aROOjcoVZuCWt9lng"/>
<br>
<br>


### Deep Speech 3 Layers
<img src="https://drive.google.com/uc?export=view&id=1-axvDegKnccZTycGoOIDMLvUrmyteZZI"/>