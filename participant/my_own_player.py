import random
from . import participant as part


class my_own_player(part.Participant):
    def __init__(self):
        super().__init__('name of your team', 'team num')
        # you can change everything in this code file!!
        # also, you can define your own variables here or in the overriding method
        # Any modifications are possible if you follows the rules of Squid Game


    # ====================================================================== for initializing your player every round
    def initialize_player(self, string):
        # you can override this method in this sub-class
        # this method must contain 'self.initialize_params()' which is for initializing some essential variables
        # you can initialize what you define
        self.initialize_params()
        self.stepping_log = []
    # ====================================================================== for initializing your player every round


    # ================================================================================= for marble game
    def bet_marbles_strategy(self, playground_marbles):
        # you can override this method in this sub-class
        # you can refer to an object of 'marbles', named as 'playground_marbles'
        # the return should be the number of marbles bet (> 0)!
        my_current_marbles = playground_marbles.get_num_of_my_marbles(self)
        return 6

    def declare_statement_strategy(self, playground_marbles):
        # you can override this method in this sub-class
        # you can refer to an object of 'marbles', named as 'playground_marbles'
        # the return should be True or False!
        mih = playground_marbles._marbles_in_hand
        answer = bool(mih % 2)
        return self.set_statement(answer)
    # ================================================================================= for marble game


    # ================================================================================= for glass_stepping_stones game
    def step_toward_goal_strategy(self, playground_glasses):
        # you can override this method in this sub-class
        # you can refer to an object of 'glass_stepping_stones', named as 'playground_glasses'
        # the return should be 0 or 1 (int)!
        position = self.position
        if not self.previous_step_result:
            return random.randint(0, 1)
        if self.previous_step_result[2] is False:
            self.stepping_log.append(1 - self.previous_step_result[1])
        if position < len(self.stepping_log):
            return self.stepping_log[position]
        if self.previous_step_result[0] == len(self.stepping_log):
            self.stepping_log.append(self.previous_step_result[1])
            return random.randint(0, 1)
        playground_glasses._players_steps = [0] * 20
        return random.randint(0, 1)
    # ================================================================================= for glass_stepping_stones game


    # ================================================================================= for tug_of_war game
    def gathering_members(self):
        # you can override this method in this sub-class
        # this method gathers your members for the tug of war game
        # you only can change the configuration of the numbers of person types
        # there are 4 types of persons
        # type1 corresponds a ordinary person who has standard stats for the game
        # type2 corresponds a person with great height
        # type3 corresponds a person with a lot of weight
        # type4 corresponds a person with strong power
        # the return should be a tuple with size of 4, and the sum of the elements should be 10
        # only for computer, it is allowed to set 12 members
        return (10, 0, 0, 0)

    def act_tugging_strategy(self, playground_tug_of_war):
        # you can override this method in this sub-class
        # you can refer to an object of 'tug_of_war', named as 'playground_tug_of_war'
        # the return should be a float value in [0, 100]!
        # note that the float represents a stamina-consuming rate for tugging
        if playground_tug_of_war.player_condition[self.name] == True:
            if playground_tug_of_war.player_condition['Computer'] == True:
                if playground_tug_of_war.player_expression['Computer'] in ['best', 'well']:
                    playground_tug_of_war.mat_type = 'steel'
                    return 0


                else:
                    if playground_tug_of_war.player_expression[self.name] in ['best', 'well']:
                        playground_tug_of_war.mat_type = 'steel'
                        return random.randint(15, 20)
                    else:
                        return 4

            else:
                playground_tug_of_war.mat_type = 'glass'
                if playground_tug_of_war.player_expression[self.name] in ['best', 'well', 'good']:
                    return 20
                else:
                    return 4

        else:

            playground_tug_of_war.mat_type = 'asphalt'
            return 5
    # ================================================================================= for tug_of_war game