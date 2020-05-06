# Final Project

Kayla Bracall DAT 129 - Spring 2020

## Web Scraping 

This project aims to find which type of yarn is most expensive. This is done by scraping information from yarn.com. The types of yarn that were looked at were:

* alpaca
* bamboo
* cashmere
* cotton
* luxury
* polyester
* silk
* wool

My hypothesis is that cashmere would be the most expensive yarn material. After scraping the site and finding the average price of each type of material, this was found to be true. 

## Limitations

The first limitation that I encountered was determining the average cost of yarn by length. Yarn is often sold in different measurements, with hank, ball, skein all being common. There is no standard length for each of these units. As such, I wanted to find the average price per yard, but was unable to scrape yards from the webpage. If I were to expand this project, I would look further into scraping this information. 

The second limitation was that a lot of yarn is a blend of different materials. This is broken down by percentage on the site. An expansion of this project would also include taking these percentages into account. 

The final limitation of this project was modularity. The finished code has a separate block for scraping each type of yarn. However, I wanted to write a function that could take user input and scrape based on that input. The issue that I ran into was prompting the user to enter all yarn types so that they could all be stored in the yarn dictionary. I experimented with this concept in the file titled 'alt_final_project.py.'  This file breaks the code down into more modularized functions that can be used for more general webscraping. 

## Findings
As expected, the most expensive yarn on average is yarn that is cashmere or contains cashmere. 