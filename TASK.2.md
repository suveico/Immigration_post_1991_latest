# Putting the logic inside functions

* The goal of this exercise is to separate the LOADING and the PRESENTATION logic in two functions

1. Create a function named **loadDataSource( file_name )** which will:
  1. load the data from an specified excel file
  2. raise an exception if the file doesnt end with ".xls" or ".xlsx"
  3. return the loaded data (this should be a panda DataPanel if you check the return type)
  
2. Create a function named **plotData( data )** which will:
  1. take the data and plot it using matplotlib


* the final code that should run smoothly after defining this two functions should look like this
  ```python
  data = loadDataSource( "path/to/excel.file" )
  plotData( data )
  ```
