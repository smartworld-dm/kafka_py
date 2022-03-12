# README #

Kafka test by using Python

### How do I get set up? ###

* Install Java
* Download Kafka

* Build Kafka
```./gradlew jar -PscalaVersion=2.13.6```

* Run Zookeeper
In kafka root folder:
```sh bin/zookeeper-server-start.sh config/zookeeper.properties```

* Kafka server
In kafka root folder:
```sh bin/kafka-server-start.sh config/server.propertie```

* Run consummer
```python  src/consumer.py```

* Run producer
```python src/producer.py```
