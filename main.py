from src.Agent import Policy_Iteration_Agent, Value_Iteration_Agent
from src.Environment import Environment
Rows = 4
Columns = 4
GridWorld = Environment(Rows,Columns)
GridWorld.print_Grid_size()
GridWorld.reset()
GridWorld.print_current_location()

discount = 1
epsilon = 0.5
steps = 100
threshold = 0.5
'''Policy Iteration'''
# agent = Policy_Iteration_Agent(epsilon, discount, Rows,Columns)
# agent.Initialize_Policy()
# agent.Print_Value_Functions()
# agent.Print_Policy()
# agent.Policy_Improvement(threshold,steps)
# agent.Print_Value_Functions()
# agent.Print_Policy()


'''Value Iteration'''
agent = Value_Iteration_Agent(epsilon, discount, Rows,Columns)
agent.Value_Iteration(threshold, steps)
