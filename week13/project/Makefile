# Makefile — Step 3: sqlite3 추가
CC = gcc
CFLAGS = -Wall -g -Iinclude
LDFLAGS_DB = -lsqlite3
OBJDIR = obj

all: sensor_sim ipc_receiver

sensor_sim: $(OBJDIR)/sensor_main.o $(OBJDIR)/sensor.o
	$(CC) $(CFLAGS) -o $@ $^

ipc_receiver: $(OBJDIR)/receiver_main.o $(OBJDIR)/sensor.o
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS_DB)

$(OBJDIR)/%.o: src/%.c | $(OBJDIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJDIR): ; mkdir -p $(OBJDIR) data

clean: ; rm -rf $(OBJDIR) sensor_sim ipc_receiver
