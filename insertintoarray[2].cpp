#include <stdio.h>
int main() {
    int arr[50], n, pos, num, i;
    printf("Enter how many elements: ");
    scanf("%d", &n);
    printf("Enter %d elements:\n", n);
    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("Enter position to insert ");
    scanf("%d", &pos);
    printf("Enter number to insert: ");
    scanf("%d", &num);
    for(i = n; i >= pos; i--) {
        arr[i] = arr[i - 1];
    }
    arr[pos - 1] = num;
    n++;
    printf("Array after insertion:\n");
    for(i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}

