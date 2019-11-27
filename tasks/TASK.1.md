## The task is to "mine" data from a datasource on immigration

* Usualy a data source offers information following a "template". This template is not always suited for the reasearch you are about to do. 
That's why, sometimes analysts have to "transform" or "adapt" the source's data to a "closer" format, hence, creating an "abstraction layer" 
which will decouple the source "presentation logic" from the "analytics logic" of your project. Such an aproach will increase the menageability and
flexibility of your project. Keep in mind that most of the times it's enough to adapt a single "data branch" from a data source in order to 
be able to use all the data from that source (cause they follow the same template).

THE GOALS ARE:

1. TO write a Python adapter function which can mine data from https://statistica.gov.md/ and return structured data in form of dictionaries and lists
2. TO write a Python transformer function which "puts" this data into a numpy array and the into a pandas panel
3. TO write a visualisation of data function using a matplotlib or other python specific visualisation libraries
4. TO test data mining on multiple data sets from the selected source (in order to validate the written logic)
5. To group all this logic into a module named "statistica_gov_md_miner" (so the code sticks together an so it can be reused by others)


---
prerequisites:
1. familiarize yourself with Python's numpy, pandas
2. familiarize yourself with the concept of Python module

---
Project folder structure

create a local version of this project on your local machine
- create the parent folder: **Immigration_post_1991_latest/**
- create the child folder **data/** 
- download a csv with any desired data from the indicated source and place it in the data folder
- create the child folder **tests/**
- create the child folder **src/**
- create the child folder **modules/**


V's questions regarding data dowload in csv format. 
1. Data from date.gov.md is provided in xls formt. Some excel sheet have up to 12 tabs( data for each month). Do we save each tab individually in csv format or ther is a way to do it all at ones. 
https://date.gov.md/ckan/ro/dataset/4733-imigranti-sositi-in-republica-moldova/resource/e8450ded-47e3-438d-bc85-2e3be96ba141


