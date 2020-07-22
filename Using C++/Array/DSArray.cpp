/*

An array is used to store multiple values in one variable.

It is very simple but very useful because it can be used to store related data under one variable
instead of creating a lot of variables(takes time to create, hard to work with, confusing to remember all the variables).

ex. If we want to make a list of marks, we would have to create a variable for each students' mark in each subject.
Too many variables(Siddhanth_Math_Mark, Saba_Math_mark....)
With a 2D array we can have all the data in one variable(ex. just one array named mark.)


An array's index starts at 0.
It stores the values in consecutive memory addresses.

The only disadvantage is to update an array in the middle.(Add or delete an element in the middle)


*/

#include<iostream>

using namespace std;

int main(){
    int marks[2][3];// 2D array declaration. Rows are students. Columns are marks in name, math, phy, chem

    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++){

            cout<<"Please enter the marks of ";
            if(i==0 ){
                cout<<"Siddhanth\n";
            }
            else if(i == 1){
                cout<<"Sabareesh\n";
            }
            cin >> marks[i][j];
        }
    }



    //marks = {(100,100,100),(100,99,99)};
}

//marks[0][1] = 100;
//{(100,100,100),(100,99,99)}; //Initializing the array.
