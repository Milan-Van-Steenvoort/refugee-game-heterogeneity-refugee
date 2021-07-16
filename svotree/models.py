from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Constants(BaseConstants):
    name_in_url = 'svotree'
    players_per_group = None
    num_rounds = 1

    instructions_slider = 'svotree/SliderInstructions.html'
    instructions_9tdm = 'svotree/NineItemTDMInstructions.html'


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Subsession(BaseSubsession):
    def creating_session(self):

        #treatment assignement. This variables is imported in every app.
        import itertools
        if self.round_number == 1:
            treatment = itertools.cycle(['refugee_simseq', 'refugee_seqsim'])
            for p in self.get_players():
                p.treatment = next(treatment)
            
        #the treatment variable is stored in the participant var which allow transfer of variables to other apps and other rounds within apps (see oTree doc)

        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['treatment_assigned'] = p.treatment
        
        #in the other rounds the treatment variable is imported out of the participant var
                
        if self.round_number > 1:
            for p in self.get_players():
                p.treatment = p.participant.vars['treatment_assigned']

        if self.round_number == 5:
            for p in self.get_players():
                p.participant_vars = str(p.participant.vars)  

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Group(BaseGroup):
    pass

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Player(BasePlayer):

    treatment = models.StringField()

    def set_payoff(self):
        """Calculate payoff, to be implemented later """
        self.payoff = 0

    slider1 = models.FloatField()
    slider2 = models.FloatField()
    slider3 = models.FloatField()
    slider4 = models.FloatField()
    slider5 = models.FloatField()
    slider6 = models.FloatField()
    slider_angle = models.FloatField()
    slider_classification = models.CharField()


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# NOTES
#---------

# I deleted the models and pages related to the triple dominance measure 
# I define the treatments in this app, for the rest of the experiment - see subsession
# I changed the slider_angle from DecimalField to a FloatField
# I have to add the nine secondary sliders:
    # add new models sliders 7-15
    # add a new page 
    # update javascripts: probably I will need to adapt slider (to define new boundaries), slider_primary (mostly about confirm buttons) and slider_primary_continuous (this is were the sliders are defined)
    # update instructions