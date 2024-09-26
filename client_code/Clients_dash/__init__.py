from ._anvil_designer import Clients_dashTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server

class Clients_dash(Clients_dashTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    #self.drop_down_1.items=anvil.server.call('get_symbols')
    self.drop_down_1.items=anvil.server.call('request_all_users')
    
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    user=self.drop_down_1.selected_value
    fig,table = anvil.server.call('get_trades',user )
    self.plot_1.figure=fig 
    self.repeating_panel_2.items=table
    self.repeating_panel_1.items=anvil.server.call('user_info',user )
        
         


    

      



     