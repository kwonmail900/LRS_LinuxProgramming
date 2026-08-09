// pipe_sensor.c — 자식이 센서값을 생성하여 부모에게 전달
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>

int main() {
    int pfd[2];
    pipe(pfd);  // 파이프 생성

    if (fork() == 0) {  // 자식 프로세스 (센서)
        close(pfd[0]);  // 읽기 끝 닫기
        srand(time(NULL) ^ getpid());
        for (int i = 0; i < 10; i++) {
            int val = rand() % 4096;
            write(pfd[1], &val, sizeof(int));
            usleep(200000);
        }
        close(pfd[1]);
    } else {            // 부모 프로세스 (수신기)
        close(pfd[1]);  // 쓰기 끝 닫기
        int val;
        while (read(pfd[0], &val, sizeof(int)) > 0)
            printf("[수신] CDS: %d\n", val);
        close(pfd[0]);
        wait(NULL);
    }
    return 0;
}
