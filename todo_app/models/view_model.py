"""View model for trello items"""

class ViewModel:
  """Filters items in preparation to be displayed."""
  def __init__(self, items):
    self.items = items

  @property
  def completed_items(self):
    """Get completed items."""
    return filter(lambda x: x.status == "Completed", self.items)

  @property
  def not_started_items(self):
    """Get not started items."""
    return filter(lambda x: x.status == "Not Started", self.items)

  @property
  def in_progress_items(self):
    """Get in progress items."""
    return filter(lambda x: x.status == "In Progress", self.items)
