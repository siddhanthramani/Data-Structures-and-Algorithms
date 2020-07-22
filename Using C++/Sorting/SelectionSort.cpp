//Selection sort is used to sort an array.

#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

int main(){

    int n,min_value,min_index,temp;
    cout << "Enter size of array : ";
    cin >> n;
    int a[n];

    //creating the array
    for(int i = 0;i < n; i++){
        cout << "\nEnter the value at row = ";
        cout << i+1;
        cout << " : ";
        cin >> a[i];
    }
    //displaying the array
    cout << "The array is \n";
    for(int i = 0;i < n; i++){
        cout << a[i];
        cout << "\t";
    }

    for(int i = 0; i < n-1; i++){
        min_value = a[i];
        min_index = i; //this is important. If you forget to write this and sorting during some iteration is not required,
        //then, the previous value of 'j' will be stored in this variable leading to false output. Ex n=5, and input 6,5,4,3,2
        //will result in wring output
        for(int j = i+1; j < n; j++){
            if(a[j] < min_value){
                min_value = a[j];
                min_index = j;
            }
        }
        temp = a[i];
        a[i] = min_value;
        a[min_index] = temp;
    }
    //displaying the sorted array
    cout << "\nThe sorted array is \n";
    for(int i = 0;i < n; i++){
        cout << a[i];
        cout << "\t";
    }


}
