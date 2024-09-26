from ._anvil_designer import RowTemplate15Template
from anvil import *
import anvil.server


class RowTemplate15(RowTemplate15Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
