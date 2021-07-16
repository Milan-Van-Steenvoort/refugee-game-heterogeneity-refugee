""""
Functions to evaluate input from the slider measure and calculate the resulting SVO values.
"""

import math

items = {
    'item7': {'self_left': 100, 'self_right': 70, 'other_left': 50, 'other_right': 100},
    'item8': {'self_left': 90, 'self_right': 100, 'other_left': 100, 'other_right': 90},
    'item9': {'self_left': 100, 'self_right': 50, 'other_left': 70, 'other_right': 100},
    'item10': {'self_left': 100, 'self_right': 90, 'other_left': 70, 'other_right': 100},
    'item11': {'self_left': 70, 'self_right': 100, 'other_left': 100, 'other_right': 70},
    'item12': {'self_left': 50, 'self_right': 100, 'other_left': 100, 'other_right': 90},
    'item13': {'self_left': 50, 'self_right': 100, 'other_left': 100, 'other_right': 50},
    'item14': {'self_left': 100, 'self_right': 70, 'other_left': 90, 'other_right': 100},
    'item15': {'self_left': 90, 'self_right': 100, 'other_left': 100, 'other_right': 50}, 
             }


def allocation(item, proportional_position_slider):
    """
    Calculate the allocation to self and other which corresponds to a particular position on
    the slider for a specific item.

    params: Chosen position on slider where 0 = left-most and 1 = right-most position possible
    returns: Allocation for self and other corresponding to this position, as dict
    effects: None
    """

    self_range = items[item]['self_right'] - items[item]['self_left']
    self_allocation_exact = items[item]['self_left'] + (self_range * proportional_position_slider)

    other_range = items[item]['other_right'] - items[item]['other_left']
    other_allocation_exact = items[item]['other_left'] + (other_range * proportional_position_slider)

    return {'self': round(self_allocation_exact), 'other': round(other_allocation_exact)}


def proportional_position(value, min_value, max_value):
    """
    Calculate the proportional representation of a position on a given scale.

    params: Value (position on the scale), minimum value (lowest possible value on the scale) and maximum value
    (highest possible value on the scale).
    returns: Proportional position (0 is leftmost, 1 is rightmost)
    effects: None
    """

    return (value - min_value) / (max_value - min_value)


#def proportional_position_discrete(value):
    """
    Calculate the proportional representation of a position on the discrete version of the slider.

    params: Value (position on the scale) chosen
    returns: This function calls proportional_position() and returns the result
    effects: None
    """

    #return proportional_position(value, 1, 9)


def proportional_position_continuous(value):
    """
    Calculate the proportional representation of a position on the continuous version of the slider.

    params: Value (position on the scale) chosen
    returns: This function calls proportional_position() and returns the result
    effects: None
    """

    return proportional_position(value, 0, 100)


#def mean_allocations_discrete(chosen_values):
    """
    Calculate the mean allocations to self and other based on all chosen values on a given group of slider items, assuming discrete choices.

    params: the values must be passed as a dictionary with the structure key = item+number, value = chosen value on
        that item
    returns: A dictionary of mean allocations to self and other
    effects: None
    """

    #total_allocation_self = 0
    #total_allocation_other = 0

    #for item, value in chosen_values.items():
        #chosen_allocation = allocation(item, proportional_position_discrete(value))

        #total_allocation_self += chosen_allocation['self']
        #total_allocation_other += chosen_allocation['other']

    #mean_allocation_self = total_allocation_self / len(chosen_values)
    #mean_allocation_other = total_allocation_other / len(chosen_values)

    #return {'self': mean_allocation_self, 'other': mean_allocation_other}


def mean_allocations_continuous(chosen_values):
    """
    Calculate the mean allocations to self and other based on all chosen values on a given group of slider items, assuming continuous scale.

    params: the values must be passed as a dictionary with the structure key = item+number, value = chosen value on
        that item
    returns: A dictionary of mean allocations to self and other
    effects: None
    """

    total_allocation_self = 0
    total_allocation_other = 0

    for item, value in chosen_values.items():
        chosen_allocation = allocation(item, proportional_position_continuous(value))

        total_allocation_self += chosen_allocation['self']
        total_allocation_other += chosen_allocation['other']


    mean_allocation_self = total_allocation_self / len(chosen_values)
    mean_allocation_other = total_allocation_other / len(chosen_values)

    return {'self': mean_allocation_self, 'other': mean_allocation_other}


def svo_angle(mean_allocation_self, mean_allocation_other):
    """
    Calculate a person's social value orientation angle (based on the slider measure).

    params: A mean allocation to self and a mean allocation to other, based on the six primary items of the SVO slider
    returns: The person's social value orientation angle
    effects: None
    """

    # With the default values of the slider measure, the origin is at 0,0 but the center of the circle is at 50,50
    # By subtracting 50 from both mean allocations we compute the angle from the center of the circle
    return math.degrees(math.atan2(mean_allocation_other - 50, mean_allocation_self - 50))


