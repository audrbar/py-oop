class FitnessTracker:
    def __init__(self, user_name: str, steps: int):
        self.user_name = user_name
        self.steps = steps

    def add_steps(self, new_steps):
        self.steps += new_steps
        self._check_goal()

    def reset_steps(self):
        self.steps = 0

    def _check_goal(self):
        if self.steps >= 10000:
            print(f"{self.user_name}, you have reached your goal: {self.steps}")

    def get_steps(self):
        print(f"{self.user_name}, you have {self.steps} steps.")


user_1 = FitnessTracker('Tim', 100)
user_1.get_steps()
user_1.add_steps(100)
user_1.get_steps()
user_1.reset_steps()
user_1.get_steps()
user_1.add_steps(10001)
