Title: Simple algorithms in C#
Date: 2023-02-14 21:00
Category: languages
Tags: java, C#, algorithms
Author: Andrey G
Status: published
Summary: languages, C#, c sharp, .net, dotnet, algorithms
Lang: en
---

[TOC]

I would like to write some algorithms to train with new knowleges in C#.

All sources, tests, etc...
available here: [https://github.com/AGanyushkin/AlgoTrainer](https://github.com/AGanyushkin/AlgoTrainer)


# Task 1

What we need to do: move all zero elements to the end of the array.

also required:

- without new memory allocations
- save the original sorting

```
[ 0, 7, 3, 0, 1 ] -> [ 7, 3, 1, 0, 0 ]
```

My solution:

Main idea - from left to right, we trying to find '0' (position 1). Then find first non-zero (position 2)
after that position (position 1) and swap position 1 and position 2.

```csharp
public int[] toDo(int[] inputArray)
{
    for (int i = 0; i < inputArray.Length; i++)
    {
        if (inputArray[i] != 0) continue;
        bool hasSwap = false;
        for (int j = i + 1; j < inputArray.Length; j++)
        {
            if (inputArray[j] != 0)
            {
                var tmp = inputArray[i];
                inputArray[i] = inputArray[j];
                inputArray[j] = tmp;
                hasSwap = true;
                break;
            }
        }
        if (!hasSwap) break;
    }
    return inputArray;
}
```

# Task 2

What we need to do: calculate num of characters in sequences.

```
"abbbnnnm" -> "a1b3n3m1"
```

My solution:

Main idea - iterate from left to right. Save current character and increase counter.
if there is new character in input - put result into output and save new state.

```csharp
public string toDo(string inputString)
{
    if (inputString.Length == 0) return "";
    if (inputString.Length == 1) return $"{inputString}1";

    StringBuilder builder = new();
    char current = inputString[0];
    byte counter = 1;

    for(int i = 1; i < inputString.Length; i++)
    {
        if (inputString[i] != current)
        {
            builder
                .Append(current)
                .Append(counter);
            current = inputString[i];
            counter = 1;
        }
        else
        {
            counter += 1;
        }
    }
    builder
        .Append(current)
        .Append(counter);
    return builder.ToString();
}
```

# Task 3

Return TRUE if two string are anagrams of each other.

```
"aba" & "aab" -> true
```

My solution:

Main idea - calculate counters for each character. with "+" from first input and with "-" from second input.
If in result counters we have for all counters `value == 0` it means this is an anograms.

```csharp
public bool toDo(string firstInputString, string secondInputString)
{
    if (firstInputString == secondInputString) return true;
    if (firstInputString.Length != secondInputString.Length) return false;

    Dictionary<char, short> accumulator = new ();

    for (int i = 0; i < firstInputString.Length; i++)
    {
        char ch;

        ch = firstInputString[i];
        if (accumulator.ContainsKey(ch))
            accumulator[ch] += 1;
        else
            accumulator[ch] = 1;

        ch = secondInputString[i];
        if (accumulator.ContainsKey(ch))
            accumulator[ch] -= 1;
        else
            accumulator[ch] = -1;
        }

    foreach(var v in accumulator.Values)
    {
        if (v != 0) return false;
    }
    return true;
}
```

That's all :)