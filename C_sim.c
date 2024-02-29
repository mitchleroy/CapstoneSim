#include <stdio.h>
int main() {
    double testFlow = 20;
    double adjustedFlow;
    int time = 100;
    for (int i = 0; i < time; i++) {
        if (i <= 10) {
            adjustedFlow = testFlow;
            printf("Before 10: %f", adjustedFlow);
            printf("\n");

        } else if (i > 10) {
            adjustedFlow--;
            printf("After 10: %f", adjustedFlow);
            printf("\n");
        }
    }




   return 0;
}