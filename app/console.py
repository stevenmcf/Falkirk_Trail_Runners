import pdb
from models.runner import Runner
from models.race import Race

import repositories.race_repository as race_repository
import repositories.runner_repository as runner_repository

runner_repository.delete_all()
# race_repository.delete_all()

runner_1 = Runner("Steven", "McFarlane")
runner_repository.save(runner_1)
runner_2 = Runner("Joanna", "McFarlane")
runner_repository.save(runner_2)
runner_3 = Runner("Vito", "Corleone")
runner_repository.save(runner_3)
runner_4 = Runner("Malcolm", "Tucker")
runner_repository.save(runner_4)
runner_5 = Runner("Jimmy", "Garroppolo")
runner_repository.save(runner_5)
runner_6 = Runner("Eddie", "Vedder")
runner_repository.save(runner_6)
runner_7 = Runner("Sabrina", "Pace")
runner_repository.save(runner_7)
runner_8 = Runner("Jasmine", "Paris")
runner_repository.save(runner_8)
runner_9 = Runner("Emilie", "Forsberg")
runner_repository.save(runner_9)

race_1 = Race("Dumyat Dash", 6.2, 457,)
race_repository.save(race_1)
race_2 = Race("Cockelroy", 3.4, 132)
# race_repository.save(race_2)
race_3 = Race("Ochil 2000s", "Stirling University", 33.0, 1200)
# race_repository.save(race_3)
race_4 = Race("EPIC Trail 10K", "Callendar House", 10, 421)
# race_repository.save(race_4)

pdb.set_trace()