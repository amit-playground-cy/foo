import requests

class MyClass:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                print("Success!")
                return response.json()
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    my_obj = MyClass("https://api.github.com")
    my_obj.get_data()