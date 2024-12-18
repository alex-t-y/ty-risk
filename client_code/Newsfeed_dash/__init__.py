from ._anvil_designer import Newsfeed_dashTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server


class Newsfeed_dash(Newsfeed_dashTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    
    headlines=anvil.server.call('news_headlines_selenium')
    self.repeating_panel_1.items=headlines
    

    comps=self.repeating_panel_1.get_components() 
    
    for n in range(len(headlines)):
      
      if headlines[n]['color']=='red':
        print(n)
        comps[n].background='red'
    

