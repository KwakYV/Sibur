def get_temp_td_11():
    data_1 = '0164006ff01700c800c97d000c'
    data = '016300d841b75c0401d855000f'
    value_td = bytes.fromhex(data_1[20:22]) #14:18-temp; 2:4-battery;
    value_td = int.from_bytes(value_td, byteorder='little', signed=True)
    t_td = value_td
    #t_td = value_td / 10
    return t_td

print(get_temp_td_11())