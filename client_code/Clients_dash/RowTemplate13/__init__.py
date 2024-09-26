from ._anvil_designer import RowTemplate13Template
from anvil import *
import anvil.server


class RowTemplate13(RowTemplate13Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
