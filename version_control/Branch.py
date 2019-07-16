from version_control.State import State

class Branch():

    def __init__(self):
        self.patches = []
        self.states = [State(dict())] # state 0 is the empty state

    def add_patch(self, patch):
        # try and apply the new patch
        old_state = self.states[-1]
        new_state = patch.apply_patch(old_state)
        if new_state is None:
            raise Exception("Invalid patch to add to branch")
        self.states.append(new_state)
        self.patches.append(patch)

    def curr_state(self):
        return self.states[-1]

    """
    def write_to_file():
        for patch in self.patches:
            for operation in patch:
    """
