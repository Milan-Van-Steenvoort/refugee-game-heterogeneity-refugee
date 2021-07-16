from . import models
from ._builtin import Page, WaitPage
from .functions import slider
from otree.api import Currency as c, currency_range
from .models import Constants

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class SliderSecondaryContinuous(Page):

    def app_after_this_page(self, upcoming_apps):
        if self.player.treatment == 'refugee_simseq':
            return upcoming_apps[-3]
        elif  self.player.treatment == 'refugee_seqsim':
            return upcoming_apps[-3]


    form_model = models.Player
    form_fields = ['slider7',
                   'slider8',
                   'slider9',
                   'slider10',
                   'slider11',
                   'slider12',
                   'slider13',
                   'slider14',
                   'slider15',
                ]

    def vars_for_template(self):
        return {'slider_items': [7, 8, 9, 10, 11, 12, 13, 14, 15]}

    def before_next_page(self):
        chosen_values = {
            'item7': self.player.slider7,
            'item8': self.player.slider8,
            'item9': self.player.slider9,
            'item10': self.player.slider10,
            'item11': self.player.slider11,
            'item12': self.player.slider12,
            'item13': self.player.slider13,
            'item14': self.player.slider14,
            'item15': self.player.slider15,
        }

        #distance on the slider betwen the chosen value and the equal split point
        self.player.dist_equality_item_7 = self.player.slider7 - Constants.mid_point_item_7
        self.player.dist_equality_item_8 = self.player.slider8 - Constants.mid_point_item_8
        self.player.dist_equality_item_9 = self.player.slider9 - Constants.mid_point_item_9
        self.player.dist_equality_item_10 = self.player.slider10 - Constants.mid_point_item_10
        self.player.dist_equality_item_11 = self.player.slider11 - Constants.mid_point_item_11
        self.player.dist_equality_item_12 = self.player.slider12 - Constants.mid_point_item_12
        self.player.dist_equality_item_13 = self.player.slider13 - Constants.mid_point_item_13
        self.player.dist_equality_item_14 = self.player.slider14 - Constants.mid_point_item_14
        self.player.dist_equality_item_15 = self.player.slider15 - Constants.mid_point_item_15
        

        #distance on the slider betwen the chosen value and the joint max point - joint max is always maximised in item8, item11 and item13. Therefore, the distance is always 0
        self.player.dist_joint_max_item_7 = self.player.slider7 - Constants.joint_max_item_7
        
        self.player.dist_joint_max_item_9 = self.player.slider9 - Constants.joint_max_item_9
        self.player.dist_joint_max_item_10 = self.player.slider10 - Constants.joint_max_item_10
        
        self.player.dist_joint_max_item_12 = self.player.slider12 - Constants.joint_max_item_12
        
        self.player.dist_joint_max_item_14 = self.player.slider14 - Constants.joint_max_item_14
        self.player.dist_joint_max_item_15 = self.player.slider15 - Constants.joint_max_item_15
        
        #calculates the inequality aversion score, between 0 (inequality averse) and 1 (joint max)
        self.player.avg_dist_equality = (abs(self.player.dist_equality_item_7 )+ abs(self.player.dist_equality_item_8) + abs(self.player.dist_equality_item_9) + abs(self.player.dist_equality_item_10) + abs(self.player.dist_equality_item_11) + abs(self.player.dist_equality_item_12) + abs(self.player.dist_equality_item_13) + abs(self.player.dist_equality_item_14) + abs(self.player.dist_equality_item_15))/9
        self.player.avg_dist_joint_max = (abs(self.player.dist_joint_max_item_7) + 0 + abs(self.player.dist_joint_max_item_9) + abs(self.player.dist_joint_max_item_10) + 0 + abs(self.player.dist_joint_max_item_12) + 0 + abs(self.player.dist_joint_max_item_14) + abs(self.player.dist_joint_max_item_15))/9
        
        self.player.inequality_aversion_score = abs(self.player.avg_dist_equality) / (abs(self.player.avg_dist_equality) + abs(self.player.avg_dist_joint_max))


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

page_sequence = [
    SliderSecondaryContinuous,
]



# NOTES
#----------


# This is a previous part, from when I tried to use a python function file
        #avg_dist_equality = slider.avg_dist_equality(chosen_values)
        #avg_dist_joint_max = slider.avg_dist_joint_max(chosen_values)
        #inequality_aversion_score = slider.inequality_aversion_score(avg_dist_equality, avg_dist_joint_max)
        #self.player.inequality_aversion_score = inequality_aversion_score
# In the end, I ended up defining all the variables at the player or constant level level (see models.py, line 64 - 107) and calculate the inequality aversion in pages.py (line 48-71)
# This is probably not the cleanest way to do so
# Moreover, it is not easy to be exactly inequality averse (score of 0), as there are several (but very close) places on the slider where they both have the same payoff. 