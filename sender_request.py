import configuration
import requests

def to_form_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body) #Функция для создания заказа

def info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track)) #Получение информации о заказе