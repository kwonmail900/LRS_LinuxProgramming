// shm_writer.c — 센서 데이터를 공유 메모리에 쓰기
#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <time.h>
#include <unistd.h>
#include <string.h>

typedef struct { int id; int value; time_t ts; } SensorData;
#define SHM_KEY 0x1234
#define SHM_SIZE sizeof(SensorData)

int main() {
    int shmid = shmget(SHM_KEY, SHM_SIZE, IPC_CREAT | 0666);
    SensorData *shm = (SensorData*)shmat(shmid, NULL, 0);

    srand(time(NULL));
    for (int i = 1; i <= 20; i++) {
        shm->id = i;
        shm->value = rand() % 4096;
        shm->ts = time(NULL);
        printf("[Writer] ID:%d CDS:%d\n", shm->id, shm->value);
        sleep(1);
    }

    shmdt(shm);
    return 0;
}
