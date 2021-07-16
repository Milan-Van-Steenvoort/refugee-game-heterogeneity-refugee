# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)
# </standard imports>

author = 'Milan Van Steenvoort'

doc = """
Refuge Game
"""

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Constants(BaseConstants):
    name_in_url = 'refugee_decision'
    players_per_group = None
    num_rounds = 1


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# extract treatment from participant var

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
    decision = models.IntegerField()
    effort_earning = models.IntegerField()
    private_earning = models.FloatField()
    contribution = models.FloatField()
    participant_vars_dump = models.StringField()
    treatment = models.StringField()

    decision_sm_1 = models.IntegerField()
    decision_sm_2 = models.IntegerField()
    decision_sm_3 = models.IntegerField()
    decision_sm_4 = models.IntegerField()
 
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

#-------
# NOTES 
#-------

#Changes compared to Maik: 
#--------------------------
# Deleted instruction_form variable, as it is gender neutral in English 
# Deleted the stringfield option in the htmls. It somehow blocked the experiment, and does not seem necessary.

