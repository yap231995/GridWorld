import random
class Environment(object):
    def __init__(self, Rows, Columns):
        self.Game_over = True
        self.Rows = Rows
        self.Columns = Columns
        #Initialise the starting position for the agent.
        self.Rewards = 0
        self.agent_current_position = [0,0] #Index the Coordinates of when it is.


    def print_current_location(self):
        print(self.agent_current_position)
    def print_Grid_size(self):
        print("(Rows, Column):" + str((self.Rows,self.Columns)))


    def reset(self):
        self.Game_over =False
        while (self.agent_current_position[0] == 0 and self.agent_current_position[1] == 0) or (self.agent_current_position[0] == self.Rows-1 and self.agent_current_position[1] == self.Columns-1):
            pos_Rows = random.randint(0, self.Rows-1)
            pos_Columns = random.randint(0,self.Columns-1)
            self.agent_current_position[0] = pos_Rows
            self.agent_current_position[1] = pos_Columns

    def env_respond(self,agent_action):
        '''
        This function updates the new state, rewards, and decides if the games ends.

        :param agent_action: Action of where the agent decide to move "Up", "Down", "Left", "Right"
        :return: Game_over: False if the game is not over, True if the agent reaches the coordinate (0,0) or (self.Rows-1,self.Column-1)
        '''
        #It has all transition probability =1 for all state that is above, below, left and right of the current state.
        #With exception that, if the action move out of the grid, it will remain where it is.
        #The rest of the of transition probability = 0.
        if agent_action == "Up":
            if self.agent_current_position[0] != 0:
                self.agent_current_position[0] -= 1
        elif agent_action == "Down":
            if self.agent_current_position[0] != self.Rows -1:
                self.agent_current_position[0] += 1
        elif agent_action == "Left":
            if self.agent_current_position[1] != 0:
                self.agent_current_position[1] -= 1
        elif agent_action == "Right":
            if self.agent_current_position[1] != self.Columns -1:
                self.agent_current_position[1] += 1

        self.Rewards -= 1

        if (self.agent_current_position[0] == 0 and self.agent_current_position[1] == 0) or \
            (self.agent_current_position[0] == self.Rows-1 and self.agent_current_position[1] == self.Columns-1):
            self.Game_over = True
            return self.Game_over
        return self.Game_over
