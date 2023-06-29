from pprint import pprint
from WordCounter import WordCounter
from TaxMan import TaxMan
from Calculator import Calculator

people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
def ex1():
    def sort_people(list, field, direction):
        if direction == "asc":
            list.sort(key=lambda p:p[field])
        else:
            list.sort(key=lambda p:p[field], reverse=True)

    sort_people(people_list, "age", "dsc")
    print(people_list)
    
    
def ex2():
    def filter_males(list_to_sort):
        new_list = list(filter(lambda p:p["sex"] == "male", list_to_sort))
        return new_list
    print(filter_males(people_list))
    

people_list3 = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]
def ex3():
    def calc_bmi(list_to_map):
        list_of_bmi = list(map(lambda p: 
            { "id": p["id"],
              "name": p["name"],
              "weight":p["weight_kg"],
              "height_meters": p["height_meters"],
              "bmi":round(p["weight_kg"] / p["height_meters"] **2, 1)
            }
            , list_to_map))
        return list_of_bmi
    print(calc_bmi(people_list3))
    
def ex4():
    def get_people(list_of_people):
        list_of_names = [p["name"] for p in list_of_people if p["age"] >= 15]
        return list_of_names
    print(get_people(people_list))
    
def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    print(word_counter.get_word_count()) 
    print(word_counter.get_shortest_word())
    print(word_counter.get_longest_word())
# ex5()

def ex6():
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())
# ex6()


def ex7():
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())
# ex7()