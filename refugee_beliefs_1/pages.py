from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
# SIMULTANEOUS BLOCK 

class Instructions_2_ref_sim(Page):
    
    def is_displayed(self):
        return (self.player.treatment == 'refugee_simseq') & (self.round_number == 1)

class Instructions_3_ref_sim(Page):
    
    def is_displayed(self):
        return (self.player.treatment == 'refugee_simseq') & (self.round_number == 1)

class Instructions_4_ref_sim(Page):
    
    def is_displayed(self):
        return (self.player.treatment == 'refugee_simseq') & (self.round_number == 1)

class test_questions_ref_sim(Page):

    def is_displayed(self):
        return (self.player.treatment == 'refugee_simseq') & (self.round_number == 1)

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_helping', 't5_helping_other', 't6_timing_sim']

class ref_sim_hh(Page):

    def is_displayed(self):
        return (self.player.treatment == 'refugee_simseq') & (self.round_number == self.player.participant.vars['task_rounds_sim']['ref_sim_hh'])

    form_model = 'player'
    form_fields = ['ref_belief_sim_hh_A', 'ref_belief_sim_hh_B']

class ref_sim_hl_lh(Page):

    def is_displayed(self):
        return (self.player.treatment == 'refugee_simseq') & (self.round_number == self.player.participant.vars['task_rounds_sim']['ref_sim_hl_lh'])

    form_model = 'player'
    form_fields = ['ref_belief_sim_hl_A', 'ref_belief_sim_hl_B']

class ref_sim_ll(Page):

    def is_displayed(self):
        return (self.player.treatment == 'refugee_simseq') & (self.round_number == self.player.participant.vars['task_rounds_sim']['ref_sim_ll'])

    form_model = 'player'
    form_fields = ['ref_belief_sim_ll_A', 'ref_belief_sim_ll_B']

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
# SEQUENTIAL BLOCK 

class Instructions_2_ref_seq(Page):
    
    def is_displayed(self):
        return (self.player.treatment == 'refugee_seqsim') & (self.round_number == 1)

class Instructions_3_ref_seq(Page):
    
    def is_displayed(self):
        return (self.player.treatment == 'refugee_seqsim') & (self.round_number == 1)

class Instructions_4_ref_seq(Page):
    
    def is_displayed(self):
        return (self.player.treatment == 'refugee_seqsim') & (self.round_number == 1)

class test_questions_ref_seq(Page):

    def is_displayed(self):
        return (self.player.treatment == 'refugee_seqsim') & (self.round_number == 1)

    form_model = 'player'
    form_fields = ['t1_number_of_citizens_groups', 't2_number_of_citizens', 't3_number_of_refugees', 't4_helping', 't5_helping_other', 't6_timing_seq']

class ref_seq_hh(Page):

    def is_displayed(self):
        return (self.player.treatment == 'refugee_seqsim') & (self.round_number == self.player.participant.vars['task_rounds_seq']['ref_seq_hh'])

    form_model = 'player'
    form_fields = ['ref_belief_seq_hh_A', 'ref_belief_seq_hh_B_1', 'ref_belief_seq_hh_B_2', 'ref_belief_seq_hh_B_3', 'ref_belief_seq_hh_B_4']

class ref_seq_hl(Page):

    def is_displayed(self):
        return (self.player.treatment == 'refugee_seqsim') & (self.round_number == self.player.participant.vars['task_rounds_seq']['ref_seq_hl'])

    form_model = 'player'
    form_fields = ['ref_belief_seq_hl_A', 'ref_belief_seq_hl_B_1', 'ref_belief_seq_hl_B_2', 'ref_belief_seq_hl_B_3', 'ref_belief_seq_hl_B_4']

class ref_seq_lh(Page):

    def is_displayed(self):
        return (self.player.treatment == 'refugee_seqsim') & (self.round_number == self.player.participant.vars['task_rounds_seq']['ref_seq_lh'])

    form_model = 'player'
    form_fields = ['ref_belief_seq_lh_A', 'ref_belief_seq_lh_B_1', 'ref_belief_seq_lh_B_2', 'ref_belief_seq_lh_B_3', 'ref_belief_seq_lh_B_4']

class ref_seq_ll(Page):

    def is_displayed(self):
        return (self.player.treatment == 'refugee_seqsim') & (self.round_number == self.player.participant.vars['task_rounds_seq']['ref_seq_ll'])
        
    form_model = 'player'
    form_fields = ['ref_belief_seq_ll_A', 'ref_belief_seq_ll_B_1', 'ref_belief_seq_ll_B_2', 'ref_belief_seq_ll_B_3', 'ref_belief_seq_ll_B_4']

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

page_sequence = [
        Instructions_2_ref_sim,
        Instructions_3_ref_sim,
        Instructions_4_ref_sim,
        test_questions_ref_sim,
        ref_sim_hh,
        ref_sim_hl_lh,
        ref_sim_ll,
        Instructions_2_ref_seq,
        Instructions_3_ref_seq,
        Instructions_4_ref_seq,
        test_questions_ref_seq,
        ref_seq_hh,
        ref_seq_hl,
        ref_seq_lh,
        ref_seq_ll,
        ]
