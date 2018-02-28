city = {
    '北京': '101010100',
    '海淀': '101010200',
    '朝阳': '101010300'
}

import pickle

pickle_file = open('city_data.pkl', 'wb')
pickle.dump(city, pickle_file)  # dump 倾倒
pickle_file.close()
