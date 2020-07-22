// a code to sort a 2D array row wise. i.e each row would be sorted using the bubble sort technique

#include<iostream>
#include<stdio.h>

using namespace std;



int main()
{
    int rows, cols;
    cout << "Enter the no of rows : ";
    cin >> rows;
    cout<<"Enter the no of columns : ";
    cin >> cols;

    int tab[rows][cols];

    //creating the array
    for(int i = 0;i < rows; i++){
        for (int j = 0;j < cols;j++){

            cout << "\nEnter the value at row = ";
            cout << i+1;
            cout << " and column = ";
            cout << j+1;
            cout << " : ";
            cin >> tab[i][j];
        }

    }
    //displaying the array
    cout << "The array is \n";
    for(int i = 0;i < rows; i++){
        for (int j = 0;j < cols;j++){
            cout << tab[i][j];
            cout <<"\t";
        }
        cout << "\n";
    }

    //sorting using bubble sort to sort one row (the zero index row)
    int temp; //temporary variable for swapping
    for(int j = 0; j < cols-1; j++){
        for(int i = 0; i < cols-j-1; i++){
            if(tab[0][i] > tab[0][i+1]){
                temp = tab[0][i+1];
                tab[0][i+1] = tab[0][i];
                tab[0][i] = temp;
            }
        }

    }
    //displaying the sorted array of the first row
    cout << "\nThe sorted array is \n";
    for(int i = 0;i < rows; i++){
        for (int j = 0;j < cols;j++){
            cout << tab[i][j];
            cout <<"\t";
        }
        cout << "\n";
    }
    //sorting using bubble sort to sort all the rows
    for (int k = 0; k < rows; k++){//k keeps a count of the rows
        for(int j = 0; j < cols-1; j++){//keeps the count of how many times the loop has to run for every row
            for(int i = 0; i < cols-j-1; i++){//keeps the count of how many swaps has to be done for each row traversal
                if(tab[k][i] > tab[k][i+1]){
                    temp = tab[k][i+1];
                    tab[k][i+1] = tab[k][i];
                    tab[k][i] = temp;
                }
            }
        }
    }
    //displaying the sorted array of all the rows
    cout << "\nThe sorted array of all rows is \n";
    for(int i = 0;i < rows; i++){
        for (int j = 0;j < cols;j++){
            cout << tab[i][j];
            cout <<"\t";
        }
        cout << "\n";
    }



}
