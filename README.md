# Airbnb Host Dashboard Project Summary

*By: Belle Peng    | 2018-09-17*

**Motivation**

Travelling and experiencing the local lifestyle through staying at locals' homes is a passion of mine, so naturally I want to work on a project related to this. Many Airbnb hosts identified three primary concerns:

1. Hosts are not sure how their guests feel, especially if they have many guests often or have many properties
2. Hosts are not sure if there are recurring themes in the reviews, or where to focus their improvement efforts on
3. Hosts sometimes are not getting enough booking

The goal of this project is to build an **Airbnb** **Host Dashboard** that serves as a self-diagnostics tools for the hosts to tackle these concerns. 



**Data**

This project is prototyped using San Francisco data, which can be easily extended to other cities in the future. I downloaded csv files from [InsideAirbnb](<http://insideairbnb.com/get-the-data.html>) for San Francisco as of August 2018, which contains 6633 listings and 278884 reviews.  The data behind the Inside Airbnb site is sourced from publicly available information from the Airbnb site. The data I used can be found in this github repo under *“data”*.



**Tools** **&** **Algorithms**

The code for this project is done in python, using machine learning techniques including Linear Modeling, Natural Language Processing, and Data visualization. Packages include but not limited to NLTK, Textblob and Scikit-Learn. The Dashboard is built in Tableau. For complete code, please see *“notebooks”* directory.



**Results**

The final **Airbnb Host Dashboard** can be found in the *“results”* directory as a “[Host Dashboard.twb](https://github.com/bellepeng/Project_AirBNB/blob/master/results/Host%20Dashboard.twb)” along with a deck to explain the project in a more visually fun way “[AirBNB Host Dashboard Presentation.pptx](https://github.com/bellepeng/Project_AirBNB/blob/master/results/AirBNB%20Host%20Dashboard%20Presentation.pptx)”. The dashboard contains these sections:

- A 2-sentences review summary of the most recent 20 reviews for each listing, so that a host can gauge the guests’ main reviews without having to read all of the reviews 
- A top 3 topic to tell the hosts what their guests are talking about 
- A sentiment analyzer over time to help the host monitor trends, which can be used in conjunction with the review scores bar chart (scores are provided by Airbnb) to identify trouble areas
- A market rate comparison to help the host understand if they are significantly below or above comparable homes, which may be the cause for not getting enough bookings

 

**Future**

I plan to expand this project in the future with the following components / ideas:

- Incorporate clustering algorithms to improve the pricing model
- Incorporate image recognition to identify areas of improvements for the host
- Build a recommendation engine for the guests to recommend properties for the city they are looking at but have not yet booked, or for another similar city. For example, for the bi-coastal working people recommend Airbnb in NYC for those that also book in SF.