from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from django.conf import settings
import time
import random

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# Only display the page in round one 

class Start(Page):
   
    #def vars_for_template(self):
        #self.player.instruction_form = self.participant.vars['treatment_assigned']
    
    def is_displayed(self):
        return (self.round_number == 1)


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# Each specific treatment html is only displayed if the player's treatment is the same
   
##########
# Page 1 #
##########

class Instructions_1(Page):
   
    #def vars_for_template(self):
        #self.player.instruction_form = self.participant.vars['treatment_assigned']
    
    def is_displayed(self):
        return (self.round_number == 1) 
  

##########
# Page 2 #
##########

class Instructions_2_hh_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_fm') 
        
class Instructions_2_hh_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_sim') 
        
class Instructions_2_hh_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_sm') 



class Instructions_2_hl_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_fm') 
        
class Instructions_2_hl_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_sim') 
        
class Instructions_2_hl_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_sm') 



class Instructions_2_ll_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_fm') 
        
class Instructions_2_ll_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_sim') 
        
class Instructions_2_ll_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_sm') 



class Instructions_2_lh_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_fm') 
        
class Instructions_2_lh_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_sim') 
        
class Instructions_2_lh_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_sm') 

##########
# Page 3 #
##########

class Instructions_3_hh_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_fm') 
        
class Instructions_3_hh_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_sim') 
        
class Instructions_3_hh_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_sm') 



class Instructions_3_hl_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_fm') 
        
class Instructions_3_hl_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_sim') 
        
class Instructions_3_hl_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_sm') 



class Instructions_3_ll_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_fm') 
        
class Instructions_3_ll_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_sim') 
        
class Instructions_3_ll_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_sm') 



class Instructions_3_lh_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_fm') 
        
class Instructions_3_lh_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_sim') 
        
class Instructions_3_lh_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_sm') 
        
##########
# Page 4 #
##########


class Instructions_4_2_hh_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_fm') 
        
class Instructions_4_2_hh_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_sim') 
        
class Instructions_4_2_hh_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_sm') 



class Instructions_4_2_hl_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_fm') 
        
class Instructions_4_2_hl_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_sim') 
        
class Instructions_4_2_hl_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_sm') 



class Instructions_4_2_ll_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_fm') 
        
class Instructions_4_2_ll_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_sim') 
        
class Instructions_4_2_ll_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_sm') 



class Instructions_4_2_lh_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_fm') 
        
class Instructions_4_2_lh_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_sim') 
        
class Instructions_4_2_lh_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_sm') 

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# Test questions for all treatments 

class Test_questions_hh_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_fm') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_h', 't5_points_other_h', 't6_refugee_participant', 't7_contribution_example_h', 't8_contribution_other_example_h', 't9_helping', 't10_helping_other', 't11_timing_fm']

class Test_questions_hh_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_sim') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_h', 't5_points_other_h', 't6_refugee_participant', 't7_contribution_example_h', 't8_contribution_other_example_h', 't9_helping', 't10_helping_other', 't11_timing_sim']

class Test_questions_hh_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_sm') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_h', 't5_points_other_h', 't6_refugee_participant', 't7_contribution_example_h', 't8_contribution_other_example_h', 't9_helping', 't10_helping_other', 't11_timing_sm']







class Test_questions_hl_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_fm') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_h', 't5_points_other_l', 't6_refugee_participant', 't7_contribution_example_h', 't8_contribution_other_example_l', 't9_helping', 't10_helping_other', 't11_timing_fm']

class Test_questions_hl_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_sim') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_h', 't5_points_other_l', 't6_refugee_participant', 't7_contribution_example_h', 't8_contribution_other_example_l', 't9_helping', 't10_helping_other', 't11_timing_sim']

class Test_questions_hl_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_sm') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_l', 't5_points_other_h', 't6_refugee_participant', 't7_contribution_example_l', 't8_contribution_other_example_h', 't9_helping', 't10_helping_other', 't11_timing_sm']





class Test_questions_ll_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_fm') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_l', 't5_points_other_l', 't6_refugee_participant', 't7_contribution_example_l', 't8_contribution_other_example_l', 't9_helping', 't10_helping_other', 't11_timing_fm']

class Test_questions_ll_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_sim') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_l', 't5_points_other_l', 't6_refugee_participant', 't7_contribution_example_l', 't8_contribution_other_example_l', 't9_helping', 't10_helping_other', 't11_timing_sim']

