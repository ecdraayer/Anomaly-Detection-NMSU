from fileio.data_io import file_reading
# ../data/artificialNoAnomaly/art_daily_no_noise.csv

def file_reading(file_name, data_col=-1, delimiter=',', header=True):
    num = 0
    data_list = []
    with open(file_name) as f:
        data_row = []
        for line in f:
            if header is True:
                header = False
                continue
            num = num + 1
            line = line.strip()
            data_row = line.split(delimiter)
            data_list.append(float(data_row[data_col]))
    return data_list