# Check your understanding of the "panda" toolkit 

1. What is the main difference between **panda** and **numpy** ?
2. What is the difference between **DataFrame** and **Series** in **panda** ?
3. Can we hardcode data into a panda data structure, what type of data can we put inside ? 
4. Which methods (functions) does panda use to read from: text file, csv file, excel files, pdf files ?
5. Does panda use "external" libraries in order to load (parse) a formatted file ?
6. Can panda save data in csv or excel format ?


V's answers
 
1. Difference between pandas and numpy 
NumPy - used for fast mathematical computation for Arrays and Matrice
Pandas - provides DataFrames similar to tables (rows and columns)

2. Series Objects vs DataFrame Object
Series - one dimensional labeled (called index) array capable of holding any data type
DataFrames  - two dimensional labeled with columns of POTENTIAL different type, similar spreadsheet or SQL tables 

3. Yes, hardcored  data can be added into pandas by actually writing the data in list of list format.
	 Pandas accepts data types such as:
   
	  	Scalar values - integers / string values 
      
		  Python Dictionary - key value pairs 
      
		  NDarray - multidimensional, homogeneous array of  fix sizes items. 
      
4. How to read in pandas the following formats:
  
 Excel single sheet: pd.read_excel(‘file.xlsx’)	
                   : df.to_excel(‘path to xlsx’, sheet_name = “sheet 1”)
 
 Excel multiple sheets: 
		     : xlsx = pd.ExcelFile(‘file.xls’)
		     : dp= pd.read_excel(xlsx, ‘sheet 1’)
  
 CSV & text
		     :  pd.read_csv( ‘file.csv’, header=None, nrows=5)  
         :  df.to_csv ( 'pat/myDataFrame.csv' )
 
 PDF                 
         : Method 1. 
            from tabula import read_pdf
		        Df = read_pdf( “data.pdf”)
	        : Method 2.
		        Copy pdf file into Excel then separate the data into colums 
		        Use excel method, see Q4
	
5. Pandas is a library used in Python and it can be used with other libraries such as SciPy and Matplotlib
6. df.to_csv( r’Path to store exported csv file\FileName.csv’)



