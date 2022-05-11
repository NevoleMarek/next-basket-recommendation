import numpy as np


def jaccard_rd1(a, b):
    a = set(map(int, a))
    b = set(map(int, b))
    return len(a & b) / len(a | b)


def jaccard_rd2(a, b):
    a = list(map(int, a))
    b = list(map(int, b))
    uniques = set(a) | set(b)
    num, den = 0, 0
    for pid in uniques:
        count_a = a.count(pid)
        count_b = b.count(pid)
        num += min(count_a, count_b)
        den += max(count_a, count_b)
    return num / den


def expl_ratio(order_history, last_n = 1):
    bought = set()
    expl_cnt = 0
    total = 0

    for i, basket in enumerate(order_history):
        basket = list(set(map(int, basket)))
        if len(order_history) - i <= last_n:
            total += len(basket)
        for item in basket:
            if item not in bought:
                if len(order_history) - i <= last_n:
                    expl_cnt +=1
                bought.add(item)

    return expl_cnt / total


def prediction(uid, method, freqs, bskt_size, r_e_ratio, threshold):
    pred_bskt_size = int(np.floor(bskt_size.loc[uid]))

    if method in {'gfreq'}:
        return freqs.head(pred_bskt_size).index.to_list()

    elif method in {'pfreq', 'wpfreq'}:
        if threshold:
            total = freqs.loc[uid]['freq'].sum()
            for count in freqs.loc[uid]['freq'].head(pred_bskt_size):
                if count/total < threshold:
                    pred_bskt_size += -1
        return freqs.loc[uid].head(pred_bskt_size).index.to_list()

    elif method in {'gpfreq'}:
        r_ratio = r_e_ratio.loc[uid, 'repetition']
        e_ratio = r_e_ratio.loc[uid, 'exploration']
        r_bskt_size = int(np.ceil(pred_bskt_size * r_ratio))
        e_bskt_size = int(np.floor(pred_bskt_size * e_ratio))
        r_bskt = freqs[0].loc[uid].head(r_bskt_size).index.to_list()
        e_bskt = freqs[1][freqs[1].index.isin(freqs[0].loc[uid].index.to_list())==False].head(e_bskt_size).index.to_list()
        return r_bskt + e_bskt


def pred(userid, method, freqs, basket_size, r_e_ratio=None, threshold=0):
    return userid.apply(prediction, args=(method, freqs, basket_size, r_e_ratio, threshold))


def evaluate(df, round1=True):
    if round1:
        return df.apply(lambda x: jaccard_rd1(x[0], x[1]), axis=1)
    else:
        return df.apply(lambda x: jaccard_rd2(x[0], x[1]), axis=1)


def dataframe_prediction(test_df, method, freqs, basket_size, r_e_ratio=None, threshold=0):
    return (
        test_df
        .assign(
            pred=lambda x: pred(x['userid'], method=method, freqs=freqs, basket_size=basket_size, r_e_ratio=r_e_ratio, threshold=threshold)
        )
    )


def dataframe_score(test_df):
    return (
        test_df
        .assign(score=lambda x: evaluate(x[['product_id', 'pred']]))
    )['score'].mean()
