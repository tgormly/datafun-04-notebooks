# datafun-04-notebooks
Work for Week 4 in Data Analytics Fundamentals 44608-80


Task 0 - get started
Log in to your GitHub account. 
Create a new GitHub repo named datafun-04-notebooks.
Git clone your new repo into your Documents folder. 
Ensure your repo has the 3 basic files all our repos need:
a good README.md,
.gitignore, and
about.py. 
Copy these from previous repos as needed.
Update README.md to reflect the focus of this module. 
Add new files to your repo as described below.
Git add, git commit, and git push (commit/sync in VS Code) your updated content to GitHub.
Authors examples: You're encouraged to use the authors examples for practice. Use these right from your local IntroToPython directory - don't commit the author's work into your repo. 

 

Task 1 - yourname_1.ipynb
Start the Jupyter environment on your machine from your Documents folder.
Use the navigation window to get to your repo for this module. 
In your repo, create a new notebook in Jupyter (name the file yourname_1.ipynb), so mine might be denisecase_1.ipynb.
Research how to add Markdown to a Jupyter notebook.
At the top of your new notebook, change the first cell from Python to Markdown.
Add your name as a top-level heading in Markdown at the top of the file (hint: # Denise Case's Module 4 Project)
In the next cell of your notebook, change back to Python code. 
Use the text, do a search, find a video, and/or use the forum to share resources for getting acquainted with notebooks. We won't duplicate those resources here. 

Add a Markdown cell for each section heading.

## Task 1 - Series 
We'll look at using a one-dimensional pandas Series to hold and process simple exam data.
Follow the instructions in 7.14 to import the pandas module (as pd).
Create a pandas Series named grades from a list of integers (exam scores).
Get the value of the first grade with grades[0].
Call the built in Series functions: count(), mean(), min(), max(), std(), and describe().
## Task 2 - Series from Dictionary
Follow the instructions in the "Dictionary Initializers' subsection to modify your code to initialize grades with a dictionary (a set of key-value pairs instead) - we'll use the student name as the key  and their exam score as the value. 
Get Eva's score by calling grades['Eva']
Get Wally's score using the easier dot notation: grades.Wally.  This is much more common and can be used as long as there are NO spaces in the key text.  If there are spaces, you'll have to use the approach we used for Eva above - wrapping the key in single quotes. 
Use the Series values attribute to display the array of values. 
Complete the self-check on Page 266. 
We can use a Series whenever our values are a simple one-dimensional array.  
Make sure the notebook is nicely formatted with a heading and sections in Markdown clearly dividing the work. 
Run the entire file and export the results to yourname_1.html. This will display your calculated results. 

 

Task 2 - yourname_2.ipynb
See the text Ch 7.14.2.
For more complex data, we can use a DataFrame. In a DataFrame, each value is a Series of numbers.
We can use a two-dimensional DataFrame to handle many  exam scores for each key/student.
Create a new notebook to practice using DataFrames.
Name the notebook yourname_2.ipynb.
Use your Markdown skills to add a customized title to your notebook. 
Use Markdown heading for each section below.
## Task 1. Create DataFrame

Follow the instructions in 7.14.2 to import pandas as pd and create a pandas DataFrame from a dictionary (a set of key-value pairs) holding multiple exam scores for each key/student. In this example, we have 5 students, each with 3 exam scores, but the scores aren't labeled.  
## Task 2. Custom Index

Follow the instructions to apply a custom index (instead of 0,1,2), let's call them 'Test1', Test2', and 'Test3'. See 'Customizing a DataFrame's Indices with the index Attribute subsection. 
As we did in Part 1, we can request grades by key using the text attribute (square brackets with single quoted text strings). Find Eva's grades with grades['Eva'] 
If no spaces in the key, we can use the simpler dot attribute approach. Find Sam's grades with grades.Sam as shown in 'Accessing a DataFrame's columns' subsection. 
## Task 3. Accessing Rows (loc, iloc)

Like spreadsheets, we can access specific rows or columns.
We use loc['ColA'] and iloc[i]  to access rows by name and index, respectively.
Execute the examples using loc['Test1'] to get scores for the first exam, or iLoc[0] to get scores for the first exam and iLoc[1] to get scores for the second exam. Which do you prefer? 
We can also get slices of rows, e.g., from ['Test1':'Test3'], inclusive, or, using index values, from [0:2], inclusive.
## Task 3. Accessing Subsets (at, iat)

We can use similar notation to get a single cell in the DataFrame (much like getting a single cell in a spreadsheet). 
Use grades.at['Test2', 'Eva'} to find her score on the second exam using labels.
Use grades.iat[2,0] to get the score on the third exam for the first student (Wally), using indices. 
## Task 4. Describe (By Column)

Use grades.describe() to get descriptive statistics for our gradebook columns.
See why learning Python and DataFrames can be so powerful?  
Try to set the precision using the pd.set_option('precision',2) provided.
Does it work? Libraries are evolving. If you get an error, copy the error text and do a web search.
Can you find something about a newer option using "display.precision"?
If so, try pd.set_option("display.precision",2).
Being able to debug evolving features on your own is important for success.
Our field, languages, and libraries are constantly evolving. 
## Task 5. Transpose (rows <--> columns)

Get the average for each column by calling grades.mean()
Transpose the DataFrame using the T attribute.
Get the mean by the new columns with .T.describe()
## Task 6. Sort 

Sort the gradebook rows in reverse order so the most recent exam row appears at the top with grades.sort_index(ascending=False)
Sort the gradebook columns so the names appear in order using grades.sort_index(axis=1).
We can sort our data pretty much however we like. 
Make sure the notebook is nicely formatted with a heading and sections in Markdown clearly dividing the work. 

Run the entire file and export the results to yourname_2.html. This will display your calculated results. 

Minimal submissions earn minimal credit. Repos clearly demonstrating practice, in an organized fashion, with custom notes and remarks are eligible for maximum credit. 

 

Task 3. Push Repo to GitHub
Your repo should at least the 3 basic files. 2 notebooks, and 2 exported html files.

Use VS Code to commit and sync (push) your repo to GitHub - or in Git Bash or terminal, do the following. 

git add .
git commit -m "added code"
git push origin main
Task 4.  Read about String Methods
String methods are helpful for processing text.
For now, in 8.9, read "Joining Strings" on page 295 carefully.
string.join() is an important and widely used method when working with text. 
The string holds the separator and we pass one argument to the join() method - a list, or a list comprehension.
Get an idea of what's possible with strings and string methods. 
In 8.11, read about raw strings (with an r instead of an f in front).
In 8.12, read about regular expressions - a powerful way to locate specific elements of text (e.g. a phone number). 
We'll do more with strings and text in Web Mining and NLP.
If you want some practice now, try the bonus.
 

Optional Task 5 (Bonus).
Raw data is rarely ready for use.
Data preparation can be about 75% (or more) of our work.
Work through Ch 8.13 to get an idea of wrangling (cleaning & transforming) data.
On your machine, in your repo, create an additional notebook named xtra_p4.ipynb.
Start by creating the list of contacts in "Reformatting your Data" on page 310.
Create a DataFrame. 
The phone numbers are not formatted.
Follow the text to create a function that uses regular expressions (usually abbreviated regex or re) to create a function to get a formatted version of the unformatted phone number. 
Use map() and your function to improve the DataFrame 
Verify phone numbers now appear with two dashes (e.g., 555-555-5555). 
Prepare your notebook with a nice header (include a title, your name, and date)
Clearly label your steps and result. 
Execute the entire notebook, export it to xtra_p4.html.
Commit and push both files into your GitHub repo. 
Reflection (on your own)
Notebooks and scripts are both important.

Scripts for automated, unattended processes (e.g. fetch a file with daily sales).
Scripts for reusable functions so the module can be imported. 
Notebooks for initial data exploration - it makes it easy to add visualizations and remarks to your analysis. 
DataFrames and Series are widely used.

Can you think of something in your domain (or at work or in a personal project) that would be good for either a DataFrame or a Series?  Would it be better as a script/module or as a notebook? 

