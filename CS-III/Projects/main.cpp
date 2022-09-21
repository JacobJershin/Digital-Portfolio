#include <limits.h>
#include <stdio.h>
#include <iostream>

void sort(std::string arr[], int N)
{
  int i;
  int min = ;
  for (i = 0; i < N; i++) {
    if (arr[i] < min) {
      min = arr[i];
    }
  }
  printf("The element is %d", min);
  return;
}

int main()
{
  std::string arr[] = { "a", "b" };
  int N = sizeof(arr) / sizeof(arr[0]);
  sort(arr, N);
  return 0;
}