def svo_classification(angle):
    """
    Determine a person's social value orientation category based on slider measure angle. (Cutoffs as per Murphy,
    Ackermann & Handgraaf 2011)

    params: SVO angle in degrees
    returns: The person's social value orientation classification
    effects: None
    """

    if angle < -12.04:
        return "Competitive"
    elif angle < 22.45:
        return "Individualistic"
    elif angle < 57.15:
        return "Prosocial"
    else:
        return "Altruistic"






# Attempt to have it work with functions
#----------------------------------------

# DISCLAIMER: DID NOT WORK 


#mid_points = {
#    'item7': {'mid_point' : 61.8},    
#    'item8':{'mid_point' : 45.7},
#    'item9':{'mid_point' : 37.1},
#    'item10':{'mid_point' : 75.0},
#    'item11':{'mid_point' : 49.1},
#    'item12':{'mid_point' : 83.8},
#    'item13':{'mid_point' : 50.7},
#    'item14':{'mid_point' : 24.9},
#    'item15':{'mid_point' : 15.9},
#             }
#
#joint_max = {
#    'item7': {'joint_max' : 100},    
#    'item8':{'joint_max' : 0 },
#    'item9':{'joint_max' : 0},
#    'item10':{'joint_max' : 100},
#    'item11':{'joint_max' : 0 },
#    'item12':{'joint_max' : 100},
#    'item13':{'joint_max' : 0 },
#    'item14':{'joint_max' : 0},
#    'item15':{'joint_max' : 0},
#             }
#
#
#def dist_equality(item, proportional_position_slider):
#
#    return proportional_position_slider - mid_points[item]['mid_point']
#    
#def dist_joint_max(item, proportional_position_slider):
#    
#    return proportional_position_slider - joint_max[item]['joint_max']
#
#def avg_dist_equality(dist_equality):
#
#    return sum(dist_equality) / 9 
#
#def avg_dist_joint_max(dist_joint_max):
#    
#    return sum(dist_joint_max) / 9
#
#def inequality_aversion_score(avg_dist_equality, avg_distance_joint_max):
#
#    return avg_dist_equality / (avg_dist_equality + avg_distance_joint_max)








# Basically, this is what I want to do 
#---------------------------------------

    # I manually calculated the mid-points on the slider
   # mid_point_item_7 = 61.8
   # mid_point_item_8 = 45.7
   # mid_point_item_9 = 37.1
   # mid_point_item_10 = 75.0
   # mid_point_item_11 = 49.1
   # mid_point_item_12 = 83.8
   # mid_point_item_13 = 50.7
   # mid_point_item_14 = 24.9
   # mid_point_item_15 = 15.9
   # 
   # # I manually calculated the joint_max-points on the slider
   # joint_max_item_7 = 100
   # 
   # joint_max_item_9 = 0
   # joint_max_item_10 = 100
   # 
   # joint_max_item_12 = 100
   # 
   # joint_max_item_14 = 0
   # joint_max_item_15 = 0 
   #
   # dist_equality_item_7 = slider7 - mid_point_item_7
   # dist_equality_item_8 = slider8 - mid_point_item_8
   # dist_equality_item_9 = slider9 - mid_point_item_9
   # dist_equality_item_10 = slider10 - mid_point_item_10
   # dist_equality_item_11 = slider11 - mid_point_item_11
   # dist_equality_item_12 = slider12 - mid_point_item_12
   # dist_equality_item_13 = slider13 - mid_point_item_13
   # dist_equality_item_14 = slider14 - mid_point_item_14
   # dist_equality_item_15 = slider15 - mid_point_item_15
   # 
   # dist_joint_max_item_7 = slider7 - joint_max_item_7
   # 
   # dist_joint_max_item_9 = slider9 - joint_max_item_9
   # dist_joint_max_item_10 = slider10 - joint_max_item_10
   # 
   # dist_joint_max_item_12 = slider12 - joint_max_item_12
   # 
   # dist_joint_max_item_14 = slider14 - joint_max_item_14
   # dist_joint_max_item_15 = slider15 - joint_max_item_15
   # 
   # avg_dist_equality = (dist_equality_item_7 + dist_equality_item_8 + dist_equality_item_9 + dist_equality_item_10 + dist_equality_item_11 + dist_equality_item_12 + dist_equality_item_13 + dist_equality_item_14 + dist_equality_item_15)/9
   # avg_distance_joint_max = (dist_joint_max_item_7 + dist_joint_max_item_9 + dist_joint_max_item_10 + dist_joint_max_item_12 + dist_joint_max_item_14 + dist_joint_max_item_15)/6
   # 
   # inequality_aversion_score = avg_dist_equality / (avg_dist_equality + avg_distance_joint_max)