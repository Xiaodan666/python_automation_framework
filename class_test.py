class Dog:
    name = None
    breed = None
    age = 0
    sex = 1

    def set_value(self):
        dog_list = []
        dog_data = [{'name': 'wangzai', 'breed': 'bishon', 'age': 5, 'sex': 1},
                    {'name': '123', 'breed': '123', 'age': 3, 'sex': 2},
                    {'name': '444', 'breed': '13', 'age': 3, 'sex': 1}]
        for i in dog_data:
            dog = Dog()
            dog.name=i['name']
            dog.breed=i['breed']
            dog.age=i['age']
            dog.sex=i['sex']
            dog_list.append(dog)
        return dog_list

if __name__ == '__main__':
    # dog = Dog()
    # print(dog.set_value())
    test="123"
    if test:
        print("true")
    else:
        print("false")