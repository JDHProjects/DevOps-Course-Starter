class ViewModel:
  def __init__(self, items):
    self.items = items
    
  @property
  def completed_items(self):
    return filter(lambda x: x.status == "Completed", self.items)
  
  @property
  def not_started_items(self):
    return filter(lambda x: x.status == "Not Started", self.items)
  
  @property
  def in_progress_items(self):
    return filter(lambda x: x.status == "In Progress", self.items)