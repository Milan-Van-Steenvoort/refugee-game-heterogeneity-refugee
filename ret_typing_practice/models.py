# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)
import random


# </standard imports>
#adapted version of:

author = 'Curtis Kephart (economicurtis@gmail.com)'

doc = """
Real Effort Task. Type as many strings as possible.  
"""
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

#These are all the variables defined as constants

class Constants(BaseConstants):
    name_in_url = 'task_typing'
    players_per_group = None
    num_rounds = 2 # must be more than the max one person can do in task_timer seconds #see Subsession, before_session_starts setting. 
    #In this experiment the amount of rounds is fixed.

    reference_texts = [
        '6v4jsM4PLnP8',
        '3wd7p9cQpnqW',
        'V4x7B58ovNk3',
    ]

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------     

class Group(BaseGroup):
	pass

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# These are all the variables defined at the subsession level.
# The subsession here refers to the practice typing exercise (it is a subsession of the entire experiment)
# 1: The first variable we create is players, which is a list of all players (get_players)
# 2: The second variable we create is p. correct_text, which refers to the reference texts defined as constants

class Subsession(BaseSubsession):
    def creating_session(self):

        players = self.get_players()

        for p in self.get_players():
            p.correct_text = Constants.reference_texts[self.round_number - 1]

        for p in self.get_players():
            p.treatment = p.participant.vars['treatment_assigned']    
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# These are all the variables defined at the player level. 
# For each player, we define: 
    # his score in the round. The 'if' implies that if user_text is equal to correct_test, then he is correct and his payoff score is 10. Otherwise, the payoff score is 0
        # This variable is not used
    # the correct text
    # the user text, for which we specify the initial value of ''
    # a dummy variable that tells us whether the player got his answer right (1) or wrong (0)
    # his final score, up to this round
    # his payoff score in the task

class Player(BasePlayer):
    
    treatment = models.StringField()
    user_text = models.CharField(initial = '')

    def user_text_error_message(Player,value):
        print('value is', value)
        if value!= Player.correct_text:
            Player.user_text = value
            return 'There is an error in the number-letter sequence you entered. Please try again.'


#This part is not used. Since the payoff is fixed in this experiment
    def score_round(self):
        # update player payoffs
        if (self.correct_text == self.user_text):
            self.is_correct = True
            self.payoff_score = 10

        else: 
            self.is_correct = False
            self.payoff_score = c(0)

    correct_text = models.CharField(
       doc="user's transcribed text")

    is_correct = models.BooleanField(
        doc="did the user get the task correct?")

    ret_final_score = models.IntegerField(
        doc="player's total score up to this round")

    payoff_score = models.CurrencyField(
            doc = '''score in this task'''
        )

    round_count = models.IntegerField(
        doc="number of rounds completed")

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

#-------
# NOTES 
#-------

#Changes compared to Maik: 
#--------------------------
# Instead of using an html widget, I used the formfield expression for user_text
# I moved the user_text_error_message from pages to models, and defined it at the player level. I also slightly changed the formfield error in task.html, line 31
# I desactivated the total payoff in the part where we defined the variables to be brought over to templates -> in this experiment, they receive a fixed payment (lines 46-49 and 61 of pages)
# I removed the debug part, line 56 in pages and for the cheatmode section in task.html. For some reasons, it made it impossible to run the experiment