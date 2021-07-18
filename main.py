from src.Agent import Policy_Iteration_Agent
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
agent = Policy_Iteration_Agent(epsilon, discount, Rows,Columns)
agent.Initilize_Policy()
agent.Print_Policy()
# agent.Print_Value_Functions()
agent.Policy_Improvement(1,steps)
# agent.Print_Value_Functions()
# agent.Print_Policy()
