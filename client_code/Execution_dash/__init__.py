from ._anvil_designer import Execution_dashTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server


class Execution_dash(Execution_dashTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
'''
    with anvil.server.no_loading_indicator:
      
      print(anvil.server.call('livePositions'))

    with anvil.server.no_loading_indicator:
      # this is a server function that launches the background task and returns the task object
      self.task = anvil.server.call('livePositions') #background task
      print('done')
'''               
