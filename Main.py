import requests


def tests():
    url = "https://jsonplaceholder.typicode.com/posts"
    print(f"URL: {url}")
    main_response = requests.get(url)
    main_json_response = main_response.json()
    max_uid = max(main_json_response, key=lambda ev: ev['userId']).get('userId')
    print(f"Max user Id: {max_uid}")
    max_pid = max(main_json_response, key=lambda ev: ev['id']).get('id')
    print(f"Max post Id: {max_pid}")

    num = input("Choose test:"
                "\n1 - Filtering by user ID"
                "\n2 - Get every post by post ID"
                "\n3 - Get all resources"
                "\nInput number: ")

    if num == "1":
        print("Test 1: Filtering by user ID")
        test_url = url + "?userId="
        err = False
        err_list = []
        for i in range(1, max_uid + 1):
            response = requests.get(test_url + str(i))
            json_response = response.json()
            if json_response:
                print(f"userId={str(i)} OK")
            elif not json_response:
                print(f"userId=={str(i)} Error")
                err = True
                err_list.append(i)
        if not err:
            print("No Errors")
        elif err:
            print("Errors on IDs: ")
            print(*err_list)

    elif num == "2":
        print("Test 2: Get by ID")
        test_url = url + "/"
        # Для пропуска post_id = 0: range(max_pid + 1) -> range(1, max_pid + 1)
        for i in range(max_pid + 1):
            response = requests.get(test_url + str(i))
            code = response.status_code
            assert code == 200, f"ID: {i}; HTTP: {code}"
            print(f"ID:{i} OK {code}")
        print("No Errors")

    elif num == "3":
        print("Test 3: Get all resources")
        response = requests.get(url)
        print(f"GET {url} {str(response.status_code)}")

    else:
        tests()


tests()
