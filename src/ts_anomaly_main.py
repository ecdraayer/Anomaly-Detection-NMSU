from online_pca_main import online_pca
from data import file_reading
from ts_embedding import ts_embedding

def anomalyDetection(ts_data):
    return None

# ../data/artificialNoAnomaly/art_daily_no_noise.csv
def main():
    no_anomaly_file = "../data/artificialNoAnomaly/art_daily_no_noise.csv"
    no_anomaly_data = file_reading(no_anomaly_file)
    #print(no_anomaly_data)
    print(len(no_anomaly_data))
    ts_embedding(no_anomaly_data)
    #burnin = 100
    #win_size = 100
    #online_pca(no_anomaly_data, burnin, win_size)

if __name__ == "__main__":
    main()