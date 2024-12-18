from ._anvil_designer import LoginTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
 
    
  def button_1_click(self, **event_args):
      
      user = anvil.users.login_with_form(allow_cancel=False)
      if user:
        open_form('HOME') 