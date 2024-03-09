import sender_request
import data

# Нурудинова Ксения 14-я когорта
def test_info_by_track():
    track = sender_request.to_form_order(data.order_body).json()['track']
    response = sender_request.info_by_track(track)
    assert response.status_code == 200 #Тест получения информации по треку