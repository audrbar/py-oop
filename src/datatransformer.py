class DataTransformer:
    @staticmethod
    def normalization(dataset):
        norm_list: list = list()
        if isinstance(dataset, list):
            min_value = min(dataset)
            max_value = max(dataset)
            for value in dataset:
                tmp = (value - min_value) / (max_value - min_value)
                norm_list.append(tmp)
        return norm_list

    @staticmethod
    def row_encode(secret, encoding='utf-8', errors='replace'):
        return secret.encode(encoding, errors)

    @staticmethod
    def row_decode(secret, decoding='utf-8', errors='replace'):
        return secret.decode(decoding, errors)

    @staticmethod
    def data_filter(dataset: dict, filter_value: int):
        filtered_in = {}
        filtered_out = {}
        for key, value in dataset.items():
            if value > filter_value:
                filtered_in.update({key: value})
            else:
                filtered_out.update({key: value})
        return filtered_in, filtered_out


print(DataTransformer.normalization([2, 4, 6]))
en_sec = DataTransformer.row_encode('Hello')
print(en_sec)
print(DataTransformer.row_decode(en_sec))
print(DataTransformer.data_filter({'price': 2, 'amount': 3, 'sum': 5}, 3))
