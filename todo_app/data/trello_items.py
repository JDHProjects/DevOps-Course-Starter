import requests
import os

TRELLO_BASE = "https://api.trello.com/1"

class Item:
    def __init__(self, card):
      self.id = card["id"]
      self.name = card["name"]
      self.status_id = card["idList"]
      if self.status_id == os.getenv('TRELLO_NOT_STARTED_LIST'):
        self.status = "Not Started" 
      elif self.status_id == os.getenv('TRELLO_IN_PROGRESS_LIST'):
        self.status = "In Progress"
      else:
        self.status = "Completed"

    def __str__(self):
      return self.name

class Items:
  def __init__(self):
    self.items = self.get_items()

  def _build_params(self, **kwargs):
    """
    Creates param dict with auth.

    Returns:
      dict: The built params dict.
    """
    params = kwargs
    params['key'] = os.getenv('TRELLO_API_KEY')
    params['token'] = os.getenv('TRELLO_TOKEN')
    return params


  def get_items(self):
    """
    Fetches all saved items from the Trello board.

    Returns:
      list: The list of saved items.
    """
    response = requests.request(
      "GET",
      f'{TRELLO_BASE}/boards/{os.getenv("TRELLO_BOARD_ID")}/cards',
      params=self._build_params()
    )

    self.items = [Item(card) for card in response.json()]
    return self.items


  def add_item(self, title):
    """
    Adds a new item with the specified title to the Trello board.

    Args:
      title: The title of the item.
    """
    response = requests.request(
      "POST",
      f"{TRELLO_BASE}/cards",
      params=self._build_params(idList=os.getenv('TRELLO_NOT_STARTED_LIST'), name=title)
    )

    card = response.json()
    self.items.append(Item(card))


  def change_item_list(self, id, list_id):
    """
    Moves an existing item in the Trello board to be part of a different list.

    Args:
      item: The item to update.
    """
    response = requests.request(
      "PUT",
      f'{TRELLO_BASE}/cards/{id}',
      params=self._build_params(idList=list_id)
    )

    card = response.json()
    for item in self.items:
      if item.id == id:
        self.items.remove(item)
        self.items.append(Item(card))
        return 
