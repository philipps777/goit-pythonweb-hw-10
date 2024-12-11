
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     database_url: str
#     cloudinary_url: str
#     jwt_secret: str
#     jwt_algorithm: str

#     class Config:
#         env_file = ".env"
#         env_file_encoding = 'utf-8'

# settings_instance = Settings()

# # В Pydantic 2.x можно использовать .dict() с параметром 'exclude_unset=True' для вывода значений
# print("Settings initialized:", settings_instance.model_dump())










# from pydantic_settings import BaseSettings
#
# class Settings(BaseSettings):
#     database_url: str
#     cloudinary_url: str
#     jwt_secret: str
#     jwt_algorithm: str
#
#     class Config:
#         env_file = ".env"
#         env_file_encoding = 'utf-8'
#
# print("Settings initialized:", Settings.dict())


# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     database_url: str
#     cloudinary_url: str  
#     jwt_secret: str
#     jwt_algorithm: str

#     class Config:
#         env_file = ".env"
#         env_file_encoding = 'utf-8'

# # Попробуйте напечатать настройки
# settings_instance = Settings()
# print("Settings initialized:", settings_instance.dict())

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    cloudinary_url: str  
    jwt_secret: str
    jwt_algorithm: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Получение настроек через класс
settings = Settings.parse_obj({})
print("Settings initialized:", settings.dict())