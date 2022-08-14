/*Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
 *
 * Example
 * arr = [1,3,5,7,9]
 * The minimum sum is 1+3+5+7=16 and the maximum sum is 3+5+7+9=24. The function prints 
 * 16 24
 * Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of5  integers

Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.*/

#include <iostream>

using namespace std;

int main()
{
    unsigned long long arr[5], sum[5]= {0,0,0,0,0},max,min;

    for(int i=0;i<5;i++)
    {
       cin>>arr[i];
    }

    for(int i=0;i<5;i++)
    {
        for(int j=0;j<5;j++)
        {
            if( j==i)
            {

            }

            else
            {
                sum[i] = sum[i]+arr[j];
            }
        }
    }

    min = sum[0];
    max = sum[0];
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<5;j++)
        {
            if(max<sum[j])
            {
                max=sum[j];
            }

            if(min>sum[j])
            {
                min=sum[j];
            }
        }
    }

    cout<<min<<" "<<max;

}

