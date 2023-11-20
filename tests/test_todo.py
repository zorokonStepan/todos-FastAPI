import requests


class TestTodo:

    RESPONSE_TIMEOUT = 5

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
        pass
