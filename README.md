# temperature_dataset_generator
script Python yang dimodifikasi untuk mensimulasikan data temperatur suhu dari 5 node sensor suhu dengan jeda waktu 30 menit

Perubahan yang dilakukan:

    Jeda waktu: Jeda waktu diubah dari 5 menit menjadi 30 menit dengan menggunakan datetime.timedelta(minutes=30*i).
    Pembagian data: Node ID diubah menggunakan modulo (i%num_nodes+1) untuk membagi data secara merata ke 5 node. Ini memastikan setiap node memiliki 200 baris data (1000 / 5 = 200).

Penjelasan:

    Script ini menghasilkan 1000 baris data temperatur suhu.
    Setiap baris data memiliki timestamp, node ID, dan temperatur suhu.
    Timestamp dihitung dengan menambahkan 30 menit ke timestamp awal untuk setiap baris data.
    Node ID dihitung dengan menggunakan modulo untuk membagi data secara merata ke 5 node.
    Temperatur suhu dibuat secara acak dalam rentang 20 hingga 28 derajat Celcius.
    Data disimpan ke file CSV dengan nama "dataset_suhu_datacenter.csv".

Tips:

    Anda dapat menyesuaikan rentang temperatur minimum dan maksimum sesuai dengan kebutuhan Anda.
    Anda dapat menambahkan kolom lain ke dataset, seperti kelembaban, tekanan udara, atau status node (aktif/tidak aktif).
    Anda dapat menggunakan format waktu lain yang sesuai dengan kebutuhan Anda.
    Anda dapat menggunakan format file lain untuk dataset, seperti JSON atau XML.
    Anda dapat memvisualisasikan data untuk melihat tren dan pola temperatur suhu di datacenter Anda.

Explanation:

    Timestamp: Each row starts with a timestamp in the format YYYY-MM-DD HH:MM:SS, indicating the date and time when the data was recorded.
    Node ID: The second field is the node ID, which identifies the specific node sensor that recorded the data. In this case, the node IDs are node1, node2, node3, node4, and node5, indicating that there are 5 nodes.
    Temperature: The third field is the temperature value in Celsius. The values are formatted with two decimal places for better readability.

This output represents a sample of the temperature data generated by the script. The actual data will vary depending on the random temperature values generated.

Additional Notes:

    The output can be modified to include additional columns, such as humidity, pressure, or node status.
    The output can be saved in different formats, such as CSV, JSON, or XML.
    The output can be used for various purposes, such as data analysis, visualization, or real-time monitoring.
