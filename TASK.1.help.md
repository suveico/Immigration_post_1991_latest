## Import and visualize simple data with pandas / numpy and matplotlib

* modules to use:
 - pandas
 - matplotlib
 - xlrd
 
* !!! Attention pandas sometimes uses external libraries in order to "read" / "write" from or to some data formats (e.g. to work with excel files 
  you need to install xlrd) 
 
* in order to read data from xls or csv we just use one of the next two options
```python
import pandas as pd

data = pd.read_csv('path/to/file.csv')
data = pd.read_excel('path/to/file.csv')
```

* after that, the logic begomes less different

* please create a python file called "excel_sample_reader.py" in the "test/" folder
* download [this sample data](./data/sample_1.xls) to your "data/" folder
* and using the sample above, load the excel file into the "data variable"
* if no errors till now continue
---
* for example in order to see the first / last few lines from a large set of data we can use
 ```python
 print( data.head(5) )
 print( data.tail(5) )
 ```
* for example in order to see the dimensions of the array you are working with
 ```python
 print( data.shape )
 ``` 
* for example in order to select a column and print me max/min values from it
 ```python
 print( data['people'].max() )
 print( data['people'].min() )
 ```  
* for example in order to plot the data set
 ```python
 data.plot()
 plt.show()
 ```  
* please check the mentioned options on the sample data set 
---
* THE TASK:
1. using the sample data provided, plot the last 3 years values using "bars"
2. using the 'people' column, plot the "change in percentage" for all the years
3. using the 'people' column, find and print the maximum value and the minimum of the 'people' count 
4. print the maximum value of the first 5 years from the data
5. print the maximum "change rate" and the YEAR it took place

 
 ## Valentina's Comments on the tasks. 11/25
 
 The first 2 tasks don't make much sense to me. 
 In task 1 we created a bar chart that is difficult to read. It doesn't make sense plotting people and yers using "bars" format. I think more apropriate would've been to create a bar that would represent just "peopele" category overy the 3 years and not years and people. 
 Please see the example in viber (I was not able to upload it in this workspace). 
 
Next:

In task 2 we have to change the "non-sense" graph into percentage. It drove me crazy because I don't see the logit and terefore I can't find the right solution on the web. Please provide som urls or tutoring that I can follow along. 
 
Questions:
Are these 5 tasks that you've assigned are the foundation of more complex code that we will use in our final data set? If so, I believe it would make more sense to work with the simplified version of the actual data. 
I propose to work with the actual data set. This way I will star wrapping my mind arround the actual numbers and start seing the story and the paterns. 
https://statbank.statistica.md/pxweb/pxweb/ro/20%20Populatia%20si%20procesele%20demografice/20%20Populatia%20si%20procesele%20demografice__POP__POP070/POP070300.px/?rxid=b2ff27d7-0b96-43c9-934b-42e1a2a9a774

We can start with two first two colums, countries and 1993. 

