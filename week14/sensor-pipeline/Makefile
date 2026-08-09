# Makefile — Sensor Pipeline Project
CC = gcc
CFLAGS = -Wall -g -Iinclude
LDFLAGS_DB = -lsqlite3
OBJDIR = obj

TARGETS = sensor_sim ipc_receiver
all: dirs $(TARGETS)

dirs: ; @mkdir -p $(OBJDIR) data

sensor_sim: $(OBJDIR)/sensor_main.o $(OBJDIR)/sensor.o
	$(CC) $(CFLAGS) -o $@ $^

ipc_receiver: $(OBJDIR)/receiver_main.o $(OBJDIR)/sensor.o
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS_DB)

$(OBJDIR)/%.o: src/%.c include/sensor.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJDIR) $(TARGETS) data/*.db data/*.png data/*.json

install-deps:
	pip3 install -r requirements.txt
	sudo apt install -y libsqlite3-dev

run: all
	bash scripts/run_pipeline.sh $(N)

web: all
	bash scripts/run_web.sh $(N)

.PHONY: all clean dirs install-deps run web
