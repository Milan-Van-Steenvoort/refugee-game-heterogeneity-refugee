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

class Constants(BaseConstants):
    name_in_url = 'task_typing_real'
    players_per_group = None
    num_rounds = 5 # must be more than the max one person can do in task_timer seconds

    reference_texts = [
        'Y90ZQ4gFV4x7',
        'WSx7IJ8Y3wd7',
        '6gt6k1dZ7zQT',
        '8gkmGZY3Cuw7',
        'tz4hJ6NqfZP3',
    ]

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# Assignment and storage of treatment. Beware: hl_sim refers to the high group whereas lh_sim refers to the low group

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

class Group(BaseGroup):
	pass

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# participant_vars allows to pass on variables across rounds and apps - handy for treatment 
# instruction_form refered to the gender of the instructions, which could be chosen in the German version of the experiment

class Player(BasePlayer):

    #instruction_form = models.LongStringField()
    participant_vars = models.LongStringField()

# (1) Variables related to the typing task (similar as practice)
#---------------------------------------------------------------

# For next week:I will probably have to define the user_text_error_message at the player level again and then also change the field in the html. 

    def score_round(self):
        # update player payoffs
        if (self.correct_text == self.user_text):
            self.is_correct = True
            self.payoff_score = 10

        else: 
            self.is_correct = False
            self.payoff_score = c(0)

    effort_earning =  models.IntegerField()        
    treatment = models.StringField()
    treatment_test = models.StringField()
    
    # Amount of incorrect attempts for all the questions
    incorrect_attempts1 = models.IntegerField(initial=0)  
    incorrect_attempts2 = models.IntegerField(initial=0)      
    incorrect_attempts3 = models.IntegerField(initial=0)  
    incorrect_attempts4 = models.IntegerField(initial=0)
    incorrect_attempts5 = models.IntegerField(initial=0)  
    incorrect_attempts6 = models.IntegerField(initial=0)   
    incorrect_attempts7 = models.IntegerField(initial=0)  
    incorrect_attempts8 = models.IntegerField(initial=0)   
    incorrect_attempts9 = models.IntegerField(initial=0)  
    incorrect_attempts10 = models.IntegerField(initial=0) 
    incorrect_attempts11 = models.IntegerField(initial=0)       
    
 
    # def get_treatment(self):
        # if self.round_number > 1:
            # treatment = self.participant.vars['treatment_assigned']
    
    
    correct_text = models.CharField(
        doc="user's transcribed text")

    user_text = models.CharField(initial = '')
    
    def user_text_error_message(Player,value):
        print('value is', value)
        if value!= Player.correct_text:
            Player.user_text = value
            return 'There is an error in the number-letter sequence you entered. Please try again.'

    is_correct = models.BooleanField(
        doc="did the user get the task correct?")

    ret_final_score = models.IntegerField(
        doc="player's total score up to this round")

    payoff_score = models.CurrencyField(
            doc = '''score in this task'''
        ) 
 
# (2) Variables related to test questions
#---------------------------------------------------------------  

            # QUESTIONS

#number of groups of citizens _all treatments     
    t1_number_of_citizens_groups = models.IntegerField(
      choices=[
        [1, '1'],
        [2, '2'],
        [3, '3'],
      ], label='How many groups of citizens are there in total?',
        widget=widgets.RadioSelect)

#number of  citizens _all treatments     
    t2_number_of_citizens = models.IntegerField(
      choices=[
        [2, '2'],
        [3, '3'],
        [4, '4'],
      ], label='How many citizens are there per group?',
        widget=widgets.RadioSelect)
        
#numbers of refugees _all treatemnts
    t3_number_of_refugees = models.IntegerField(
      choices=[
        [1, '1'],
        [2, '2'],
        [3, '3'],
      ], label='How many refugees are there?',
        widget=widgets.RadioSelect)

#earnings _high

    t4_points_h = models.IntegerField(
      choices=[
        [50, '50'],
        [25, '25'],
        [75, '75'],
      ], label='How many points do citizens from your group receive in the typing task?',
        widget=widgets.RadioSelect)

#earnings _low

    t4_points_l = models.IntegerField(
      choices=[
        [50, '50'],
        [25, '25'],
        [75, '75'],
      ], label='How many points do citizens from your group receive in the typing task?',
        widget=widgets.RadioSelect)

#earnings other _high

    t5_points_other_h = models.IntegerField(
      choices=[
        [50, '50'],
        [25, '25'],
        [75, '75'],
      ], label='How many points do citizens from the other group receive in the typing task?',
        widget=widgets.RadioSelect)

