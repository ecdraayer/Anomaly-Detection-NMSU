import numpy as np

# Run sliding window to convert a time series sequence into a data matrix. One sliding window is one row.
def build_phase_space(ts_list, latent, pattern_length, rate=1):
    tmp_glob = []
    current_seq = [0]*pattern_length
    first = True
    for i in range(int((len(ts_list) - pattern_length - latent)/rate)):
        tmp = []
        it_rate = i*rate
        if first:
            first = False
            for j in range(pattern_length - latent):
                tmp.append(sum(x for x in ts_list[it_rate+j:it_rate+j+latent]))
            tmp_glob.append(tmp)
            current_seq = tmp
        else:
            tmp = current_seq[1:]
            tmp.append(sum(x for x in ts_list[it_rate+pattern_length-latent:it_rate+pattern_length]))
            tmp_glob.append(tmp)
            current_seq = tmp
    #return pd.DataFrame(tmp_glob)
    return tmp_glob

# This is the time-series embedding funtion from VLDB 2019 paper, the PCA is changed to be a online PCA version
def ts_embedding(ts_list, pattern_length=50, latent=None):
    if latent is None:
        latent = pattern_length//3
    min_ts = min(ts_list)
    max_ts = max(ts_list)
    #min_df_r = 1
    #max_df_r = 1000
    df_ref = []
    for i in np.arange(min_ts, max_ts, (max_ts-min_ts)/100):
        tmp = []
        T = [i]*pattern_length
        for j in range(pattern_length - latent):
            tmp.append(sum(x for x in T[j:j+latent]))
        df_ref.append(tmp)

    # df_ref shape is 101 * (l-c), the reason to mantain this matrix is not clear yet
    #df_ref = pd.DataFrame(df_ref)
    # phase_space_1 shape is (n/l) * (l-c), after the convolutional operation
    sliding_matrix = build_phase_space(ts_list, latent, pattern_length)
    print(len(sliding_matrix))
    print(len(sliding_matrix[0]))
    print(np.array(sliding_matrix).shape)
    sdfs

    pca_1 = PCA(n_components=3)
    pca_1.fit(phase_space_1)
    # reduced is (n/l) * 3
    reduced = pd.DataFrame(pca_1.transform(phase_space_1), columns=[str(i) for i in range(3)])
    reduced_ref = pd.DataFrame(pca_1.transform(df_ref), columns=[str(i) for i in range(3)])
    v_1 = reduced_ref.values[0]
    R = get_rotation_matrix(v_1,[0.0, 0.0, 1.0])
    
    A = np.dot(R,reduced.T)
    A_ref = np.dot(R,reduced_ref.T)
    A = pd.DataFrame(A.T,columns=['0','1','2'])