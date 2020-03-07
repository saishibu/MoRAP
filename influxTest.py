#ref: https://www.influxdata.com/blog/getting-started-python-influxdb/
#Note: Works with Python3 only

from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('MoRAPData')


data=[{"measurement":"IR","tags":{"user":1},"fields":{"place":1,"value":1.0}}]

client.write_points(data)


