## The task is to "mine" data from a datasource on real immigration DATA and to start processing it


* The purpose of the task is to get the list of the top 10 countries where immigrants went to during the period of 2001-2010. We will use [this source](../data/real/imigr._scop_tara_2001-2010.xlsx), please take a look at it. After getting the list - we will save the results inside "data/real/top_10_2001_2010.csv"

* please do all the work inside [this python file](../tests/panda.basics.real.data.2001_2010.top10.py) it has already the libraries imported. So just continue step by step following the steps presented bellow. In order for this to run you should RUN python at the level of the folder which contains the tasks/ and data/!

1. Loading the data from the source excel file:
    ```python
    filename = f"{os.getcwd()}/data/real/imigr._scop_tara_2001-2010.xlsx"
    df = pd.read_excel(filename, index_col=0)
    print(df)

    ```  
    * you should see a reduced table printed on the screen.
    * NOTE the ```os.getcwd()``` which helps us find the data in the right path. 
2. Lets check the data type we are getting:    
    ```python
    print( type(df) )
    ```  
    * you should see ```<class 'pandas.core.frame.DataFrame'>``` which means that you get an object of type "DataFrame" and you can use all of it's options / methods
   
3. Let's pick up only the needed data (the country names with the data for 2001 - 20010), first take a look into the excel file, you will see that the TOTAL column is each 4th column starting with the 0th, till the 40th, so:    
    ```python
    useful_data = df.iloc[5:146, list(range(0, 40 , 4))]
    print( useful_data )
    print( useful_data.columns )
    print( type( useful_data ) )
    ```  
    * NOTICE how we use a list generated from a range() function so we can write less! 
    * you will notice again that we get the same - unnamed columns - which is not so great for presenting data or for filtering data
5. Let's rename the columns. Now - renaming the columns manually will also take a lot of time if we write it like so
    ```python
    useful_data = useful_data.rename(columns={ 'Unnamed: 1': '2001', 'Unnamed: 5': '2002', ... })
    print( useful_data )
    ``` 
    * SO IT IS REQUIRED OF YOU THAT YOU DEFINE A FUNCTION **generateColumnNames()** which will return a dictionary containing the structure 
      ```{ 'Unnamed: 1': '2001', 'Unnamed: 5': '2002', ... }``` up till 2010. The function should use a **for** loop which ads keys and values to the dictionary using maybe a **range()** too

      when you are done with this function we should be able to call the code above like so:
      ```python
      useful_data = useful_data.rename(columns=generateColumnNames())
      print( useful_data )
      ``` 
6. Let's sort the values in an descending ( by default is ascending ) order - so we get the top immigrants destinations. 
   to sort multicolumn values, it's enough to put the list of the columns names which we want to be sorted by, the dataframe will do it's best to
   sort by all the values
   ```python
   useful_data = useful_data.replace('-',0).sort_values( ['2001','2002',...], ascending = False )
   print( useful_data )
   ```  
   again, this will take a lot of code to write it manually 
   * SO IT IS REQUIRED OF YOU THAT YOU DEFINE A FUNCTION **generateColumnLabels()** witch will return a **list** with the labels from '2001' to '2010', use a similar algorithm that you used in the function above!

   so we could after call the sort like this:
   ```python
   useful_data = useful_data.replace('-',0).sort_values( generateColumnLabels(), ascending = False )
   print( useful_data )
   ```   

7. Picking the top 10, as required, easy - just using .head()
   ```python
   useful_data = useful_data.head(10)
   print( useful_data )
   ```  
   
8. Save the data to a csv file   
   ```python
   filename = f"{os.getcwd()}/data/real/top_10_2001_2010.csv"
   useful_data.to_csv(filename)
   ```   
 
---

BONUS!!! - does something change if you apply the sort like so: 
```python
useful_data = useful_data.replace('-',0).sort_values( ['2010','2009','2008',...,'2001'], ascending = False )
```
if YES - what changes ?
