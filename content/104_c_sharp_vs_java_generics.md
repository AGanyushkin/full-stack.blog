Title: C# vs Java: Generics
Date: 2023-02-18 22:00
Category: languages
Tags: java, C#
Author: Andrey G
Status: published
Summary: languages, java, jvm, C#, c sharp, .net, dotnet
Lang: ru
---

[TOC]


Generics - обобщения, обобщенные типы и методы. Возможность создать код (класс или метод) без привязки к конкретным тыпам данных.
Такая реализация имеет обобщенный параметр типа, который используется в реализации и мы должны определнить этот параметр конкретным типом в момент создания класса.


# Как использовать

## в Java

Сделаем обобщенный класс для хранения экземпляра объекта.
Наш контейнер должен уметь предоставить доступ к id хранимого объекта.

```java
class MyСontainer<T> {
    private T value;

    public MyСontainer(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }

    public int getId() throws IllegalStateException {
        if (value == null) throw new IllegalStateException("Container shoujld be initialized.");
        return value.getId();
    }
}

var wrappedObject = new MyСontainer<SomeObject>(someObject);
System.out.println("object id = " + wrappedObject.getId());
```

Здесь `T` - это наш обобщенный тип, определяемый как `SomeObject` при создании инстанса `MyСontainer`.

> Java: нельзя использовать примитивные типы как параметр обобщенной перализации

Еще один пример с вариантами использования

```java
class Base {}
class DomainObject extends Base {}

interface MyInterface<T extends Base> {}

class MyClass implements MyInterface<DomainObject> {
};

class MySecondClass<T extends Base> {

};

var x = new MyClass();
var x = new MySecondClass<DomainObject>();
```

## в С\#

```csharp
interface MyInterface
{
    int getId();
}

class MyСontainer<T>
{
    private T value { get; init; }

    public MyСontainer(T value)
    {
        this.value = value;
    }

    public int getId()
    {
        if (value == null) throw new InvalidOperationException("Container shoujld be initialized.");
        return ((MyInterface) value).getId();
    }
}

var wrappedObject = new MyСontainer<SomeObject>(someObject);
Console.WriteLine($"object id = {wrappedObject.getId()}");
```

> C#: можно использовать int, string, double, bool как параметр обобщенной реализации

Больше примеров C#

```csharp
class Base { }
class DomainObject : Base { }


interface MyCustomInterface<out T, in Q>
{
    T GetMessage(Q message);
}

class MyCustomList1 : MyCustomInterface<string, string>
{
    public string GetMessage(string message)
    {
        return message;
    }
}

class MyCustomList2<T> : MyCustomInterface<T, T>
{
    public T GetMessage(T message)
    {
        return message;
    }
}

var x = new MyCustomList1();
var y = new MyCustomList2<string>();
```

# Raw Types

Если не указывать конкретный тип при создании инстанса, например так `new MyСontainer<>(someObject);`, то мы получим так называемый diamond синтакс. Применяя diamond синтакс мы пологаемся на механизм компилятора, который определит требуемый тип по левой части выражения.

