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


doc = """
Your app description
"""
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Constants(BaseConstants):
    name_in_url = 'refugee_beliefs_2'
    players_per_group = None
    tasks_sim = ['ref_sim_hh', 'ref_sim_hl_lh', 'ref_sim_ll']
    num_rounds_sim = len(tasks_sim)
    tasks_seq = ['ref_seq_hh', 'ref_seq_hl', 'ref_seq_lh', 'ref_seq_ll']
    num_rounds_seq = len(tasks_seq)
    num_rounds = 4
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

class Subsession(BaseSubsession):

  
    def creating_session(subsession):
        import random
        if subsession.round_number == 1:
          for p in subsession.get_players():
            round_numbers_sim = list(range(1, Constants.num_rounds_sim+1))
            random.shuffle(round_numbers_sim)
            print(round_numbers_sim)
            p.participant.vars['task_rounds_sim'] = dict(zip(Constants.tasks_sim, round_numbers_sim))
            print(p.participant.vars['task_rounds_sim'])

        import random
        if subsession.round_number == 1:
          for p in subsession.get_players():
            round_numbers_seq = list(range(1, Constants.num_rounds_seq+1))
            random.shuffle(round_numbers_seq)
            print(round_numbers_seq)
            p.participant.vars['task_rounds_seq'] = dict(zip(Constants.tasks_seq, round_numbers_seq))
            print(p.participant.vars['task_rounds_seq'])

          for p in subsession.get_players():
            p.treatment = p.participant.vars['treatment_assigned']

        #in the other rounds the treatment variable is imported out of the participant var
                
        if subsession.round_number > 1:
            for p in subsession.get_players():
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
 
 # (1) Variables related to beliefs
#---------------------------------------------------------------  

    ref_belief_sim_hh_A = models.IntegerField()
    ref_belief_sim_hh_B = models.IntegerField()
    ref_belief_sim_hl_A = models.IntegerField()
    ref_belief_sim_hl_B = models.IntegerField()
    ref_belief_sim_ll_A = models.IntegerField()
    ref_belief_sim_ll_B = models.IntegerField()

    ref_belief_seq_hh_A = models.IntegerField()
    ref_belief_seq_hh_B_1 = models.IntegerField()
    ref_belief_seq_hh_B_2 = models.IntegerField()
    ref_belief_seq_hh_B_3 = models.IntegerField()
    ref_belief_seq_hh_B_4 = models.IntegerField()

    ref_belief_seq_hl_A = models.IntegerField()
    ref_belief_seq_hl_B_1 = models.IntegerField()
    ref_belief_seq_hl_B_2 = models.IntegerField()
    ref_belief_seq_hl_B_3 = models.IntegerField()
    ref_belief_seq_hl_B_4 = models.IntegerField()

    ref_belief_seq_lh_A = models.IntegerField()
    ref_belief_seq_lh_B_1 = models.IntegerField()
    ref_belief_seq_lh_B_2 = models.IntegerField()
    ref_belief_seq_lh_B_3 = models.IntegerField()
    ref_belief_seq_lh_B_4 = models.IntegerField()

    ref_belief_seq_ll_A = models.IntegerField()
    ref_belief_seq_ll_B_1 = models.IntegerField()
    ref_belief_seq_ll_B_2 = models.IntegerField()
    ref_belief_seq_ll_B_3 = models.IntegerField()
    ref_belief_seq_ll_B_4 = models.IntegerField()


# (2) Variables related to test questions
#---------------------------------------------------------------  

    # Amount of incorrect attempts for all the questions
    incorrect_attempts1 = models.IntegerField(initial=0)  
    incorrect_attempts2 = models.IntegerField(initial=0)      
    incorrect_attempts3 = models.IntegerField(initial=0)  
    incorrect_attempts4 = models.IntegerField(initial=0)
    incorrect_attempts5 = models.IntegerField(initial=0)  
    incorrect_attempts6 = models.IntegerField(initial=0)
    incorrect_attempts7 = models.IntegerField(initial=0)

    total_incorrect_answers = models.IntegerField(initial=0)   

            # QUESTIONS

