Title: C# vs Java: Declare, instantiate and initialize
Date: 2023-02-18 21:00
Category: languages
Tags: java, C#
Author: Andrey G
Status: published
Summary: languages, java, jvm, C#, c sharp, .net, dotnet
Lang: en
---

[TOC]

In this article, my idea is to illustrate how we can create objects or other structures
inline, in-place, without additional classes, function calls, etc...


# Java

## Literals

Yes, it's so simple, just let's describe all features ;)

```Java
int x = 1;
double y = 2.3;
float z = 3f;
long k = 42L;
String message = "example string";  // and this string will be created in "string pool"
```
> [a bit more about strings and "string pool"](/c-vs-java-sistema-tipov-ru.html#strings)

Also, we can create primitive types in different number systems.
```java
int x = 0b1010;
int y = 0xEFEF;
```

## Array literals

For arrays we also can use literals to quick creation. There is an example how this can be done:
```java
int[] xyz = {1, 1, 1};
double[] xyz = {0.42, 0.0, 0.42};

double[] xyz = new double[] {0.42, 0.0, 0.42};
// or
var xyz = new double[] {0.42, 0.0, 0.42};

var messages = new String[] { "OK", "FAIL", "IN-PROGRESS" };
```

Initialization with literal `int[] xyz = {1, 1, 1};` will create a new array in each execution.

Array literal can be used ONLY with variable declaration, we can't reassign variable with Array literal.
```java
int[] xyz = {1, 1, 1}; // OK
xyz = {1, 1, 1}; // FAIL: "illegal start of expression"
```
But, we can reassign our variable with `new` keyword like this
```java
int[] xyz = {1, 1, 1}; // OK
xyz = new int[] {1, 1, 1}; // OK
```

## Autoboxing

This feature already [was described here](/c-vs-java-sistema-tipov-ru.html#autoboxing-and-unboxing),
but lets show how it can be used to quick creating the wrapper

```java
Integer x = 42;
Double y = 42.0;
Boolean flag = false;
```

## Anonymous class declaration

Anonymous class - it is inner class without name. We can use this types of classes
to extend other classes or implement interfaces.

```java
// en example, how we can use this
var predicate = new Predicate<Integer>() {
    @Override
    public boolean test(Integer integer) {
        return false;
    }
};
```

### extend a class

There is example how we can owerride methods without new classes, in sample below:

```Java
var myInstance = new MyClass("some arguments") {
    @Override
    public String toString() {
        return "Hello world!";
    }
};
```

### implement an interface

To implement interface or abstract class we just use it as:

```java
var myComparator = new Comparator<String>() {
    @Override
    public int compare(String o1, String o2) {
        return 0;
    }

    @Override
    public boolean equals(Object obj) {
        return false;
    }
};
```

### initialize data structure

One interesting application for "anonymous class".

instead of this
```java
var myMap = new HashMap<String, String>();
myMap.put("1", "a");
myMap.put("2", "b");
myMap.put("3", "c");
```
we can create "anonymous class" which based on BaseClass and define initialization block in "anonymous class",
in this initialization block we can call any methods from BaseClass and initialize our instance

```java
var yourMap = new HashMap<String, String>() {{
    put("1", "a");
    put("2", "b");
    put("3", "c");
}};
```

Can we define two or more initialization blocks and override any methods? Yes, sure :)

```Java
var mapp = new HashMap<String, String>() {
    {
        put("1", "a");
    }
    {
        put("2", "b");
    }

    @Override
    public String toString() {
        return "Hello from HashMap ;)";
    }
};
```

### anonymous object with custom fields

Java allows us to construct anonymous objects with fields. It is possible, and can be used for some
data wrapers, if you need to return multiples values from function etc...

```java
var someData = new Object() {
    final String key = "key_data";
    final String value = "value_data";
};
System.out.println(someData.key + ": " + someData.value); // -> "key_data: value_data"
```

<br /><br /><br />

# C\#

## Literals

Very similar to Java. Same code, same description.
Just use `string` instead of `String` in samples.

## Array literals

Very similar to Java. Same code, same description.
Just use `string` instead of `String` in samples.

## Object initialization

I like this initializers in C#. We just write field name and value for this field.
Also we can pass some parameters in constructor, but in additional to constructor initialization
we can ajust instance fields with initializer.

In sample below we can see example how to initialize field with initializer and how to use
initializer with constructor.

```csharp
Cat cat = new Cat { Age = 10, Name = "Fluffy" };
Cat sameCat = new Cat("Fluffy"){ Age = 10 };
```

## Anonymous object initializers

Same as in prevoius section but with out type :).
Here, will be created anonymous object with HashCode, ToString, etc...

```csharp
var pet = new { Age = 10, Name = "Fluffy" };
```

Very useful variant to create data wrappers without dedicated classes, just pass data and use it.

> Anonymous types are class types that derive directly from object,
> and that cannot be cast to any type except object. The compiler provides a
> name for each anonymous type, although your application cannot access it.
> From the perspective of the common language runtime, an anonymous type is no
> different from any other reference type.

## Collection initializer

In Java we have only approach with anonymous classes, but here we can initialize collections as in example:

a bit similar to array literals

```csharp
List<int> digits = new List<int> { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

// or, more complex example. List with objects.

List<Cat> cats = new List<Cat>
{
    new Cat{ Name = "Sylvester", Age=8 },
    new Cat{ Name = "Whiskers", Age=2 },
    null
};
```

For dictionaries we can use initializer for "map"s

```csharp
var numbers = new Dictionary<int, string>
{
    [7] = "seven",
    [9] = "nine",
    [13] = "thirteen"
};

// or

var moreNumbers = new Dictionary<int, string>
{
    {19, "nineteen" },
    {23, "twenty-three" },
    {42, "forty-two" }
};
```

## Array of anonymously typed elements

Here example how we can create array of anonymous elements with anonymous type

```csharp
var anonArray = new[]
{
    new { name = "apple", diam = 4 },
    new { name = "grape", diam = 1 }
};
```

Fewer types, more flexibility. I hope...
