from models.user import UserData
from models.support import SupportData

users_data = {1: UserData(id=1, email="george.bluth@reqres.in", first_name="Janet", last_name="George",
                          avatar="https://reqres.in/img/faces/1-image.jpg", job=''),
              2: UserData(id=2, email="janet.weaver@reqres.in", first_name="Janet", last_name="Weaver",
                          avatar="https://reqres.in/img/faces/2-image.jpg", job=''),
              3: UserData(id=3, email="emma.wong@reqres.in", first_name="Emma", last_name="Wong",
                          avatar="https://reqres.in/img/faces/3-image.jpg", job=''),
              4: UserData(id=4, email="eve.holt@reqres.in", first_name="Eve", last_name="Holt",
                          avatar="https://reqres.in/img/faces/4-image.jpg", job=''),
              5: UserData(id=5, email="charles.morris@reqres.in", first_name="Charles", last_name="Morris",
                          avatar="https://reqres.in/img/faces/5-image.jpg", job=''),
              6: UserData(id=6, email="tracey.ramos@reqres.in", first_name="Tracey", last_name="Ramos",
                          avatar="https://reqres.in/img/faces/6-image.jpg", job=''),
              7: UserData(id=7, email="michael.lawson@reqres.in", first_name="Michael", last_name="Lawson",
                          avatar="https://reqres.in/img/faces/7-image.jpg", job=''),
              8: UserData(id=8, email="lindsay.ferguson@reqres.in", first_name="Lindsay", last_name="Ferguson",
                          avatar="https://reqres.in/img/faces/8-image.jpg", job=''),
              9: UserData(id=9, email="tobias.funke@reqres.in", first_name="Tobias", last_name="Funke",
                          avatar="https://reqres.in/img/faces/9-image.jpg", job=''),
              10: UserData(id=10, email="byron.fields@reqres.in", first_name="Byron", last_name="Fields",
                           avatar="https://reqres.in/img/faces/10-image.jpg", job=''),
              11: UserData(id=11, email="george.edwards@reqres.in", first_name="George", last_name="Edwards",
                           avatar="https://reqres.in/img/faces/11-image.jpg", job=''),
              12: UserData(id=12, email="rachel.howell@reqres.in", first_name="Rachel", last_name="Howell",
                           avatar="https://reqres.in/img/faces/12-image.jpg", job=''),
              }

support_data = SupportData(url="https://reqres.in/#support-heading",
                           text="To keep ReqRes free, contributions towards server costs are appreciated!")
