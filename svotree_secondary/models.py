from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Constants(BaseConstants):
    name_in_url = 'svotree_secondary'
    players_per_group = None
    num_rounds = 1

    instructions_slider = 'svotree/SliderInstructions.html'
    instructions_9tdm = 'svotree/NineItemTDMInstructions.html'

    # I manually calculated the mid-points on the slider (there can be some slight discrepencies, as several very close positions on the slider display the same allocation)
    mid_point_item_7  = 61.8
    mid_point_item_8  = 45.7
    mid_point_item_9  = 37.1
    mid_point_item_10  = 75.0
    mid_point_item_11  = 49.1
    mid_point_item_12  = 83.8
    mid_point_item_13  = 50.7
    mid_point_item_14  =24.9
    mid_point_item_15= 15.9
    
    # I manually calculated the joint_max-points on the slider
    joint_max_item_7 = 100
    
    joint_max_item_9 = 0
    joint_max_item_10 = 100
    
    joint_max_item_12 = 100
    
    joint_max_item_14 = 0
    joint_max_item_15 = 0



#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Subsession(BaseSubsession):
    def creating_session(self):

        players = self.get_players()

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

    treatment = models.StringField()

    def set_payoff(self):
        """Calculate payoff, to be implemented later """
        self.payoff = 0

    slider7 = models.FloatField()
    slider8 = models.FloatField()
    slider9 = models.FloatField()
    slider10 = models.FloatField()
    slider11 = models.FloatField()
    slider12 = models.FloatField()
    slider13 = models.FloatField()
    slider14 = models.FloatField()
    slider15 = models.FloatField()


    avg_dist_equality = models.FloatField()
    avg_dist_joint_max = models.FloatField()
    inequality_aversion_score = models.FloatField()

    dist_equality_item_7 = models.FloatField()
    dist_equality_item_8 = models.FloatField()
    dist_equality_item_9 = models.FloatField()
    dist_equality_item_10 = models.FloatField()
    dist_equality_item_11 = models.FloatField()
    dist_equality_item_12 = models.FloatField()
    dist_equality_item_13 = models.FloatField()
    dist_equality_item_14 =  models.FloatField()
    dist_equality_item_15 =models.FloatField()

    dist_joint_max_item_7 = models.FloatField()
    dist_joint_max_item_9 = models.FloatField()
    dist_joint_max_item_10 = models.FloatField()
    dist_joint_max_item_12 = models.FloatField()
    dist_joint_max_item_14 =  models.FloatField()
    dist_joint_max_item_15 =models.FloatField()


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