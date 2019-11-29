## The task is to "mine" data from a datasource on real immigration DATA

> May libraries dedicated to "structured" or "complex data" are designed in a way that simplifies the usage of the library. 
> 
> For example "pandas" is designed for "chaining". What does this mean? - Well we can apply consecutive methods (functions) as long as we know which data type we've got in return from the previous method. For example ```data.first().second().third().....``` - this is called **chaining**. At each step - we obtain a new copy of the modified data structure.


* The purpose of the task is to get the list of the top 10 countries where immigrants went to during the year 2001. We will use [this source](../data/real/imigr._scop_tara_2001-2010.xlsx), please take a look at it. After getting the list - we will save the results inside "data/real/top_10_2001.csv"

* please do all the work inside [this python file](../tests/panda.basics.real.data.2001.top10.py) it has already the libraries imported. So just continue step by step following the steps presented bellow. In order for this to run you should RUN python at the level of the folder which contains the tasks/ and data/!

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
   
3. Let's take a look at the columns:    
    ```python
    print( df.columns )
    ```  
    * you should see
      ```
        Index(['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5',
        'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10',
        'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14',
        'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18',
        'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22',
        'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26',
        'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30',
        'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33', 'Unnamed: 34',
        'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37', 'Unnamed: 38',
        'Unnamed: 39', 'Unnamed: 40'],
        dtype='object')
      ```
      which means that the columns do not have any names associated with them, which means that it will be harder to determine WHERE exactly we are located in the source file when doing search, filtering, etc. BUT!! we could use indexes. For example the first column - with the country names is the 0th and the second (1st index) is the column with the data for the year 2001, unfortunatelly both of this columns are not using the ENTIRE VERTICAL SPACE of the document (there is other data before the 7th row and below the 147th)  which doesnt really fit into the idea of these two columns.
4. Let's pick up only the needed data (the country names with the data for 2001):    
    ```python
    useful_data = df.iloc[5:146, [0]]
    print( useful_data )
    print( useful_data.columns )
    print( type( useful_data ) )
    ```  
    * as you can see we used the ".iloc" method / option which is present in the DataFrame, and it searched and selected data based on the INDEX of the rows and columns. You should read the parameters of this method like so (for this case) - take the data from the 6 trhough the 147 - row intersecting with the first column, the country names are the "indexes" in this case
    * another interesting thing is that we get the same "DataFrame" type for the result, so we could chain / apply anothe method that suits this data type
    * you will notice again that we get the same - unnamed columns - which is not so great for presenting data or for filtering data
5. Let's rename the columns
    ```python
    useful_data = useful_data.rename(columns={ 'Unnamed: 1': '2001'})
    print( useful_data )
    ``` 
    * notice the name "2001" - this is much easier to undestand when using the data from this subset
6. Let's sort the values in an descnding ( by default is ascending ) order - so we get the top immigrants destinations. 
   if you will try this
   ```python
   useful_data = useful_data.sort_values( '2001', ascending = False )
   print( useful_data )
   ```  
   you will most likely get an error, because - in the attempt of the df to sort it's column as numeric - it will encounter cells with the value of ```"-"``` as string. Many data sources uses "theyre standards" of annotating "empty" or "zero" values. This will create a problem for our numeric calculations, so we must adjust the data before sorting it numerically. Add the .replace() method like this:
    ```python
   useful_data =useful_data.replace('-',0).sort_values( '2001', ascending = False )
   print( useful_data )
   ``` 
   * notice the fact that we "cained" two methods in order to get the desired result (it's like saying.. hey- do this, then that, then...)
7. Picking the top 10, as required, easy - just using .head()
   ```python
   useful_data = useful_data.head(10)
   print( useful_data )
   ```  
   * notice how after each step we "remember" the result of the operation into the same variable, overriding the last result?
8. Save the data to a csv file   
   ```python
   filename = f"{os.getcwd()}/data/real/top_10_2001.csv"
   useful_data.to_csv(filename)
   ```   
   * in order for the OS path to work, don't forget to use the same folder/file structure as in the repository and always run python from the main folder!

--- 
* Try to pick up the years 2002,2003 and do the same operations as in this example
* To check you understanding try to write a code that will do all of this in a single like meaning:
  ```python
  df.iloc[5:146, [0]].rename(columns = { ... }).replace()......   .to_csv(...)
  ``` 