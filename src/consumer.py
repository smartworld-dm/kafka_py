from kafka import KafkaConsumer

consumer = KafkaConsumer('foobar', group_id='foobar')

for msg in consumer:
	print (f'Received - {msg.value}')
