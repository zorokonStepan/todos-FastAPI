import requests

from json import dumps


class TestTodo:

    RESPONSE_TIMEOUT = 5

    start_url = "http://127.0.0.1:8000"

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
        response = self.__request(url=f"{self.start_url}/todo")
        assert type(response['todos']) == list

    def test_add_todo(self):
        data = {"id": 1, "item": "First Todo is to finish this book!"}
        response = self.__request(url=f"{self.start_url}/todo", method="POST", json_data=data)
        assert response['message'] == 'TODO added successfully'

        response = self.__request(url=f"{self.start_url}/todo")
        assert len(response['todos']) == 1
        assert response['todos'] == [{'id': 1, 'item': 'First Todo is to finish this book!'}]

    def test_get_single_todo(self):
        data_1 = {"id": 1, "item": "First Todo is to finish this book!"}
        response = self.__request(url=f"{self.start_url}/todo", method="POST", json_data=data_1)
        assert response['message'] == 'TODO added successfully'

        data_2 = {"id": 2, "item": "Second Todo is to finish this book!"}
        response = self.__request(url=f"{self.start_url}/todo", method="POST", json_data=data_2)
        assert response['message'] == 'TODO added successfully'

        response = self.__request(url=f"{self.start_url}/todo/1")
        assert response['todo'] == data_1

        response = self.__request(url=f"{self.start_url}/todo/2")
        assert response['todo'] == data_2

        response = self.__request(url=f"{self.start_url}/todo/3")
        assert response['message'] == "Todo with supplied ID doesn't exist."
