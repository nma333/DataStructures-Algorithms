#include <stdio.h>

int main()
{
    int arr[5]={8,0,5,18,6};
    printf("Sorted array is:\n");
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            if(arr[j]>arr[j+1]){
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    printf("%d\n",arr[i]);
    }
    return 0;
}


Output:
            Sorted array is:
            0
            5
            6
            8
            18
