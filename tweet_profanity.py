import re #importing regex module
import pandas as pd #importing pandas

'''
### THE SAMPLE INPUT TWEETS FILE IS "tweets.xls" AND THE SAMPLE TEXT FILE WITH RACIAL SLUR WORDS IS "slur_words.txt

NOTE: The tweets present in the tweets.xls file are not the origianl tweets but are just created to use them as a simple sample input file. The racial slur words in the text file are some sample words taken from wikipedia

step1: Ask the user for the file type (whether it is a csv file or an xls file)
step2: Ask the user if the input file has a header
step3: Read the given file into a dataframe named "tweets"
step4: Change the old column name of the tweets to an understandable column name "Tweets"
step5: Ask the user to give the name of the text file that contains the Racial Slur words list
step6: Read the text file and store all the racial slur words to a python list named words
step7: In the sample dataset, each tweet is started with "@" and a user name. Split the user name and put it in a separate column named "user"
step8: Have the tweet without any other information (like user name) in the "Tweets" column
step9: Create a new column named "Total Words" to store the number of words present in the tweet
step10: Write a function to count the number of racial slur words present in the tweet
step11: Put all the slur words in a column named "Slur Words" and Count the number of slur words using the above function and put it in a separate column named "Slur Words Count" in the dataframe
step12: Calculate the degree of profanity by dividing number of slur words in a tweet to the total number of words in the tweet and add those values to a column named "Degree of Profanity"
step13: Save the result (dataframe) to a new csv file (In this case the file is saved as "Profanity_check.csv")
 '''

#STEP1
file_type=input('''What type of tweets file do you have (Enter the number)?
1. csv file
2. xls file :
''')


#STEP2
header_presence=input("Is the header present in the file? Y : N --->")

#STEP3
if file_type=="1":
    tweets=pd.read_csv("tweets.csv", header=True if header_presence=="Y" else None)
elif file_type=="2":
    tweets=pd.read_excel("tweets.xls", header=True if header_presence=="Y" else None)
else:
    print("Please enter 1 if the file is '.csv' else enter 2 if the file is '.xml'")


#STEP4
old_col = tweets.columns.to_list()[0]
tweets = tweets.rename(columns={old_col: "Tweets"})
print(tweets)


#STEP5
txt_file=input("Enter the text file that contains Racial Slur words list:  ")
with open("txt_file") as file:
#STEP6
    words=list(map(lambda x: x.strip(),file.readlines()))
    #print(words)


#STEP7
tweets["User"]=tweets["Tweets"].apply(lambda x: [str(x) for x in x.split() if x.startswith("@")][0])


#STEP8
tweets["Tweets"]=tweets["Tweets"].apply(lambda x: [x for x in x.split()[1:]])
tweets["Tweets"]=tweets["Tweets"].apply(lambda x: " ".join(x))


#STEP9
tweets["Total Words"]=tweets["Tweets"].apply(lambda x: len(x.split()))


#STEP10
def racial_slur_words(user_tweet):
    slur_words_in_tweet=[]
    for word in words:
        if re.search(word, user_tweet, re.IGNORECASE) is not None:
            slur_words_in_tweet.append(word)
        else:
            pass
    for _ in range(slur_words_in_tweet.count([])):
        slur_words_in_tweet.remove([])
    return ",".join(slur_words_in_tweet)


#STEP11
tweets["Slur Words"]=tweets["Tweets"].apply(racial_slur_words)
tweets["Slur Word Count"]=tweets["Slur Words"].apply(lambda x: len(x.split(",")))


#STEP12
tweets["Degree of Profanity"]=tweets["Slur Word Count"]/tweets["Total Words"]
print(tweets)


#STEO13
tweets.to_csv("Profanity_check.csv")
