import pytest, requests, os
from dotenv import load_dotenv, find_dotenv
from todo_app import app

class StubResponse():
  def __init__(self, fake_response_data):
    self.fake_response_data = fake_response_data

  def json(self):
    return self.fake_response_data

@pytest.fixture
def client(monkeypatch):
  def stub(url, params={}):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    if url == f'https://api.trello.com/1/boards/{test_board_id}/cards':
      fake_response_data = [{
        'id': '1',
        'name': 'test1',
        'idList': os.environ.get('TRELLO_COMPLETED_LIST')
      },{
        'id': '2',
        'name': 'test2',
        'idList': os.environ.get('TRELLO_IN_PROGRESS_LIST')
      },
      {
        'id': '3',
        'name': 'test3',
        'idList': os.environ.get('TRELLO_NOT_STARTED_LIST')
      }]
      return StubResponse(fake_response_data)
    raise Exception(f'Integration test did not expect URL "{url}"')

  monkeypatch.setattr(requests, 'get', stub)
  # Use our test integration config instead of the 'real' version
  file_path = find_dotenv('.env.test')
  load_dotenv(file_path, override=True)
  # Create the new app.
  test_app = app.create_app()
  # Use the app to create a test_client that can be used in our tests.
  with test_app.test_client() as client:
    yield client


def test_index_page(client):
  response = client.get('/')
  assert response.status_code == 200
  page = response.data.decode()
  # check for items
  assert 'test1' in page
  assert 'test2' in page
  assert 'test3' in page

  # check for lists
  assert 'id="not-started"' in page
  assert 'id="in-progress"' in page
  assert 'id="completed"' in page

def test_add_page(monkeypatch, client):
  def stub(url, params={}):
    if url == f'https://api.trello.com/1/cards':
      fake_response_data = {
        'id': '1',
        'name': 'test1',
        'idList': os.environ.get('TRELLO_COMPLETED_LIST')
      }
      return StubResponse(fake_response_data)
    raise Exception(f'Integration test did not expect URL "{url}"')

  monkeypatch.setattr(requests, 'post', stub)
  response = client.post('/add')
  assert response.status_code == 302
  page = response.data.decode()
  
  # check redirect back to index
  assert 'You should be redirected automatically to target URL: <a href="/">/</a>' in page

def test_not_started_page(monkeypatch, client):
  def stub(url, params={}):
    if url == f'https://api.trello.com/1/cards/1':
      fake_response_data = {
        'id': '1',
        'name': 'test1',
        'idList': os.environ.get('TRELLO_NOT_STARTED_LIST')
      }
      return StubResponse(fake_response_data)
    raise Exception(f'Integration test did not expect URL "{url}"')
  
  monkeypatch.setattr(requests, 'put', stub)
  response = client.get('/completed/1')
  assert response.status_code == 302
  page = response.data.decode()
  
  # check redirect back to index
  assert 'You should be redirected automatically to target URL: <a href="/">/</a>' in page

def test_in_progress_page(monkeypatch, client):
  def stub(url, params={}):
    if url == f'https://api.trello.com/1/cards/1':
      fake_response_data = {
        'id': '1',
        'name': 'test1',
        'idList': os.environ.get('TRELLO_IN_PROGRESS_LIST')
      }
      return StubResponse(fake_response_data)
    raise Exception(f'Integration test did not expect URL "{url}"')

  monkeypatch.setattr(requests, 'put', stub)
  response = client.get('/in-progress/1')
  assert response.status_code == 302
  page = response.data.decode()
  
  # check redirect back to index
  assert 'You should be redirected automatically to target URL: <a href="/">/</a>' in page

def test_completed_page(monkeypatch, client):
  def stub(url, params={}):
    if url == f'https://api.trello.com/1/cards/1':
      fake_response_data = {
        'id': '1',
        'name': 'test1',
        'idList': os.environ.get('TRELLO_COMPLETED_LIST')
      }
      return StubResponse(fake_response_data)
    raise Exception(f'Integration test did not expect URL "{url}"')

  monkeypatch.setattr(requests, 'put', stub)
  response = client.get('/completed/1')
  assert response.status_code == 302
  page = response.data.decode()
  
  # check redirect back to index
  assert 'You should be redirected automatically to target URL: <a href="/">/</a>' in page