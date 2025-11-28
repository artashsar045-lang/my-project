""" Գրել MyShows class, որը․
   - __init__ ում կստանա
     -- սերիալի անունը (պետք է լինի տեքստ),
     -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ),
     -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
     -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
     -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
     -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
   - բոլոր ատրիբուտները կլինեն private,
   - կունենա getter բոլոր ատրիբուտների համար,
   - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
   - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
   - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
   - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։"""

class MyShows:
    def __init__(self,name,platform, data, actors_list,rating = None,seria_num = 1):
        self.__name = name
        self.__platform = platform
        self.__data = data
        self.__seria_num = seria_num
        self.__rating = rating
        self.__actors_list = actors_list

        self._is_valid_name_platform(name, platform)
        self._is_valid_data(data)
        self._is_valid_seria_num(seria_num)
        self._is_valid_rating(rating)
        self._is_valid_actors_list(actors_list)

    @staticmethod
    def _is_valid_name_platform(name,platform):
        if not isinstance(name,str) or not isinstance(platform,str):
            raise ValueError("Պետք է լինի տեքստ")

    @staticmethod
    def _is_valid_data(data):
        if not isinstance(data,int):
            raise ValueError("Պետք է լինի ամբողջ թիվ")

    @staticmethod
    def _is_valid_seria_num(seria_num):
        if not isinstance(seria_num, int):
            raise ValueError("Պետք է լինի ամբողջ թիվ")
    @staticmethod
    def _is_valid_rating(rating):
        if not isinstance(rating, int) or not (1 <= rating <= 10):
            raise ValueError("պետք է լինի ամբողջ թիվ 1-10 միջակայքում")
        return rating

    @staticmethod
    def _is_valid_actors_list(actors_list):
        if not isinstance(actors_list, list):
            raise ValueError("Պետք է լինի լիստ")


    @property
    def name(self):
        return self.__name

    @property
    def platform(self):
        return self.__platform

    @property
    def data(self):
        return self.__data

    @property
    def actors(self):
        return self.__actors_list

    @property
    def seria_num(self):
        return self.__seria_num

    @property
    def rating(self):
        return self.__rating

    @seria_num.setter
    def seria_num(self,new_seria):
        self._is_valid_seria_num(new_seria)
        self.__seria_num = new_seria

    @rating.setter
    def rating_change(self,new_rating):
        self._is_valid_rating(new_rating)
        self.__rating = new_rating

    @rating.deleter
    def rating(self):
        self.__rating = None

    def add_actors(self,actors_name):
        if not isinstance(actors_name,str):
            raise ValueError("Պետք է լինի տեքստ")
        self.__actors_list.append(actors_name)

    def remove_actors(self, actors_name):
        if actors_name in self.__actors_list:
            self.__actors_list.remove(actors_name)

    def info(self):
        return self.__name, self.__platform, self.__data,self.__actors_list, self.seria_num, self.__rating


seria = MyShows("Breaking bed","Netflix", 2008, ["Aaron Paul" , "Dean Norris", "Bryan Cranston"], 7)

# seria.seria_num = 8
seria.add_actors("Giancarlo Esposito")
seria.remove_actors("Dean Norris")
del seria.rating
seria.rating_change = 9

print(seria.info())
