class Test_questions_ll_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_sm') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_l', 't5_points_other_l', 't6_refugee_participant', 't7_contribution_example_l', 't8_contribution_other_example_l', 't9_helping', 't10_helping_other', 't11_timing_sm']





class Test_questions_lh_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_fm') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_l', 't5_points_other_h', 't6_refugee_participant', 't7_contribution_example_l', 't8_contribution_other_example_h', 't9_helping', 't10_helping_other', 't11_timing_fm']

class Test_questions_lh_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_sim') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_l', 't5_points_other_h', 't6_refugee_participant', 't7_contribution_example_l', 't8_contribution_other_example_h', 't9_helping', 't10_helping_other', 't11_timing_sim']

class Test_questions_lh_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_sm') 

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_points_h', 't5_points_other_l', 't6_refugee_participant', 't7_contribution_example_h', 't8_contribution_other_example_l', 't9_helping', 't10_helping_other', 't11_timing_sm']




#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# Start task for all treatments 

class start_hh_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_fm')

class start_hh_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_sim')

class start_hh_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hh_sm')



class start_hl_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_fm')

class start_hl_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_sim')

class start_hl_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'hl_sm')



class start_ll_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_fm')

class start_ll_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_sim')

class start_ll_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'll_sm')




class start_lh_fm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_fm')

class start_lh_sim(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_sim')

class start_lh_sm(Page):

    def is_displayed(self):
        return (self.round_number == 1) & (self.player.treatment == 'lh_sm')

    # def vars_for_template(self):

        # return {
            # 'debug': settings.DEBUG,  
        # }


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# This part refers to the slider task and is similar to the previous app

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

#This page is not used in the experiment, as the payoff is fixed

class Effort(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        total_payoff = 0
        for p in self.player.in_all_rounds():
            if p.payoff_score != None: 
                total_payoff += p.payoff_score


        # round turns total_payoff into an integer
        self.participant.vars['task1_score'] = round(total_payoff) 
    
        self.player.effort_earning = round(total_payoff)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

page_sequence = [
        Start,
        Instructions_1,
        Instructions_2_hh_fm,
        Instructions_2_hh_sim,
        Instructions_2_hh_sm,
        Instructions_2_hl_fm,
        Instructions_2_hl_sim,
        Instructions_2_hl_sm,
        Instructions_2_ll_fm,
        Instructions_2_ll_sim,
        Instructions_2_ll_sm,
        Instructions_2_lh_fm,
        Instructions_2_lh_sim,
        Instructions_2_lh_sm,
        Instructions_3_hh_fm,
        Instructions_3_hh_sim,
        Instructions_3_hh_sm,
        Instructions_3_hl_fm,
        Instructions_3_hl_sim,
        Instructions_3_hl_sm,
        Instructions_3_ll_fm,
        Instructions_3_ll_sim,
        Instructions_3_ll_sm,
        Instructions_3_lh_fm,
        Instructions_3_lh_sim,
        Instructions_3_lh_sm,
        Instructions_4_2_hh_fm,
        Instructions_4_2_hh_sim,
        Instructions_4_2_hh_sm,
        Instructions_4_2_hl_fm,
        Instructions_4_2_hl_sim,
        Instructions_4_2_hl_sm,
        Instructions_4_2_ll_fm,
        Instructions_4_2_ll_sim,
        Instructions_4_2_ll_sm,
        Instructions_4_2_lh_fm,
        Instructions_4_2_lh_sim,
        Instructions_4_2_lh_sm,
        Test_questions_hh_fm,
        Test_questions_hh_sim,
        Test_questions_hh_sm,
        Test_questions_hl_fm,
        Test_questions_hl_sim,
        Test_questions_hl_sm,
        Test_questions_ll_fm,
        Test_questions_ll_sim,
        Test_questions_ll_sm,
        Test_questions_lh_fm,
        Test_questions_lh_sim,
        Test_questions_lh_sm,
        start_hh_fm,
        start_hh_sim,
        start_hh_sm,
        start_hl_fm,
        start_hl_sim,
        start_hl_sm,
        start_ll_fm,
        start_ll_sim,
        start_ll_sm,
        start_lh_fm,
        start_lh_sim,
        start_lh_sm,
        task,
        ]






        