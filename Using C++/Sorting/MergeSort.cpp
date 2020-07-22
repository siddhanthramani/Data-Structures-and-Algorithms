//Merge sort is used to sort an array.

#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>//stdlib is used for rand and srand functions
#include<time.h>//used for time function

using namespace std;

int main(){

    srand(time(0)); //srand stands for seed rand
    //VERY IMPORTANT  It should be used if we want different values of random number during every run.

    int n,min_value,min_index,temp;
    cout << "Enter size of array : ";
    cin >> n;
    int a[n];

    //creating the array
    for(int i = 0;i < n; i++){
        cout << "\nEnter the value at row = ";
        cout << i+1;
        cout << " : ";
        a[i] = rand();//generates a random number. Will generate the same values during each run if not used with srand
    }
    //displaying the array
    cout << "The array is \n";
    for(int i = 0;i < n; i++){
        cout << a[i];
        cout << "\t";
    }

    int merge_start = 0;
    int merge_end = 5;
    int smerge_mid;
    int smid[3];
    int si = 0;
    while(smerge_mid == merge_start){
        smerge_mid = (merge_end - merge_start) / 2;
        smid[si] = smerge_mid;
        si++;
        merge_end = smerge_mid;
    }
    merge_start = 0;
    merge_end = 5;
    int emerge_mid;
    int emid[3];
    int ei = 0;
    while(emerge_mid == merge_end){
        emerge_mid = (merge_end - merge_start) / 2;
        emid[ei] = emerge_mid;
        ei++;
        merge_start = emerge_mid;
    }

    //displaying the sorted array
    cout << "\nThe sorted array is \n";
    for(int i = 0;i < 3; i++){
        cout << smid[i];
        cout << "\t";
    }
    for(int i = 0;i < 3; i++){
        cout << emid[i];
        cout << "\t";
    }



}
