from ._anvil_designer import RowTemplate16Template
from anvil import *
import anvil.server


class RowTemplate16(RowTemplate16Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
