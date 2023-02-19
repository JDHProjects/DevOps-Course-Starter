import requests
import os

TRELLO_BASE = "https://api.trello.com/1"
BOARD_ID = "63dd25f4eaaf087231fa1c44"

class Item:
  def __init__(self, card):
    self.id = card["id"]
    self.name = card["name"]
    self.status_id = card["idList"]
    self.status = "Not Started" if self.status_id == os.getenv('TRELLO_NOT_STARTED_LIST') else "Completed"

  def __str__(self):
    return self.name

def build_params(**kwargs):
  """
  Creates param dict with auth.

  Returns:
    dict: The built params dict.
  """
  params = kwargs
  params['key'] = os.getenv('TRELLO_API_KEY')
  params['token'] = os.getenv('TRELLO_TOKEN')
  return params


def get_items():
  """
  Fetches all saved items from the Trello board.

  Returns:
    list: The list of saved items.
  """
  response = requests.request(
    "GET",
    f'{TRELLO_BASE}/boards/{os.getenv("TRELLO_BOARD_ID")}/cards',
    params=build_params()
  )

  return [Item(card) for card in response.json()]


def add_item(title):
  """
  Adds a new item with the specified title to the Trello board.

  Args:
    title: The title of the item.

  Returns:
    item: The saved item.
  """
  response = requests.request(
    "POST",
    f"{TRELLO_BASE}/cards",
    params=build_params(idList=os.getenv('TRELLO_NOT_STARTED_LIST'), name=title)
  )

  card = response.json()
  return Item(card)


def change_item_list(id, list_id):
  """
  Moves an existing item in the Trello board to be part of a different list.

  Args:
    item: The item to update.
  """
  response = requests.request(
    "PUT",
    f'{TRELLO_BASE}/cards/{id}',
    params=build_params(idList=list_id)
  )

  card = response.json()
  return Item(card)
