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
* download [this sample data]() to your "data/" folder
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

 
