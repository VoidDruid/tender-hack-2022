from sentence_transformers import SentenceTransformer, util
mat_model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1') 


def create_embedding(query): 
    query= str(query)
    result = mat_model.encode(query)
    return result


def sort_embedding(query, elastic_result, n_relevant=3):
    query = str(query)
    query_emb = mat_model.encode(query)
    elastic_result_emb = mat_model.encode(elastic_result)
    scores = util.dot_score(query_emb, elastic_result_emb)[0].cpu().tolist()
    doc_score_pairs = list(zip(elastic_result, scores))
    doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)
    result = []
    for i in range(n_relevant):
        result.append(doc_score_pairs[i][0])
    return result
