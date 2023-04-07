from todo_app.models.view_model import ViewModel
from todo_app.data.trello_items import Item
import os, pytest

@pytest.fixture(scope='session', autouse=True)
def set_env():
    os.environ['TRELLO_NOT_STARTED_LIST'] = "123"
    os.environ['TRELLO_IN_PROGRESS_LIST'] = "456"
    os.environ['TRELLO_COMPLETED_LIST'] = "789"

def test_completed_items():
    items = [
        Item({"id":0, "name": "test0", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":1, "name": "test1", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":2, "name": "test2", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":3, "name": "test3", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":4, "name": "test4", "idList": os.getenv('TRELLO_COMPLETED_LIST')}),
        Item({"id":5, "name": "test5", "idList": os.getenv('TRELLO_COMPLETED_LIST')})
    ]
    test_view_model = ViewModel(items)
    assert [item.name for item in test_view_model.completed_items] == ["test4", "test5"]

def test_no_completed_items():
    items = [
        Item({"id":0, "name": "test0", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":1, "name": "test1", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":2, "name": "test2", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":3, "name": "test3", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')})
    ]
    test_view_model = ViewModel(items)
    assert [item.name for item in test_view_model.completed_items] == []

def test_only_completed_items():
    items = [
        Item({"id":4, "name": "test4", "idList": os.getenv('TRELLO_COMPLETED_LIST')}),
        Item({"id":5, "name": "test5", "idList": os.getenv('TRELLO_COMPLETED_LIST')})
    ]
    test_view_model = ViewModel(items)
    assert [item.name for item in test_view_model.completed_items] == ["test4", "test5"]

def test_in_progress_items():
    items = [
        Item({"id":0, "name": "test0", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":1, "name": "test1", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":2, "name": "test2", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":3, "name": "test3", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":4, "name": "test4", "idList": os.getenv('TRELLO_COMPLETED_LIST')}),
        Item({"id":5, "name": "test5", "idList": os.getenv('TRELLO_COMPLETED_LIST')})
    ]
    test_view_model = ViewModel(items)
    assert [item.name for item in test_view_model.in_progress_items] == ["test2", "test3"]

def test_no_in_progress_items():
    items = [
        Item({"id":0, "name": "test0", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":1, "name": "test1", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":4, "name": "test4", "idList": os.getenv('TRELLO_COMPLETED_LIST')}),
        Item({"id":5, "name": "test5", "idList": os.getenv('TRELLO_COMPLETED_LIST')})
    ]
    test_view_model = ViewModel(items)
    assert [item.name for item in test_view_model.in_progress_items] == []

def test_only_in_progress_items():
    items = [
        Item({"id":2, "name": "test2", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":3, "name": "test3", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')})
    ]
    test_view_model = ViewModel(items)
    assert [item.name for item in test_view_model.in_progress_items] == ["test2", "test3"]

def test_not_started_items():
    items = [
        Item({"id":0, "name": "test0", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":1, "name": "test1", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":2, "name": "test2", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":3, "name": "test3", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":4, "name": "test4", "idList": os.getenv('TRELLO_COMPLETED_LIST')}),
        Item({"id":5, "name": "test5", "idList": os.getenv('TRELLO_COMPLETED_LIST')})
    ]
    test_view_model = ViewModel(items)
    assert [item.name for item in test_view_model.not_started_items] == ["test0", "test1"]

def test_no_not_started_items():
    items = [
        Item({"id":2, "name": "test2", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":3, "name": "test3", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":4, "name": "test4", "idList": os.getenv('TRELLO_COMPLETED_LIST')}),
        Item({"id":5, "name": "test5", "idList": os.getenv('TRELLO_COMPLETED_LIST')})
    ]
    test_view_model = ViewModel(items)
    assert [item.name for item in test_view_model.not_started_items] == []

def test_only_not_started_items():
    items = [
        Item({"id":0, "name": "test0", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":1, "name": "test1", "idList": os.getenv('TRELLO_NOT_STARTED_LIST')}),
        Item({"id":2, "name": "test2", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":3, "name": "test3", "idList": os.getenv('TRELLO_IN_PROGRESS_LIST')}),
        Item({"id":4, "name": "test4", "idList": os.getenv('TRELLO_COMPLETED_LIST')}),
        Item({"id":5, "name": "test5", "idList": os.getenv('TRELLO_COMPLETED_LIST')})
    ]
    test_view_model = ViewModel(items)
    assert [item.name for item in test_view_model.not_started_items] == ["test0", "test1"]