#earnings other _low

    t5_points_other_l = models.IntegerField(
      choices=[
        [50, '50'],
        [25, '25'],
        [75, '75'],
      ], label='How many points do citizens from the other group receive in the typing task?',
        widget=widgets.RadioSelect)


# refugee participants is
        
    t6_refugee_participant = models.IntegerField(
      choices=[
        [1, 'A participants in another study'],
        [2, 'A participant in this study'],
        [3, 'The role of the refugee is not taken by any real person'],
      ], label='The player who takes on the role of the refugee is',
        widget=widgets.RadioSelect)


# contribution _high
    t7_contribution_example_h = models.IntegerField(
      choices=[
        [1, '4 citizens x 15 points (20 percent of 75 points) = 60 points'],
        [2, '4 citizens x 30 points (40 percent of 75 points) = 120 points'],
        [3, '4 citizens x 45 points (60 percent of 75 points) = 180 points'],
      ], label='Each citizen from your group receives 75 points in the typing task. How many points are added to the common account of your group?',
        widget=widgets.RadioSelect) 

# contribution _low
    t7_contribution_example_l = models.IntegerField(
      choices=[
        [1, '4 citizens x 5 points (20 percent of 25 points) = 20 points'],
        [2, '4 citizens x 10 points (40 percent of 25 points) = 40 points'],
        [3, '4 citizens x 15 points (60 percent of 25 points) = 60 points'],
      ], label='Each citizen from your group receives 25 points in the typing task. How many points are added to the common account of your group?',
        widget=widgets.RadioSelect)     

# contribution other _high
    t8_contribution_other_example_h = models.IntegerField(
      choices=[
        [1, '4 citizens x 15 points (20 percent of 75 points) = 60 points'],
        [2, '4 citizens x 30 points (40 percent of 75 points) = 120 points'],
        [3, '4 citizens x 45 points (60 percent of 75 points) = 180 points'],
      ], label='Each citizen from the other group receives 75 points in the typing task. How many points are added to the common account of the other group?',
        widget=widgets.RadioSelect) 

# contribution other _low
    t8_contribution_other_example_l = models.IntegerField(
      choices=[
        [1, '4 citizens x 5 points (20 percent of 25 points) = 20 points'],
        [2, '4 citizens x 10 points (40 percent of 25 points) = 40 points'],
        [3, '4 citizens x 15 points (60 percent of 25 points) = 60 points'],
      ], label='Each citizen from the other group receives 25 points in the typing task. How many points are added to the common account of the other group?',
        widget=widgets.RadioSelect)         

# helping
    t9_helping = models.IntegerField(
      choices=[
        [1, 'Between 0 percent and 20 percent'],
        [2, 'Between 0 percent and 30 percent'],
        [3, 'Between 0 percent and 40 percent'],
      ], label='What percentage of your common account can citizens from your group share with the refugee?',
        widget=widgets.RadioSelect)

# helping other
    t10_helping_other = models.IntegerField(
      choices=[
        [1, 'Between 0 percent and 20 percent'],
        [2, 'Between 0 percent and 30 percent'],
        [3, 'Between 0 percent and 40 percent'],
      ], label='What percentage of their common account can citizens from the other group share with the refugee?',
        widget=widgets.RadioSelect)

# timing of the decision fm 
    t11_timing_fm = models.IntegerField(
      choices=[
        [1, 'Before the other group makes their decision'],
        [2, 'After the other group makes their decision'],
        [3, 'At the same time that the other group makes their decision'],
      ], label='There are two groups in the experiment. When are you and the other participants in your group making the decision?',
        widget=widgets.RadioSelect)

# timing of the decision sm 
    t11_timing_sm = models.IntegerField(
      choices=[
        [1, 'Before the other group makes their decision'],
        [2, 'After the other group makes their decision'],
        [3, 'At the same time that the other group makes their decision'],
      ], label='There are two groups in the experiment. At what time are you and the other participants in your group making the decision?',
        widget=widgets.RadioSelect)

# timing of the decision sim 
    t11_timing_sim = models.IntegerField(
      choices=[
        [1, 'Before the other group makes their decision'],
        [2, 'After the other group makes their decision'],
        [3, 'At the same time that the other group makes their decision'],
      ], label='There are two groups in the experiment. At what time are you and the other participants in your group making the decision?',
        widget=widgets.RadioSelect)

                    # ANSWERS


