# Tweets-degree-of-profanity
A python code to clean the data and indicate the degree of profanity in the tweets file.

### THE SAMPLE INPUT TWEETS FILE IS "tweets.xls" AND THE SAMPLE TEXT FILE WITH RACIAL SLUR WORDS IS "slur_words.txt".

NOTE: The tweets present in the tweets.xls file are not the origianl tweets but are just created to use them as a simple sample input file. The racial slur words in the text file are some sample words taken from wikipedia.

step1: Ask the user for the file type (whether it is a csv file or an xls file),
step2: Ask the user if the input file has a header,
step3: Read the given file into a dataframe named "tweets",
step4: Change the old column name of the tweets to an understandable column name "Tweets",
step5: Ask the user to give the name of the text file that contains the Racial Slur words list,
step6: Read the text file and store all the racial slur words to a python list named words,
step7: In the sample dataset, each tweet is started with "@" and a user name. Split the user name and put it in a separate column named "user",
step8: Have the tweet without any other information (like user name) in the "Tweets" column,
step9: Create a new column named "Total Words" to store the number of words present in the tweet,
step10: Write a function to count the number of racial slur words present in the tweet,
step11: Put all the slur words in a column named "Slur Words" and Count the number of slur words using the above function and put it in a separate column named "Slur Words Count" in the dataframe,
step12: Calculate the degree of profanity by dividing number of slur words in a tweet to the total number of words in the tweet and add those values to a column named "Degree of Profanity",
step13: Save the result (dataframe) to a new csv file (In this case, the file is saved as "Profanity_check.csv").
