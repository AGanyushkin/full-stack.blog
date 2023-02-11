Title: C# vs Java: Control flow statements
Date: 2023-02-11 21:00
Category: languages
Tags: java, C#
Author: Andrey G
Status: published
Summary: languages, java, jvm, C#, c sharp, .net, dotnet
Lang: ru
---

Сложно найти менее увлекательную тему чем инструкции потока управления.
В этой статье(заметке) я приведу только примеры кода с редкими комментариями если это будет иметь смысл.

Возможно, самая интересная часть этой статьи - это разджел про switch и pattern matching.


# Java: if, if-else, else-if

```java
final int IDEAL_MAGIC_NUMBER = 42;
int magicNumber = 42;

if (magicNumber == IDEAL_MAGIC_NUMBER)
    System.out.println("Hello world!");

if (magicNumber > IDEAL_MAGIC_NUMBER) {
    System.out.println("Hello world!");
}

if (magicNumber > IDEAL_MAGIC_NUMBER) {
    System.out.println("Hello world!");
} else {
    System.out.println("Goodbye");
}

if (magicNumber > IDEAL_MAGIC_NUMBER) {
    System.out.println("Hello world!");
} else if (magicNumber < IDEAL_MAGIC_NUMBER) {
    System.out.println("Bla bla bla");
} else {
    System.out.println("Goodbye");
}
```

# C\#: if, if-else, else-if

```csharp
const int IDEAL_MAGIC_NUMBER = 42;
int magicNumber = 42;

if (magicNumber == IDEAL_MAGIC_NUMBER)
    Console.WrtieLine("Hello world!");

if (magicNumber < IDEAL_MAGIC_NUMBER)
{
    Console.WrtieLine("Hello world!");
}

if (magicNumber >= IDEAL_MAGIC_NUMBER)
{
    Console.WrtieLine("Hello world!");
}
else
{
    Console.WrtieLine("Goodbye");
}

if (magicNumber > IDEAL_MAGIC_NUMBER)
{
    Console.WrtieLine("Hello world!");
}
else if (magicNumber < IDEAL_MAGIC_NUMBER)
{
    Console.WrtieLine("Bla bla bla");
}
else
{
    Console.WrtieLine("Goodbye");
}
```


# Java: switch

```java
int value = 2;
String result;
switch (value) {
    case 2:
    case 3:
        result = "value == 2 or value == 3";
        break;
    default:
        result = "value < 2 and value > 3";
        break;
}
System.out.println(result);
```
`value` может иметь следующий тип: `int`, `byte`, `short`, `char`, `Integer`, `Byte`, `Short`, `Character`, `String`, `Enum`

# Java: switch-выражения

В отличии от оператора, в выражении мы не можем игнорировать ситуацию когда разработчик не определил ветку для `case`.
Компилятор должен проверить все ли значения были учтены разработчиком.
Остается ситуация когда компилятор не может сделать этого и должен быть возвращен null.

```java
int value = 2;
System.out.println(
    switch (value) {
        case 2, 3 -> "value == 2 or value == 3";
        default -> {
            yield "value < 2 and value > 3"
        };
    }
);
```

```java
int value = 2;
System.out.println(
    switch (value) {
        case 2, 3:
            yield "value == 2 or value == 3";
        default:
            yield "value < 2 and value > 3";
    }
);
```

`return` может быть использован только с _оператором_ `switch`, нельзя c _выражением_ `switch`

```java
// OK
String myFanction(int magicNumber) {
    switch (magicNumber) {
        case 2 -> { return "magicNumber == 2"; }
        default -> { return "magicNumber <> 2"; }
    }
}

// FAIL
String myFanction(int magicNumber) {
    String result = switch (magicNumber) {
        case 2 -> { return "magicNumber == 2"; }
        default -> { return "magicNumber <> 2"; }
    }
}

// но вот так - опять можно
String myFanction(int magicNumber) {
    return switch (magicNumber) {
        case 2 -> "magicNumber == 2";
        default -> "magicNumber <> 2";
    }
}
```

