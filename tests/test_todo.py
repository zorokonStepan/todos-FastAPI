import requests

from settings import HOST_URL


class TestTodo:
    RESPONSE_TIMEOUT = 5

    todo_url = f"{HOST_URL}/todo"
    get_todo_item_url = lambda self, item: f"{HOST_URL}/todo/{item}"
    update_todo_item_url = lambda self, item: f"{HOST_URL}/todo/{item}"

    @classmethod
    def __request(cls, url, method="GET", json_data=None):
        try:
            response = requests.request(method,
                                        url,
                                        headers={
                                            "Content-Type": "application/json",
                                        },
                                        timeout=cls.RESPONSE_TIMEOUT,
                                        json=json_data)

            assert response.status_code == 200
            return response.json()

        except AssertionError as exception:
            print(f'{exception = }')
        except Exception as exception:
            print(f'{exception = }')

    def test_retrieve_todos(self):
        response = self.__request(url=self.todo_url)
        assert type(response['todos']) == list

    def test_add_todo(self):
        data = {"id": 1, "item": "First Todo is to finish this book!"}
        response = self.__request(url=self.todo_url, method="POST", json_data=data)
        assert response['message'] == 'TODO added successfully'

        response = self.__request(url=self.todo_url)
        assert len(response['todos']) == 1
        assert response['todos'] == [{'id': 1, 'item': 'First Todo is to finish this book!'}]

    def test_get_single_todo(self):
        data_1, data_2 = self.insert_data()

        response = self.__request(url=self.get_todo_item_url(1))
        assert response['todo'] == data_1

        response = self.__request(url=self.get_todo_item_url(2))
        assert response['todo'] == data_2

        response = self.__request(url=self.get_todo_item_url(3))
        assert response['message'] == "Todo with supplied ID doesn't exist."

    def test_update_todo(self):
        self.insert_data()

        data_1 = {"id": 1, "item": "First Todo UPDATED!"}
        data_2 = {"id": 2, "item": "Second Todo UPDATED!"}
        data_3 = {"id": 3, "item": "Third Todo UPDATED!"}

        response = self.__request(url=self.update_todo_item_url(1), method="PUT", json_data=data_1)
        assert response['message'] == "Todo updated successfully."
        response = self.__request(url=self.get_todo_item_url(1))
        assert response['todo'] == data_1

        response = self.__request(url=self.update_todo_item_url(2), method="PUT", json_data=data_2)
        assert response['message'] == "Todo updated successfully."
        response = self.__request(url=self.get_todo_item_url(2))
        assert response['todo'] == data_2

        response = self.__request(url=self.update_todo_item_url(3), method="PUT", json_data=data_3)
        assert response['message'] == "Todo with supplied ID doesn't exist."

    def insert_data(self):
        data_1 = {"id": 1, "item": "First Todo is to finish this book!"}
        data_2 = {"id": 2, "item": "Second Todo is to finish this book!"}
        self.__request(url=self.todo_url, method="POST", json_data=data_1)
        self.__request(url=self.todo_url, method="POST", json_data=data_2)
        return data_1, data_2


