// shm_reader.c — 공유 메모리에서 센서 데이터 읽기
#include <stdio.h>
#include <sys/shm.h>
#include <time.h>
#include <unistd.h>

typedef struct { int id; int value; time_t ts; } SensorData;
#define SHM_KEY 0x1234

int main() {
    int shmid = shmget(SHM_KEY, sizeof(SensorData), 0666);
    SensorData *shm = (SensorData*)shmat(shmid, NULL, SHM_RDONLY);

    int last_id = 0;
    for (int i = 0; i < 20; i++) {
        if (shm->id != last_id) {  // 새 데이터 감지
            printf("[Reader] ID:%d CDS:%d\n", shm->id, shm->value);
            last_id = shm->id;
        }
        usleep(500000);  // 0.5초 폴링
    }

    shmdt(shm);
    shmctl(shmid, IPC_RMID, NULL);  // 공유 메모리 삭제
    return 0;
}
