from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Subsession(BaseSubsession):
    def creating_session(self):
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

class Player(BasePlayer):
    #instruction_form = models.IntegerField()
    treatment = models.StringField()

    age = models.IntegerField(
        label='Your age:',
        min=18, max=100)

    gender = models.StringField(
        choices=['Male', 'Female', 'Other', 'Prefer not to tell'],
        label='Your gender:',
        widget=widgets.RadioSelect)
    
    ending_time = models.LongStringField(doc="Time at which the ending page is reached")

    #equality condition
    
    #belief = models.IntegerField()
    
    #hochverdiener condition
    
    #belief_hoch_hoch = models.IntegerField() # first hoch represents condition, second hoch the player the belief is about
    
    #belief_hoch_gering = models.IntegerField() # hoch represents condition, gering the players the belief is about

    #geringverdiener condition
    
    #belief_gering_gering = models.IntegerField() # first gering represents condition, second gering the player the belief is about
    
    #belief_gering_hoch = models.IntegerField() # gering represents condition, hoch the players the belief is about
    
    
    
    left_right = models.IntegerField(
    choices=[
        [1, ''],
        [2, ''],
        [3, ''],
        [4, ''],
        [5, ''],
        [6, ''],
        [7, ''],
        [8, ''],
        [9, ''],
        [10, ''],
        [11, ''],
        ],
    label='In politics, people sometimes talk about "left" and "right". Where would you place yourself on a scale from "extreme left" to "extreme right"?',
    widget=widgets.RadioSelectHorizontal
    )
    
    #check1 = models.IntegerField(
    #choices=[
        #[1, ''],
        #[2, ''],
        #[3, ''],
        #[4, ''],
       #[5, ''],
       # [6, ''],
       # [7, ''],
        #],
    #label='Alle Bürger hatten die gleiche Möglichkeit, eine hohe Anzahl von Punkten in der Tippaufgabe zu verdienen.',
    #widget=widgets.RadioSelectHorizontal
    #)

    #check2 = models.IntegerField(
    #choices=[
       # [1, ''],
       # [2, ''],
       # [3, ''],
       # [4, ''],
       # [5, ''],
       # [6, ''],
       # [7, ''],
       # ],
    #label='Ich denke, die Tippaufgabe war für alle Bürger gleich fair.',
   # widget=widgets.RadioSelectHorizontal
    #)


