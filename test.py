import logging
import os
from telegram.ext.updater import Updater
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
PORT = int(os.environ.get('PORT', 5000))
TOKEN = "YOURTOKENHERE"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


# hello
def start(update, context):
    update.message.reply_text("Hello! Any questions? Type /help ")


# help

#image
def image(update,context):
    chat_id = update.message.chat_id
    pic = open('Math_for_ML.pdf', 'rb')
    update.message.reply_text("""There are 4 main topics used in AI:
    Linear algebra
    Probability theory
    Multivariate calculus
    Optimization theory
    Here is awesome book that covers math these topics""")
    context.bot.send_document(chat_id, doc)


#
def help(update, context):
    update.message.reply_text("""Available commands: 
/ForBeginners (No Programming experience)
/WhatIsAI 
/Algorithms
/MathBook 
/Curriculum 
/Courses""")


# Option one (Brief information about AI)

def what_is_ai(update, context):
    update.message.reply_text("""According to Wikipedia: Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals and humans. AI research has been defined as the field of study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals.
According to IBM: It is the science and engineering of making intelligent machines, especially intelligent computer programs.It is related to the similar task of using computers to understand human intelligence, but AI does not have to confine itself to methods that are biologically observable""")


# Option two (Choice of algorithm)

def algo_choice(update, context):
    update.message.reply_text("""Please, choose algorithm:
/Linear_regression
/Logistic_regression                             
/Decision_tree
/SVM
/Naive_Bayes
/K_nearest_neighbours 
/K_means
/Random_forest
/Dimensionality_reduction
/Gradient_boosting""")


# Option 2.1 (Linear Regression)
def LR(update, context):
    update.message.reply_text("""You can watch this videos:
https://www.youtube.com/watch?v=zPG4NjIkCjc - An Introduction to Linear Regression Analysis
https://www.youtube.com/watch?v=nk2CQITm_eo - Linear Regression, Clearly Explained

And read this article:
http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm - Created by Yale university, one of the best universities in the world """)


# Option 2.2 (Logistic Regression)
def logR(update, context):
    update.message.reply_text("""You can watch this videos:
https://www.youtube.com/watch?v=3tq4t41MsPc - Logistic Regression: An Introduction
https://www.youtube.com/watch?v=yIYKR4sgzI8 - StatQuest: Logistic Regression

And read this articles:
https://www.ibm.com/topics/logistic-regression - Explaining from IBM, found this tutorial useful for myself
https://towardsdatascience.com/logistic-regression-detailed-overview-46c4da4303bc - Also good tutorial for Logistic regression """)


# Option 2.3 (Decision_tree)

def dt(update, context):
    update.message.reply_text(""" I would suggest this articles:
https://www.geeksforgeeks.org/decision-tree/ - GFG has excellent explanations, including this one
https://towardsdatascience.com/decision-trees-in-machine-learning-641b9c4e8052 - TDS also is one of the best source of explanations and tutorials specialized on AI 

Videos:
https://www.youtube.com/watch?v=ZVR2Way4nwQ - Decision Tree Classification Clearly Explained!
https://www.youtube.com/watch?v=_L39rN6gz7Y - Decision and Classification Trees, Clearly Explained!!!
""")


# Option 2.4 (Support Vector Machine)

def svm(update, context):
    update.message.reply_text("""Videos:
https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/resources/lecture-16-learning-support-vector-machines/ - Lecture of AI course made by MIT, world-class university specialized on STEM
https://www.youtube.com/watch?v=efR1C6CvhmE - tutorial by beloved StatQuest

Articles:
https://www.youtube.com/watch?v=_YPScrckx28 - Support Vector Machine (SVM) in 2 minutes
https://www.youtube.com/watch?v=ny1iZ5A8ilA - Support Vector Machines: All you need to know!""")


# Option 2.5 (Naive Bayes)

def nb(update, context):
    update.message.reply_text(""" Videos:
https://www.youtube.com/watch?v=nt63k3bfXS0 - Lecture by Stanford University, Andrew Ng is excellent lecturer
https://www.youtube.com/watch?v=lFJbZ6LVxN8 - Video that elucidates math behind Naive Bayes

Articles:
https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c
https://www.geeksforgeeks.org/naive-bayes-classifiers/ 
""")


# Option 2.6 (KNN)
def knn(update, context):
    update.message.reply_text(""" Videos:
https://www.youtube.com/watch?v=HVXime0nQeI- K-nearest neighbors, Clearly Explained
https://www.youtube.com/watch?v=09mb78oiPkA- Introduction to Learning, Nearest Neighbors

Articles:
https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761 
https://www.geeksforgeeks.org/k-nearest-neighbours/""")


