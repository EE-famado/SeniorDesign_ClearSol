from csv import writer


def csvdata(count, v1, i1, v2, i2, v3, i3, v4, i4):
    header = ['Supercap Input', 'Supercap Output', 'EDS']
    data = [count, v1, i1, v2, i2, v3, i3, v4, i4]

    with open('data.csv', 'a', newline = '') as f_object:
        writer_object = writer(f_object)
    
        writer_object.writerow(data)
        f_object.close()