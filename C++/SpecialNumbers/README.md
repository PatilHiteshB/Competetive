Rearranging Digits in an Integer

You are given an array of positive integers, arr, of size arr_lenght. Your task is to find the number of special integers in arr.

It is given that an num is considered a special integer if it digits cannot be rearranged in any way to produce an integer larger than num.

Notes:

    - 431 is a special integer, as no other combination of its digits would produce an integer that is larger than 431.
    - 312 is NOT a special integer, as you could rearrange the digits as 321, which would be larger than 312.
    - Any sinlge digit such as 5 is always a special integer.


Input Format:

    - The first line contains an integer, array_length, denoting the number of elements in arr.
    - Each line i of the array_length subsequent lines contains an integer describing arr[i].

Constraints:

    - 1 <= array_length <= 10^5
    - 1 <= arr[i] <= 10^5

Sample Testcases:

Input 1:

    2
    321
    433

Output 1:

    2

Description 1:

    Both 321 & 433 are special, so output is 2.

Input 2:

    2
    312
    431

Output 2:

    1

Description 2:

    312 is not special, but 431 is special, so the output is 1.

