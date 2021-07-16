from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from django.conf import settings
import random

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------



# Only display the page in round one 

class start(Page):

    def is_displayed(self):
        return self.round_number == 1

    

    # def vars_for_template(self):

        # return {
            # 'debug': settings.DEBUG,  
        # }

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# The first part tells us that we display the user text entry in the task page
    # We define its position in the html file, in 'templates':  {{ player.user_text }}
# The second part defines an error message if the value entered by the player is different from the correct answer
# The third part is used to pass variables to the template. It defines the total payoff for players. Initially, it is set at zero and for every player in all rounds, it is augmented by the player's payoff score if the latter is superior to 0 (None). 
    #It also returns (the payoff and) the number of already played rounds (in templates,{{round_count}}).

class task(Page):
    form_model = models.Player
    form_fields = ['user_text']
    # timeout_seconds = self.player.ret_timer # time? no, only works on specific pages

    def vars_for_template(self):
        # current number of correctly done tasks
        #total_payoff = 0
        #for p in self.player.in_all_rounds():
            #if p.payoff_score != None: 
                #total_payoff += p.payoff_score

        # set up messages in transcription task
        # if self.round_number == 1: #on very first task
        #     correct_last_round = "<br>"
        # else: #all subsequent tasks
        #     if self.player.in_previous_rounds()[-1].is_correct:
        #         correct_last_round = "Ihre letzte Eingabe war <font color='green'>korrekt</font>."
        #     else: 
        #         correct_last_round = "Ihre letzte Eingabe war <font color='red'>falsch</font>."
        
        return {
            #'total_payoff': round(total_payoff),
            'round_count':(self.round_number - 1),
            #'debug': settings.DEBUG,
            # 'correct_last_round': correct_last_round,        
        }



    def before_next_page(self):
        self.player.score_round()

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# We don't have this page in our experiment 

class ResultsWaitPage(WaitPage):
    pass
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def after_all_players_arrive(self):
        pass

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# We don't have this page in our experiment 

class Results(Page):
    pass

# Not needed because it is a practice task and payoff is calculated after the experiment    
"""     def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        total_payoff = 0
        for p in self.player.in_all_rounds():
            if p.payoff_score != None: 
                total_payoff += p.payoff_score

        

        # only keep obs if YourEntry player_sum, is not None. 
        table_rows = []
        for prev_player in self.player.in_all_rounds():
            if (prev_player.user_text != None):
                row = {
                    'round_number': prev_player.round_number,
                    'correct_text': prev_player.correct_text,
                    'user_text': prev_player.user_text,
                    'is_correct':prev_player.is_correct,
                    'payoff': round(prev_player.payoff_score),
                }
                table_rows.append(row)
        # round turns total_payoff into an integer
        return {
        'table_rows': table_rows,
        'total_payoff':round(total_payoff),
        } """

            
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

page_sequence = [start,task]








        