[The Diamond](https://docs.oracle.com/javase/tutorial/java/generics/types.html#diamond) - это `<>` в `MyСontainer<>`.
Такой (diamond) синтаксис следует использовать всегда так как использование например `new MyСontainer(someObject);`
 приведит к менее надежному выводу типов в Java.

В некоторых случаях Java может вывести тип самостоятельно

```java
var wrappedObject = new MyСontainer<SomeObject>(someObject);

MyСontainer<SomeObject> wrappedObject = new MyСontainer<>(someObject);

MyСontainer<SomeObject> wrappedObject = new MyСontainer(someObject);

var wrappedObject = new MyСontainer<>(someObject);

MyСontainer wrappedObject = new MyСontainer<>(someObject);
```

<br />

В __C#__ эта "фича" не поддерживатеся. C# более строг в плане типизации ;)



# Ковариантность, контравариантность и инвариантность

__Ковариантность__: upper bounded, позволяет использовать более конкретный тип, чем заданный изначально

В C# ковариантность реализуется с использованием `out T`.

В Java ковариантность реализуется с использованием `? extends Number`.


__Контравариантность__: lower bounded, позволяет использовать более универсальный тип, чем заданный изначально

В C# ковариантность реализуется с использованием `in T`.

В Java ковариантность реализуется с использованием `? super Number`.

__Инвариантность__: unbounded, позволяет использовать только заданный тип

Если просто о сложном, то - возможностью использовать тип, который находится ниже или выше в иерархии наследования.

<br />


Пример для Java
```Java
class Base {}
class DomainObject extends Base {}

// ковариантность. можем использовать Base и его потомки
class MyCustomList<T extends Base> {}

// контравариантность. можем использовать DomainObject и его предков
// class MyCustomList<T super DomainObject> {} - не допустимо для переменной типа

// инвариантность. можем использовать только DomainObject
class MyCustomList<T> {}
```

Пример для C# немного отличается, так как в C# определение ковариант или контравариант происходит __только__ при определении
класса или интерфейса.

> В C# только interface и delegate могуть иметь ковариантность/контравариантность определения типов
> классы должны быть с инвариантными параметрами тапов

```csharp
class Base {}
class DomainObject : Base {}

// ковариантность. можем использовать Base и его потомки
interface MyCustomList1<out T> {}
class MyCustomList<T> : MyCustomList1<T>
{
}

// контравариантность. можем использовать DomainObject и его предков
interface MyCustomList2<in T> {}

// инвариантность. можем использовать только DomainObject или Base
class MyCustomList3<T> {}
```

# Recursive bound

В Java

```java
<T extends Comparable<T>>
```

В C#

```csharp
<T extends Comparable<T>>
```

# Multiple bounds

В Java

```java
<SomeOne & SomethingElse>
```

# Wildcard syntax

В момент создания инстанса мы должны определить какой тип будет присвоен переменной типа T.
`new List<DomainObject>()`.

В Java у нас есть возможность определить тип не строго. Мы можем сказать, например,
что в нашей коллекции можно использоваться все классы унаследованные от базового и сам базовый класс.

```Java
class Base {}
class DomainObject extends Base {}

// ковариантность. можем использовать Base и его потомки
var pool = new ArrayList<? extends Base>();

// контравариантность. можем использовать DomainObject и его предков
var pool = new ArrayList<? super DomainObject>();

// инвариантность. можем использовать только DomainObject
var pool = new ArrayList<DomainObject>();
```

> Java: из списка `List<? super T>` можно только читать и только `Object`

> Java: в списов `List<? extends Number>` нельзя ничего добавить, кроме `null`

> Java: `List<?>` означает `List<? extends Object>`, так как <?> - это указание возможности подставлять любой _допустимый_ тип,
> а 'любой допустимый' тип наследуется от `Object`. PECS говорит о том что из `<?>` так как это `? extends Object` - можно только читать.

> PECS — Producer Extends Consumer Super:
>
> `<T> void move(List<? super T> dest, List<? extends T> src`

В __С#__ нет механизмов похожих на Wildcard в Java и в этом плане является более строгим.


# Коллекции

Применяя дженерики работа с коллекциями выходит на новый уровень. Теперь (да, уже давно :)) мы можем иметь одну коллекцию которая может работать с разными типами. При создании коллекции мы можем указать с каким типом или типами будет работать коллекция.

Для Java
```java
List<Integer> ints = new ArrayList<Integer>();
// or, for list of strings
List<String> ints = new ArrayList<String>();
// or
List<MyClass> ints = new ArrayList<MyClass>();

// or more complex example
List<Pair<String, Double>> ints = new ArrayList<Pair<String, Double>>();
```

В __C#__ пакет с обобщенными коллекциями находится тут `System.Collections.Generic`, [docs](https://learn.microsoft.com/ru-ru/dotnet/api/system.collections.generic?view=net-7.0)

```csharp
var list = new List<int>();
list.Add(1);
list.Add(2);
```

# Generic Methods

Для Java, обощенный метод будет выглядеть так

```java
public static class Util {
    public static <T> T toDoSomething(Object obj) {
        return (T) obj;
    }
}

Util.<String>toDoSomething(element)
```

Обобщенные методы в C#

```csharp
T Add<T>(T a, T b)
{
    return a + b;
}

// can be used as
int x = Add<int>(1, 2);
```

# Type Erasure

Затирание типов или удаление информации о типах на этапе компиляции.

Java компилирует generics в Object и в рантайм все обобщенные коллекции будут работать с Object и иметь соответствующие касты.

В C# такой механизм не используется. В нем нет необходимости так как C# runtime (dotnet) умеет работать с дженериками
и предоставлять соответствующие гарантии.

# To read

[Constraints on type parameters (C# Programming Guide)](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/constraints-on-type-parameters)