def km(update, context):
    update.message.reply_text(""" Videos:
https://www.youtube.com/watch?v=4b5d3muPQmA - K-means clustering
https://www.youtube.com/watch?v=_aWzGGNrcic - K-means clustering: how it works

Articles:
https://www.javatpoint.com/k-means-clustering-algorithm-in-machine-learning
https://www.geeksforgeeks.org/k-means-clustering-introduction/""")


# Option 2.7 (Random Forest)

def rf(update, context):
    update.message.reply_text(""" Videos:
        https://www.youtube.com/watch?v=v6VJ2RO66Ag - Random Forest Algorithm Clearly Explained!
        https://www.youtube.com/watch?v=gkXX4h3qYm4 - What is Random Forest?

        Articles:
        https://www.geeksforgeeks.org/random-forest-regression-in-python/
        https://www.tutorialspoint.com/machine_learning_with_python/machine_learning_with_python_classification_algorithms_random_forest.htm""")


# Option 2.8 (Dimensionality Reduction)
def dr(update, context):
    update.message.reply_text(""" Videos:
https://www.youtube.com/watch?v=3uxOyk-SczU - Dimensionality Reduction
https://www.youtube.com/watch?v=rng04VJxUt4 - Lecture 14.4 — Dimensionality Reduction | Principal Component Analysis Algorithm

Articles:
https://machinelearningmastery.com/dimensionality-reduction-for-machine-learning/
https://en.wikipedia.org/wiki/Dimensionality_reduction""")


# Option 2.9 (Gradient Boosting)

def gr(update, context):
    update.message.reply_text(""" Videos:
https://www.youtube.com/watch?v=en2bmeB4QUo - Gradient Boosting : Data Science's Silver Bullet
https://www.youtube.com/watch?v=kho6oANGu_A - Boosting Machine Learning Tutorial

Articles:
https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/
https://towardsdatascience.com/all-you-need-to-know-about-gradient-boosting-algorithm-part-1-regression-2520a34a502
https://www.geeksforgeeks.org/ml-gradient-boosting/""")


# mathbook

def mathbook(update, context):
    chat_id = update.message.chat_id
    doc = open('Math_for_ML.pdf', 'rb')
    update.message.reply_text("""There are 4 main topics used in AI:
Linear algebra
Probability theory
Multivariate calculus
Optimization theory
Here is awesome book that covers math these topics""")
    context.bot.send_document(chat_id, doc)


def curriculum(update, context):
    update.message.reply_text("""If you need some curriculum, here is curriculum from Carnegie Mellon University:
https://www.cs.cmu.edu/bs-in-artificial-intelligence/curriculum""")


def courses(update, context):
    update.message.reply_text("""Here is some courses:
https://www.fast.ai/
https://d2l.ai/
https://ocw.mit.edu/courses/6-034-artificial-intelligence-spring-2005/
https://ocw.mit.edu/courses/6-867-machine-learning-fall-2006/
https://www.freecodecamp.org/learn/machine-learning-with-python/
""")


# For beginners in programming
def beginning(update, context):
    update.message.reply_text(""" 
https://www.edx.org/course/cs50s-introduction-to-programming-with-python - CS50 course from Harvard University
https://www.youtube.com/watch?v=2SpuBqvNjHI - If you feel, that you need more math knowledge, I recommend this video 
""")


# if command is unknown
def unknown_text(update, context):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("5637192348:AAF-Bq-vzG1Y3V1JocC5pirMCy9JolFNm3c", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("WhatIsAI", what_is_ai))
    dp.add_handler(CommandHandler("ForBeginners", beginning))
    dp.add_handler(CommandHandler("Algorithms", algo_choice))
    #
    dp.add_handler(CommandHandler("Linear_regression", LR))

    dp.add_handler(CommandHandler("Logistic_regression", logR))

    dp.add_handler(CommandHandler("Decision_tree", dt))

    dp.add_handler(CommandHandler("SVM", svm))

    dp.add_handler(CommandHandler("Naive_Bayes", nb))

    dp.add_handler(CommandHandler("K_nearest_neighbours", knn))

    dp.add_handler(CommandHandler("K_means", km))

    dp.add_handler(CommandHandler("Random_forest", rf))

    dp.add_handler(CommandHandler("Dimensionality_reduction", dr))

    dp.add_handler(CommandHandler("Gradient_boosting", gr))

    dp.add_handler(CommandHandler("MathBook", mathbook))
    dp.add_handler(CommandHandler("Curriculum", curriculum))

    dp.add_handler(CommandHandler("Courses", courses))

    dp.add_handler(MessageHandler(Filters.text, unknown_text))

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + TOKEN)

if __name__ == '__main__':
    main()
