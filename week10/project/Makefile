CC = gcc
CFLAGS = -Wall -g -Iinclude
TARGETS = sensor_sim ipc_receiver

all: $(TARGETS)

sensor_sim: src/sensor_main.o src/sensor.o
	$(CC) $(CFLAGS) -o $@ $^

ipc_receiver: src/receiver_main.o src/sensor.o
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f src/*.o $(TARGETS) data/sensor_data.csv /tmp/sensor_fifo
