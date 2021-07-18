import random
import numpy as np

class Agent(object):

    def __init__(self,epsilon):
        self.epsilon = epsilon
        self.actions_set = ["Up", "Down", "Left", "Right"]


    def act(self,state, train = True):
        if train:
            if random.random() <= self.epsilon:
                x = random.randint(0,3)
                action = self.actions_set[x]
            else:
                action = self.learned_act(state)
        else:  # in some cases, this can improve the performance.. remove it if poor performances
            action = self.learned_act(state)
        return action

    def learned_act(self,state):
        pass



class Policy_Iteration_Agent(Agent):
    def __init__(self,epsilon, discount ,Rows, Columns):
        self.Rows = Rows
        self.Columns = Columns
        super().__init__(epsilon)
        self.Value_Functions = np.zeros((Rows,Columns))
        self.Policy = []
        self.discount = discount

    def pi(self, state, action):
        if  len(self.Policy) == 0:
            return 1/len(self.actions_set) ##No policy in place all actions are equiprobable
        elif self.Policy[state[0]][state[1]] ==action:
            return 1
        else:
            return 0

    def move(self, old_state, action):
        if old_state[0] == 0 and action == "Up":
            return old_state
        elif old_state[0] == self.Rows-1  and action == "Down":
            return old_state
        elif old_state[1] == self.Columns-1  and action == "Right":
            return old_state
        elif old_state[1] == 0  and action == "Left":
            return old_state
        else:
            new_state = []
            new_state.append(old_state[0])
            new_state.append(old_state[1])
            if action == "Up":
                new_state[0] = old_state[0] - 1
            elif action == "Down":
                new_state[0] = old_state[0] + 1
            elif action == "Right":
                new_state[1] = old_state[1] + 1
            elif action == "Left":
                new_state[1] = old_state[1] - 1
            return new_state

    def Transitional_Probability(self, new_state, old_state, action): #p(s',r|s,a)
        state_after_action = self.move(old_state,action)
        if old_state == (0,0) or old_state == (self.Rows-1,self.Columns-1): #At the Goal
            return 0
        if state_after_action == new_state:
            print("ok")
            return 1
        return 0


    def Bellman_StateValueFunction(self, state):
        V = 0
        if state == [0,0] or state == [self.Rows-1,self.Columns-1]:
            return V
        # for action in self.actions_set:
        for row in range(self.Rows):
            for col in range(self.Columns):
                new_state = [row,col]
                V += (self.Transitional_Probability(new_state = new_state,old_state= state,action = self.Policy[state[0]][state[1]])*(-1 + self.discount*self.Value_Functions[row, col]))
        return V


    def Iterative_Policy_Evaluation(self, threshold, steps =10):
        # counter = 0
        while True:
            Difference = 0
            for row in range(self.Value_Functions.shape[0]):
                for col in range(self.Value_Functions.shape[1]):
                    V_old = self.Value_Functions[row,col]
                    V_new = self.Bellman_StateValueFunction([row,col])
                    self.Value_Functions[row, col] = V_new
                    self.Print_Value_Functions()
                    Difference = max(Difference,abs(V_old - V_new))
                    print("Difference:" + str(Difference))
            # counter +=1
            if (Difference <= threshold):# or counter > steps:
                break



    def Initilize_Policy(self):
        for row in range(self.Rows):
            row_lst = []
            for col in range(self.Columns):
                y = random.choice(self.actions_set)
                row_lst.append(y)
            self.Policy.append(row_lst)

    def MaxAction(self, state):
        best_action = None
        max_state_value = float('-inf')
        for action in self.actions_set:
            V = 0
            for row in range(self.Rows):
                for col in range(self.Columns):
                    new_state = [row,col]
                    V += (self.Transitional_Probability(new_state,state,action)*(-1 + self.discount*self.Value_Functions[row,col]))
            if V > max_state_value:
                max_state_value = V
                best_action = action

        return best_action

    def Policy_Improvement(self,threshold,steps):
        self.Initilize_Policy()
        policy_stable = False
        while policy_stable == False:
            self.Iterative_Policy_Evaluation(threshold, steps)
            self.Print_Value_Functions()
            policy_stable = True
            for row in range(self.Rows):
                for col in range(self.Columns):
                    old_action = self.Policy[row][col]
                    self.Policy[row][col] = self.MaxAction([row,col])
                    self.Print_Policy()
                    if old_action != self.Policy[row][col]:
                        policy_stable =False
            print(policy_stable)

    def learned_act(self,state):
        return self.Policy[state[0]][state[1]]


    def Print_Policy(self):
        print("Current Policy:")
        for row in range(self.Rows):
            print(self.Policy[row])
    def Print_Value_Functions(self):
        print("Current Value Functions:")
        print(self.Value_Functions)