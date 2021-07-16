from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Start(Page):
   pass
   # def vars_for_template(self):
        #self.player.instruction_form = self.participant.vars['form']

######################
#Belief measures male version        
######################

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

#class Beliefs_hoch(Page):

    #def is_displayed(self):
       # return (self.player.treatment == 'high') & (self.player.instruction_form == 1)
        
    #form_model = 'player'
    #form_fields = ['belief_hoch_hoch', 'belief_hoch_gering']

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

#class Beliefs_gering(Page):
    
    #def is_displayed(self):
       # return (self.player.treatment == 'low') & (self.player.instruction_form == 1)
    
   # form_model = 'player'
   # form_fields = ['belief_gering_hoch', 'belief_gering_gering']

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

    
#class Beliefs(Page):

  #  def is_displayed(self):
      #  return (self.player.treatment == 'equal') & (self.player.instruction_form == 1)
        
   # form_model = 'player'
   # form_fields = ['belief']

#class Check(Page):

   # def is_displayed(self):
        #return self.player.instruction_form == 1

   # form_model = 'player'
    #form_fields = ['check1',
                #   'check2'
                 #  ]

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------


class LR1(Page):
    form_model = 'player'
    form_fields = ['left_right']

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
    
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender']

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Payment(Page):
    pass

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

page_sequence = [Start, LR1, Demographics]