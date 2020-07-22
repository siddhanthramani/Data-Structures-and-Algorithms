//Insertion sort is used to sort an array.

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

    int j;
    for(int i = 1; i < n; i++){
        temp = a[i];
        for(j = i-1; j >= 0; j--){
            if(temp < a[j]){
                a[j+1] = a[j];
            }
            else{
                break;
            }
        }
        a[j+1] = temp;//this cannot be inside else statement before break because, when the j loop condition does not
        //satisfy, we do not come inside to execute the else statement at all
    }
    //displaying the sorted array
    cout << "\nThe sorted array is \n";
    for(int i = 0;i < n; i++){
        cout << a[i];
        cout << "\t";
    }


}
