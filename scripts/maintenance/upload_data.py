import pickle
import time

from elasticsearch.helpers import bulk

from database.elastic import es

from tqdm import tqdm


def main():
    data_path = 'ds/cte_norm.pickle'
    data = pickle.load(open(data_path, 'rb'))
    len_data = len(data)

    def get_doc(row):
        new_row = {}
        id_cte = row.pop('ID СТЕ')
        new_row["_id"] = id_cte
        new_row["id"] = id_cte
        new_row["name"] = row.pop('Название СТЕ')
        new_row['word_cloud'] = " ".join((str(v) for v in row.values())) + " " + new_row["name"] + row.pop('Категория')
        return new_row

    print("Indexing documents...")

    n = 50
    cons_errs = 0
    for i in tqdm(range(0, len_data, n)):
        try:
            bulk(client=es, index="product", actions=[get_doc(row) for row in data[i:i+n]])
            cons_errs = 0
        except Exception as e:
            if cons_errs >= 3:
                raise
            cons_errs += 1
            time.sleep(3)
