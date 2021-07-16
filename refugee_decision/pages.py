from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Start(Page):
   pass
    #def vars_for_template(self):
        #self.player.instruction_form = self.participant.vars['form']

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
 
class Decision_hh_sim(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return (self.player.treatment == 'hh_sim') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_hh_fm(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return (self.player.treatment == 'hh_fm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_hh_sm_1(Page):
    form_model = 'player'
    form_fields = ['decision_sm_1']

    def is_displayed(self):
        return (self.player.treatment == 'hh_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_hh_sm_2(Page):
    form_model = 'player'
    form_fields = ['decision_sm_2']

    def is_displayed(self):
        return (self.player.treatment == 'hh_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_hh_sm_3(Page):
    form_model = 'player'
    form_fields = ['decision_sm_3']

    def is_displayed(self):
        return (self.player.treatment == 'hh_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_hh_sm_4(Page):
    form_model = 'player'
    form_fields = ['decision_sm_4']

    def is_displayed(self):
        return (self.player.treatment == 'hh_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_hl_fm(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return (self.player.treatment == 'hl_fm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_hl_sim(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return (self.player.treatment == 'hl_sim') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_hl_sm_1(Page):
    form_model = 'player'
    form_fields = ['decision_sm_1']

    def is_displayed(self):
        return (self.player.treatment == 'hl_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_hl_sm_2(Page):
    form_model = 'player'
    form_fields = ['decision_sm_2']

    def is_displayed(self):
        return (self.player.treatment == 'hl_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_hl_sm_3(Page):
    form_model = 'player'
    form_fields = ['decision_sm_3']

    def is_displayed(self):
        return (self.player.treatment == 'hl_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_hl_sm_4(Page):
    form_model = 'player'
    form_fields = ['decision_sm_4']

    def is_displayed(self):
        return (self.player.treatment == 'hl_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_ll_sim(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return (self.player.treatment == 'll_sim') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)
 

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_ll_fm(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return (self.player.treatment == 'll_fm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_ll_sm_1(Page):
    form_model = 'player'
    form_fields = ['decision_sm_1']

    def is_displayed(self):
        return (self.player.treatment == 'll_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_ll_sm_2(Page):
    form_model = 'player'
    form_fields = ['decision_sm_2']

    def is_displayed(self):
        return (self.player.treatment == 'll_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_ll_sm_3(Page):
    form_model = 'player'
    form_fields = ['decision_sm_3']

    def is_displayed(self):
        return (self.player.treatment == 'll_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_ll_sm_4(Page):
    form_model = 'player'
    form_fields = ['decision_sm_4']

    def is_displayed(self):
        return (self.player.treatment == 'll_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)



#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_lh_fm(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return (self.player.treatment == 'lh_fm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_lh_sim(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return (self.player.treatment == 'lh_sim') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Decision_lh_sm_1(Page):
    form_model = 'player'
    form_fields = ['decision_sm_1']

    def is_displayed(self):
        return (self.player.treatment == 'lh_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)

class Decision_lh_sm_2(Page):
    form_model = 'player'
    form_fields = ['decision_sm_2']

    def is_displayed(self):
        return (self.player.treatment == 'lh_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)


class Decision_lh_sm_3(Page):
    form_model = 'player'
    form_fields = ['decision_sm_3']

    def is_displayed(self):
        return (self.player.treatment == 'lh_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)


class Decision_lh_sm_4(Page):
    form_model = 'player'
    form_fields = ['decision_sm_4']

    def is_displayed(self):
        return (self.player.treatment == 'lh_sm') 

    def vars_for_template(self):
        #self.player.effort_earning = self.participant.vars['task1_score']
        
        if self.player.treatment == 'hh_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hh_sm':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_sim':
            self.player.effort_earning = 75
        if self.player.treatment == 'hl_fm':
            self.player.effort_earning = 75
        if self.player.treatment == 'lh_sm':
            self.player.effort_earning = 75

        if self.player.treatment == 'll_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'll_sm':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_sim':
            self.player.effort_earning = 25
        if self.player.treatment == 'lh_fm':
            self.player.effort_earning = 25
        if self.player.treatment == 'hl_sm':
            self.player.effort_earning = 25
       
        self.player.contribution = round((0.40 * self.player.effort_earning), 2)
        self.player.private_earning = round((0.6 * self.player.effort_earning), 2)


######################
#Not needed    
######################
class Results(Page):

    def before_next_page(self):
      self.player.participant_vars_dump = str(self.participant.vars)



#Page sequence
page_sequence = [Start, Decision_hh_sim, Decision_hh_fm, Decision_hh_sm_1, Decision_hh_sm_2, Decision_hh_sm_3, Decision_hh_sm_4, Decision_ll_sim, Decision_ll_fm, Decision_ll_sm_1, Decision_ll_sm_2, Decision_ll_sm_3, Decision_ll_sm_4, Decision_hl_sim, Decision_hl_fm, Decision_hl_sm_1, Decision_hl_sm_2, Decision_hl_sm_3, Decision_hl_sm_4, Decision_lh_sim, Decision_lh_fm, Decision_lh_sm_1, Decision_lh_sm_2, Decision_lh_sm_3, Decision_lh_sm_4,
]
