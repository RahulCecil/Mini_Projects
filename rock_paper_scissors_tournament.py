import numpy as np
import matplotlib.pyplot as plt

#def contestants(n_con, n_days):
#       return n_con * (1/2)**n_days

### Initial Parameters ###
n_con = 50
n_days = 30
n_sims = 100

### Generate outcomes for n games ###
flags = 0
for i in range(n_sims):
        cons = list(range(n_con))
        cons_tracker = []
        
        for i in range(n_days):
                grouped = [cons[i:i+2] for i in range(0, len(cons), 2)]
                #print(grouped)

                game_outcome = np.random.randint(2, size = (len(grouped)) )
                #print(game_outcome)

                for i in range(len(grouped)):
                        if game_outcome[i] == 0 and len(grouped[i]) == 2:
                                del grouped[i][np.random.randint(2)]

                cons = [item for sublist in grouped for item in sublist]
                #print(cons)
                
                cons_tracker.append(len(cons))
        
        
        plt.plot(cons_tracker)
        
        if len(cons) > 1:
                flags+=1

plt.title(f"\nTournament of {n_con} Failed {flags} Times Out Of {n_sims}.")
plt.show()
