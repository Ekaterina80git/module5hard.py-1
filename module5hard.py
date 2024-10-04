import time
class User:

    def __init__(self,nickname:str,password:int,age:int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self,title:str,duration:int,adult_mode:bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def play(self):
        return f'воспроизведение видео{self.title} с {self.time_now} секунд.'
    def stop(self):
        return f'видео{self.title} остановлено.'
        self.time_now = 0
    def pause(self):
        return f'видео{self.title} приостановлено на{self.time_now} секунд.'

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title


class UrTube:
    def __init__(self):
        self.users =[]
        self.videos =[]
        self.current_user = None


    def register(self,nickname:str,password:str,age:int):
        for user in self.users:
          if user.nickname == nickname:
            print(f'Пользователь {nickname} уже существует')
            return
        new_user = User(nickname,password,age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None


    def log_in(self,nickname:str,password:str):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname and user.password == User.hash(password):
             self.current_user == user
             return

    def add(self,*args):
        for video in args:
            if video not in self.videos:
             self.videos.append(video)


    def get_videos(self,text:str):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def wath_video(self,title:str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return


        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                 print("Вам нет 18 лет,пожалуйста,покиньте страницу")
                 return


        for i in range(video.duration):
            print(i,end=' ')
            video.time_now += 1
            time.sleep(1)
        
        print('Конец видео')
        video.time_now = 0
        return



if __name__== '__main__':

 ur = UrTube()
 v1 = Video('Лучший язык программирования 2024 года!',200)
 v2 = Video('Для чего девушкам парень програмист?',10,adult_mode=True)
  # добавление видео
 ur.add(v1,v2)

  # проверка поиска
 print(ur.get_videos('лучший'))
 print(ur.get_videos('ПРОГ'))
  # проверка на вход пользователя и возрастное ограничение
 ur.wath_video('Для чего девушкам парень программист?')
 ur.register('vasya_pupkin','lolkekcheburek',13)
 ur.wath_video('для чего девушкам парень программист?')
 ur.register('urban_pythonist','iScX4vIJCIb9YQavjAgF',25)
 ur.wath_video('Для чего девушкам парень программист?')

 # проверка вход в другой аккаунт
 ur.register('vasya_pupkin','F8098FM8fjm9jmi',55)
 print(ur.current_user)
  # попытка воспроизведения несуществующего видео
 ur.wath_video('Лучший язык программирования 2024 года!')






