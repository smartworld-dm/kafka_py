from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for index in range(10):
	print(f'Sending {index + 1}th message... ')
	producer.send('foobar', bytes(f'{index + 1}', 'utf-8'))
