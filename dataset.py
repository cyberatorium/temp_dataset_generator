import random
import datetime
import csv

# Jumlah node sensor suhu
num_nodes = 5

# Rentang temperatur minimum dan maksimum (Celsius)
min_temp = 20
max_temp = 28

# Timestamp awal
start_timestamp = datetime.datetime(2024, 4, 23, 00, 30, 0)

# Buat dataset dengan 1000 baris data
data = []
for i in range(1000):
    # Buat timestamp
    timestamp = start_timestamp + datetime.timedelta(minutes=30*i)

    # Buat node ID
    node_id = f"node{i%num_nodes+1}"

    # Buat temperatur acak (Celsius)
    temperature = random.uniform(min_temp, max_temp)

    # Format temperatur ke string dengan 2 desimal
    formatted_temp = f"{temperature:.2f}"

    # Tambahkan data ke dataset
    data.append([timestamp.strftime("%Y-%m-%d %H:%M:%S"), node_id, formatted_temp])

# Simpan dataset ke file CSV
with open("dataset_suhu_datacenter_celsius.csv", "w", newline="") as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(data)

print("Dataset berhasil disimpan ke file dataset_suhu_datacenter_celsius.csv")
