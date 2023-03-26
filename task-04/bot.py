import csv

import telebot
import os
import telebot
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater

import ast
import time
from telebot import types



from OMDB import get_movie_info

# bot = telebot.TeleBot("5681244979:AAHZ2DpRbCED8YGYDzY-uuxbvtnWSwsD-t8") # You can set parse_mode by default. HTML or MARKDOWN







BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
# @bot.message_handler(commands=['start', 'help'])

# def send_welcome(message):
#     bot.reply_to(message, "787878787, how are you doing?")



# # Handles all text messages that contains the commands '/start' or '/help'.
# @bot.message_handler(commands=['hello', 'hi'])
# def handle_start_help(message):
#      bot.reply_to(message, "0000, how are you doing?")



# # Handles all sent documents and audio files
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass

# # Handles all text messages that match the regular expression
# @bot.message_handler(regexp="SOME_REGEXP")
# def handle_message(message):
#     pass

# # Handles all messages for which the lambda returns True
# @bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
# def handle_text_doc(message):
#     pass

# # Which could also be defined as:
# def test_message(message):
#     return message.document.mime_type == 'text/plain'

# @bot.message_handler(func=test_message, content_types=['document'])
# def handle_text_doc(message):
#     pass

# # Handlers can be stacked to create a function which will be called if either message_handler is eligible
# # This handler will be called if the message starts with '/hello' OR is some emoji
# @bot.message_handler(commands=['0'])
# # @bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)

# def send_something(message):
#      bot.reply_to(message, " again again again ")


# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

# bot.infinity_polling()





import csv
import json

#-------------------------------------------------------------------------------------------------
# import os
# import telebot
import requests

# # TODO: 1.1 Get your environment variables 
# yourkey = os.getenv()
# bot_id = os.getenv()

# bot = telebot.TeleBot()



@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])

def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    with open('movies.csv', 'w', newline='') as file:
            file.write('')


    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    # bot.reply_to(message, 'wait movie info...')
    # print('hello')
    # print(message.text)

    print('hello tooo')
    bot.reply_to(message, 'Getting movie info... ')
    # TODO: 1.2 Get movie information from the API

    movie_name = message.text
    
    print(movie_name)
    # movie_name=movie_name.lstrip[6: ]
    # print(movie_name)
    movie = movie_name.split(' ', 1)[1]
    # print('------------------------')
    # print(movie)


   




    movie_info = get_movie_info(movie)

    
    
    
    if movie_info:
        rating_string = f"IMDb Rating: {movie_info['imdb_rating']}\n"
        # for rating in movie_info['ratings']:
        #     rating_string += f"{rating['Source']}: {rating['Value']}\n"
               
        message_text = (f"poster\n{movie_info['Poster']}\n\n" +
            f"{movie_info['title']} ({movie_info['year']}):\n\n" + 
            

            # f"Plot:\n{movie_info['plot']}\n\n" +
            f"Starring:\n{movie_info['actors']}\n\n" +
            f"Ratings:\n{rating_string}"
            ) 
        # print('movie found')
        # print(movie_info)
        # print(message_text)
       

        # @bot.message_handler(content_types=['document', 'audio'])
        # def handle_docs_audio(message):
        #     bot.reply_to(message,f"Plot:\n{movie_info['Poster']}\n\n")
         
        #bot.reply_to(message,message_text)
        bot.send_message(message.chat.id,message_text)

         # TODO: 1.3 Show the movie information in the chat window


    # TODO: 2.1 Create a CSV file and dump the movie information in it
    
        #fields = ['Title', 'Year of Release', 'IMDb Rating' ] 
    
       

        movie=[[movie_info['title'] ,movie_info['year'],movie_info['imdb_rating']]]
        print(movie)




    # writing to csv file 
        with open("movies.csv", 'a') as csvfile: 
    # creating a csv writer object 
               csvwriter = csv.writer(csvfile) 
          
    # writing the fields 
               #csvwriter.writerow(fields) 
          
    # writing the data rows 
               csvwriter.writerows(movie)

            #    csvwriter.writerow(rows)

        csvfile.close()

        

        
    else:{
         bot.reply_to(message, 'Movie Not Found...!')

    }
        
        
    
    
   

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...Please wait')
    with open("movies.csv", 'r') as csvfile: 
       
    
   
        


        bot.send_document(message.chat.id,csvfile)
       
        csvfile.close()

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()