Моё субъективное мнение: Java switch-выражения выглядят менее удобными из-за нагромождения разных подходов
и отсутствия pattern matching & when condition.

# C\#: switch

Начиная с 7й версии можно использовать любое non-null выражение внутри case.

```csharp
int value = 2;
string result;
switch (value)
{
    case 2:
    case 3:
        result = "value == 2 or value == 3";
        break;
    default:
        result = "value < 2 and value > 3";
        break;
}
Console.WriteLine(result);
```

Использование с Enum
```csharp
enum MyEnum
{
    Type1,
    Type2,
    Type3
}

var myEnum = (MyEnum) (new Random()).Next(0, 2);

switch (myEnum)
{
    case MyEnum.Type1:
        Console.WriteLine("Type1");
        break;
    case MyEnum.Type2:
        Console.WriteLine("Type2");
        break;
    case MyEnum.Type3:
        Console.WriteLine("Type3");
        break;
}
```

# C\#: switch-выражения

```csharp
string value = "ru";

string result = value switch
{
    "us" => "United States",
    "ru" => "Russian Federation",
    _ => "Unknown"
}

Console.WrtieLine(result);
```

[pattern matching](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/functional/pattern-matching) во всей красе

Null checks - возможность произвести проверку и убедиться что nullable тип != null. Реагировать на null в отдельном бранче

Type tests - проверка на соответствие типу

```csharp
record Point(int X, int Y);
//...

Point point = new(2, 7);

Console.WriteLine(
    point switch
    {
        { X: 0, Y: 0 } => "branch: 0:0",
        { X: var x, Y: var y } when x == 2 => $"branch: Point({x}, {y})",
        null => throw new NullReferenceException("Bla bla bla"),
        var otherValue => $"default branch: {otherValue}"
    }
);
```

`X: var x` - эта конструкция определит переменную `x` для поля `X`, которую мы можем использовать внутри обработчика
бранча или в уточняющем выражении `when x == 2`

Если для объекта задан [deconstruct method](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/functional/deconstruct),
то мы можем не указывать назнание полей а опираться по их позиции. Но и уточнять имена полей тоже можно.

```csharp
record Point(int X, int Y);
//...

Point point = new(2, 7);

Console.WriteLine(
    point switch
    {
        ( 1, 2 ) => "branch: 1:2",
        ( > 0, > 0 ) => "branch: 0:0",
        var otherValue => $"default branch: {otherValue}"
    }
);
```

Возможность анализировать массивы на таком уровне как это показано ниже - это дорогого стоит

```csharp
int[] list = { 1, 2, 3 };

Console.WriteLine(
    list switch
    {
        [1, 3, 4] => "branch: 1, 3, 4",
        [var firstarg, 2, _] when firstarg < 7 => "branch: _, 2, _",
        [.., 42] => "branch: .., 42",
        _ => $"default branch"
    }
);
```


# Java: for, while, do-while, for-each

```java
for(int i = 0; i<=2; i++) {
    System.out.println("i = " + i);
}
```

```java
int i = 0;
while(i<=2) {
    System.out.println("i = " + i);
    i++;
}
```

```java
int i = 0;
do {
    System.out.println("i = " + i);
    i++;
} while (i<=2);
```

```java
String[] myList = {"Str1", "Str2"};

for(String myItem : myList /* collection or Array */){
    System.out.println("myItem = " + myItem);
}
```

# C\#: for, while, do-while, for-each

```csharp
for(int i = 0; i<=2; i++) {
    Console.WriteLine("i = " + i);
}
```

```csharp
int i = 0;
while(i<=2) {
    Console.WriteLine("i = " + i);
    i++;
}
```

```csharp
int i = 0;
do {
    Console.WriteLine("i = " + i);
    i++;
} while (i<=2);
```

```csharp
string[] planets = { "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune" };

foreach (string planet in planets)
{
    Console.WriteLine(planet);
}
```

# Java & C\#: break, continue

`break` и `continue` работают одинаково в обоих языках. Первый позволяет оборвать выполнение цикла,
а второй пропустить оставшуюся часть цикла и перейти к следующей итерации.
