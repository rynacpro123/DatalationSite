from flask import Flask, render_template, url_for, request
import os
from dotenv import find_dotenv, load_dotenv


# Load environment variables from .env file (kickd)
load_dotenv()





#initialize flask appa
flask_app = Flask(__name__)


@flask_app.route('/')
@flask_app.route('/home')
def index():
    return render_template("index.html")

#
# # Define the Chatbot route
# @flask_app.route("/chatbot", methods=["POST"])
# def chatbot():
#
#     while True:
#
#         #obtain the message value input by the user in the message form
#         user_input = request.form['message']
#
#         #append the human response to our input messages list for future calls to openai
#         messages.append({"role": "user", "content": user_input})
#
#         #call openai and pass along message list containing all system, assistance and user inputs within the messages list
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",
#             temperature=0.9,
#             top_p=0.6,
#             max_tokens=200,
#             messages=messages
#         )
#
#         #extract the response text from the OpenAI API result
#         bot_response = response.choices[0].message.content
#
#
#
#
#         #append the bot response to our input messages list for future calls to openai
#         messages.append({"role": "assistant", "content": bot_response})
#
#
#         #Render the chatbot template with the response text
#         return render_template(
#             "chatbot.html",
#             user_input=user_input,
#             bot_response=bot_response,
#         )
#
#
#
# #
# # @app.route('/about')
# # def about():
# #     return render_template("about.html")
# #
# #
# # @app.route('/user/<string:name>/<int:id>')
# # def user(name, id):
# #     return "User name: " + name + " - id: " + str(id)

#start the flask app
if __name__ == "__main__":
    flask_app.run(debug=True, host="0.0.0.0", port=8000)