# Questions 1-3, 6 and 9 are similar across treatments

    def t1_number_of_citizens_groups_error_message(self, value):
      print('value is', value)
      if value != 2:
         self.incorrect_attempts1 += 1
         return 'Wrong answer. Please try again.'
         
    def t2_number_of_citizens_error_message(self, value):
      print('value is', value)
      if value != 4:
         self.incorrect_attempts2 += 1
         return 'Wrong answer. Please try again.'

    def t3_number_of_refugees_error_message(self, value):
      print('value is', value)
      if value != 1:
         self.incorrect_attempts3 += 1
         return 'Wrong answer. Please try again.'

    def t6_refugee_participant_error_message(self, value):
      print('value is', value)
      if value != 2:
         self.incorrect_attempts6+= 1
         return 'Wrong answer. Please try again.'
         
    def t9_helping_error_message(self, value):
      print('value is', value)
      if value != 1:
         self.incorrect_attempts9+= 1
         return 'Wrong answer. Please try again.'

    def t10_helping_other_error_message(self, value):
      print('value is', value)
      if value != 1:
         self.incorrect_attempts10+= 1
         return 'Wrong answer. Please try again.'


# Question 4 differs between high and low treatment groups

    def t4_points_h_error_message(self, value):
      print('value is', value)
      if value != 75:
         self.incorrect_attempts4 += 1
         return 'Wrong answer. Please try again.'
         

    def t4_points_l_error_message(self, value):
      print('value is', value)
      if value != 25:
         self.incorrect_attempts4 += 1
         return 'Wrong answer. Please try again.'
         
         
# Question 5 differs between high and low 'other' treatment groups

    def t5_points_other_h_error_message(self, value):
      print('value is', value)
      if value != 75:
         self.incorrect_attempts5 += 1
         return 'Wrong answer. Please try again.'
         
         
    def t5_points_other_l_error_message(self, value):
      print('value is', value)
      if value != 25:
         self.incorrect_attempts5 += 1
         return 'Wrong answer. Please try again.'

# Question 7 differs between high and low  treatment groups

    def t7_contribution_example_h_error_message(self, value):
      print('value is', value)
      if value != 2:
         self.incorrect_attempts7 += 1
         return 'Wrong answer. Please try again.'
         
         
    def t7_contribution_example_l_error_message(self, value):
      print('value is', value)
      if value != 2:
         self.incorrect_attempts7 += 1
         return 'Wrong answer. Please try again.'

# Question 8 differs between high and low 'other' treatment groups

    def t8_contribution_other_example_h_error_message(self, value):
      print('value is', value)
      if value != 2:
         self.incorrect_attempts8 += 1
         return 'Wrong answer. Please try again.'
         
         
    def t8_contribution_other_example_l_error_message(self, value):
      print('value is', value)
      if value != 2:
         self.incorrect_attempts8 += 1
         return 'Wrong answer. Please try again.'

# Question 11 differs between fm, sm and sim treatment groups

    def t11_timing_fm_error_message(self, value):
      print('value is', value)
      if value != 1:
         self.incorrect_attempts11 += 1
         return 'Wrong answer. Please try again.'
         
         
    def t11_timing_sm_error_message(self, value):
      print('value is', value)
      if value != 2:
         self.incorrect_attempts11 += 1
         return 'Wrong answer. Please try again.'

    def t11_timing_sim_error_message(self, value):
      print('value is', value)
      if value != 3:
         self.incorrect_attempts11 += 1
         return 'Wrong answer. Please try again.'


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

#-------
# NOTES 
#-------

#Changes compared to Maik: 
#--------------------------
# Why do we need the instruction_form variable? Without it, it works perfectly
# According to the templates Instructions_4_2, this dummy refers to either the male (1) or female (0) version of the game. It can thus safely be ignored

#This I will probably have to do: 
# Instead of using an html widget, I used the formfield expression for user_text - I did not do this
# I moved the user_text_error_message from pages to models, and defined it at the player level. I also slightly changed the formfield error in task.html, line 31 - I did not do the second part 
# I desactivated the total payoff in the part where we defined the variables to be brought over to templates -> in this experiment, they receive a fixed payment (lines 46-49 and 61 of pages)
# I removed the debug part, line 56 in pages and for the cheatmode section in task.html. For some reasons, it made it impossible to run the experiment
# I defined the treatment part in the svo app rather than in the actual typing app, as this allows me to skip those apps for the refugee treatment. This definition is done in subsession in models.py (also in player level, need treatment variable)