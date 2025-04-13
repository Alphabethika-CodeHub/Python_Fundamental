from database_connection import DatabaseConnection

server1 = DatabaseConnection()
server2 = DatabaseConnection()

server1.connect()
server2.connect()

server2.disconnect()
server1.disconnect()

server1.tampilkan_log()
server2.tampilkan_log()

print(server1 is server2)