#number of groups of citizens _all treatments     
    t1_number_of_citizens_groups = models.IntegerField(
      choices=[
        [1, '1'],
        [2, '2'],
        [3, '3'],
      ], label='How many groups of citizens are there in the decision task?',
        widget=widgets.RadioSelect)

#number of  citizens _all treatments     
    t2_number_of_citizens = models.IntegerField(
      choices=[
        [2, '2'],
        [3, '3'],
        [4, '4'],
      ], label='How many citizens are there per group?',
        widget=widgets.RadioSelect)
        
#numbers of refugees _all treatemnts
    t3_number_of_refugees = models.IntegerField(
      choices=[
        [1, '1'],
        [2, '2'],
        [3, '3'],
      ], label='How many refugees are there in the decision task?',
        widget=widgets.RadioSelect)
      

# helping
    t4_helping = models.IntegerField(
      choices=[
        [1, 'Between 0 percent and 20 percent'],
        [2, 'Between 0 percent and 30 percent'],
        [3, 'Between 0 percent and 40 percent'],
      ], label='What percentage of their common account can citizens from group A share with the refugee?',
        widget=widgets.RadioSelect)

# helping other
    t5_helping_other = models.IntegerField(
      choices=[
        [1, 'Between 0 percent and 20 percent'],
        [2, 'Between 0 percent and 30 percent'],
        [3, 'Between 0 percent and 40 percent'],
      ], label='What percentage of their common account can citizens from group B share with the refugee?',
        widget=widgets.RadioSelect)

# timing of the decision sim
    t6_timing_sim = models.IntegerField(
      choices=[
        [1, 'Before citizens from group B make their decisions'],
        [2, 'After citizens from group B make their decisions'],
        [3, 'At the same time that citizens from group B make their decisions'],
      ], label='I can think of participants in group A as making their decisions',
        widget=widgets.RadioSelect)

# timing of the decision seq
    t6_timing_seq = models.IntegerField(
      choices=[
        [1, 'Before citizens from group B make their decisions'],
        [2, 'After citizens from group B make their decisions'],
        [3, 'At the same time that citizens from group B make their decisions'],
      ], label='I can think of participants in group A as making their decisions',
        widget=widgets.RadioSelect)


                    # ANSWERS


# Questions 1-5 are similar no matter timing

    def t1_number_of_citizens_groups_error_message(self, value):
      print('value is', value)
      if value != 2:
         self.incorrect_attempts1 += 1
         self.total_incorrect_answers +=1
         return 'Wrong answer. Please try again.'
         
    def t2_number_of_citizens_error_message(self, value):
      print('value is', value)
      if value != 4:
         self.incorrect_attempts2 += 1
         self.total_incorrect_answers +=1
         return 'Wrong answer. Please try again.'

    def t3_number_of_refugees_error_message(self, value):
      print('value is', value)
      if value != 1:
         self.incorrect_attempts3 += 1
         self.total_incorrect_answers +=1
         return 'Wrong answer. Please try again.'
         
    def t4_helping_error_message(self, value):
      print('value is', value)
      if value != 1:
         self.incorrect_attempts4+= 1
         self.total_incorrect_answers +=1
         return 'Wrong answer. Please try again.'

    def t5_helping_other_error_message(self, value):
      print('value is', value)
      if value != 1:
         self.incorrect_attempts5+= 1
         self.total_incorrect_answers +=1
         return 'Wrong answer. Please try again.'


# Question 6 differs between seq and sim treatment groups

    def t6_timing_sim_error_message(self, value):
      print('value is', value)
      if value != 3:
         self.incorrect_attempts6 += 1
         self.total_incorrect_answers +=1
         return 'Wrong answer. Please try again.'
         
         
    def t6_timing_seq_error_message(self, value):
      print('value is', value)
      if value != 1:
         self.incorrect_attempts7 += 1
         self.total_incorrect_answers +=1
         return 'Wrong answer. Please try again.'
