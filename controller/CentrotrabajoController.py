class CentroTrabajoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        print(self.view.id_e)