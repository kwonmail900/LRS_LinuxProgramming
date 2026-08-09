# Makefile for Sensor Simulator
CC = gcc
CFLAGS = -Wall -g -Iinclude
TARGET = sensor_sim
SRCDIR = src
OBJDIR = obj

SRCS = $(SRCDIR)/main.c $(SRCDIR)/sensor.c
OBJS = $(OBJDIR)/main.o $(OBJDIR)/sensor.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

$(OBJDIR)/%.o: $(SRCDIR)/%.c | $(OBJDIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJDIR):
	mkdir -p $(OBJDIR) data

clean:
	rm -rf $(OBJDIR) $(TARGET) data/sensor_data.csv

.PHONY: clean