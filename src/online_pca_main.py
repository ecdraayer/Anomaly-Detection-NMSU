from rpca.omwrpca import omwrpca
import numpy as np
def online_pca(M, burnin, win_size, lambda1=np.nan, lambda2=np.nan, factor=1, pca_type=0):
    if pca_type == 0: # use the omvrpca version from rpca.omwrpca
        return omwrpca(M, burnin, win_size, lambda1, lambda2, factor)


if __name__ == "__main__":
    pass
