import subprocess
import json

def run_curl(url):
    result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def test_api(url, key_elements):
    response = run_curl(url)
    try:
        json_response = json.loads(response)
        if all(key in json_response for key in key_elements):
            return True, json_response
        else:
            return False, json_response
    except json.JSONDecodeError:
        return False, response

def main():
    tests = [
        {"url": "https://jsonplaceholder.typicode.com/posts/1", "keys": ["userId", "id", "title", "body"]},
        {"url": "https://jsonplaceholder.typicode.com/users/1", "keys": ["id", "name", "username", "email"]},
        {"url": "https://jsonplaceholder.typicode.com/comments/1", "keys": ["postId", "id", "name", "email", "body"]},
    ]

    for i, test in enumerate(tests, 1):
        passed, response = test_api(test["url"], test["keys"])
        if passed:
            print(f"Test {i}: PASSED")
        else:
            print(f"Test {i}: FAILED - Response: {response}")

if __name__ == "__main__":
    main()
