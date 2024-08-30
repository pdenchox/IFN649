import paho.mqtt.publish as publish
publish.single("ifn649", "Hello World", hostname="13.211.148.190")
print("Done")
