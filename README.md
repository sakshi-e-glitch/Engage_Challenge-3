![alt text](https://github.com/sakshi-e-glitch/Engage_Challenge-3/blob/master/static/styles/assets/Green%20White%20Modern%20Go%20Green%20Instagram%20Post%20(2).png)
# Recommendation Engine by Sakshi Pandey

This project is an attempt to help farmers by recommending them a crop which is most suitable for their land. The suitability is decided on the basis of various factors such as pH level, Nitrogen, Potassium etc. The algorithm use is *KNN algorithm*, which is a sort of classifier algorithm used in Machine Learning. 

Reference: [Medium blog link](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761#:~:text=Summary,both%20classification%20and%20regression%20problems.)

Deployed Link: [Heroku](https://krishi-e.herokuapp.com/) (the deployed website has issue with the news section, I would recommend to clone the repo in order to have a better experience) 

**Motivation:** India is an agrarian country with around 48.9%* of its people depending directly or indirectly upon agriculture and still has very less farm productivity. A total of 5,650 farmers have committedsuicides during 2014, accounting for 4.3% of total suicides victims in the country. Hence, farm productivity needs to be increased so that farmers can get more pay from the same piece of land with less labour.
[Link to a news article](https://www.downtoearth.org.in/news/agriculture/every-day-28-people-dependent-on-farming-die-by-suicide-in-india-73194)

# Table of Contents
* [Features of the Application](#features-of-the-application)
* [Data Source](#data-source)
* [Install and run locally](#install-and-run-locally)
* [Demo](#demo)
* [KNN Algorithm](#knn-algorithm) 
* [Use of Agile Methodology](#use-of-agile-methodology)
* [Challenges faced](#challenges-faced)
* [Future Scope](#future-scope)
* [Support and Contact](#support-and-contact)

# Features of the Application
* Responsive and is compatible with devices having smaller screens.
* Recommendation on basis of various factors
* A guide for crops
* Agriculture based news

[(Back to top)](#table-of-contents)

# Install and run locally
To use this project, follow the steps below:

1. You should have python installed in you computer. 

2. Initialise git on your terminal.

```bash
git init
```
3. Clone this repository.

```bash
git clone https://github.com/sakshi-e-glitch/Krishi-e.git
``` 
4. Open the directory created via a code editor, it is recommended you use Visual Studio Code. Futher, open app.py .

5. Run the following command to install required packages

```bash
pip install -r requirements.txt
```
6. Once all the required packages are installed. Again run app.py. This time it will give you a link to run on local host. :)

# Data Source
[Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

[(Back to top)](#table-of-contents)

# Demo

![Image](https://github.com/sakshi-e-glitch/Krishi-e/blob/master/static/styles/assets/responsive.png)

[(Back to top)](#table-of-contents)

# KNN Algorithm
The KNN algorithm assumes that similar things exist in close proximity. In other words, similar things are near to each other.

1. Load the data
2. Initialize K to your chosen number of neighbors
3. For each example in the data:
    ⋅⋅*Calculate the distance between the query example and the current example from the data.
    ⋅⋅*Add the distance and the index of the example to an ordered collection

There are various ways of calculating distance, and one way might be preferable depending on the problem we are solving. However, the straight-line distance (also called the Euclidean distance) is a popular and familiar choice.

4. Sort the ordered collection of distances and indices from smallest to largest (in ascending order) by the distances
5. Pick the first K entries from the sorted collection

for my project, I've used k=1

[(Back to top)](#table-of-contents)

# Use of Agile Methodology
The Agile methodology is a way to manage a project by breaking it up into several phases. As this wasn't a team project, I could not assign different tasks to different people and form a sprint out of it. Therefore I divided myself into five different people - one who will research, one who will design, one who will develop the frontend, one who will develop the recommendation system and finally the one who will fix bugs. 

I used Trello as my primary application for designing the board for the development process of this project.
![trello ss](https://github.com/sakshi-e-glitch/Krishi-e/blob/master/trello.PNG)

[(Back to top)](#table-of-contents)

# Challenges Faced
"If you are not facing challenges while developing an application, you are not considering every possible case for a better experience of your users."

During the development process I faced the following challenges:
 1. Understanding new tech stacks as I had no prior knowledge other than basic HTML and CSS before. However, thanks to online communities, stackoverflow, my mentor and friends I was able to find resources which helped me in creating this web application.
 2. Preparing a feature list. In the beginning I wanted to build an app like no other and incorporate as many features as I could. But in the interest of time, I had to narrow down the features to the most basic functionalities. :(
 3. Time Management: During the 1st 3 weeks of program I had my end semester examinations (that too in offline mode after almost 2 years), hence I could not dedicate as much time as I should.

All these challenges were less of challenges and more of lessons, lessons to help me have an even better development process in the future and to not give up even till the end. 

[(Back to top)](#table-of-contents)

# Future Scope
The web application can be improved by adding the following features.

1. A chatbot which can entertain queries of farmers.
2. Multi-lingual options
3. Nearest soil testing lab location
4. User registration through Aadhar Number
5. A disease detection model for crops

[(Back to top)](#table-of-contents)

# Support and Contact 

Email To: sakshi.pandey1510@gmail.com

[(Back to top)](#table-of-contents)
