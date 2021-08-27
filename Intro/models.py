from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Milan Van Steenvoort'

doc = """
Introduction and consent
"""

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Constants(BaseConstants):
    name_in_url = 'Intro'
    players_per_group = None
    num_rounds = 1

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Subsession(BaseSubsession):
    pass

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Group(BaseGroup):
    pass

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# This defines a variable, at the player level, that takes value 1 if confirmed and 0 otherwise (Boolean: true/false)
# The variable will be displayed as a Checkbox
class Player(BasePlayer):

    consent_rules = models.BooleanField(
        widget=widgets.CheckboxInput(),
        label= "I hereby confirm that I have read and understood the declaration of consent for the experiment and I voluntarily declare that I am willing to participate in this study and that I consent to the processing of my data. Moreover, I understand that there will be exclusion checks, and that I therefore will be excluded and lose my right to remuneration in case I do not fulfill the exclusion checks",
    )

    is_mobile = models.BooleanField(doc="Automatic check through JS whether gadget is phone or not")

    prolific_id = models.CharField(
        initial = '',
        label="Prolific ID:",
    )

# Error messages

    def consent_rules_error_message(self, value):
      print('value is', value)
      if value != 1:
         return 'Your confirmation is required to proceed.'  

    def prolific_id_error_message(self, value):
      print('value is', value)
      if value =='':
         return 'Your Prolific ID is required to proceed.'   



