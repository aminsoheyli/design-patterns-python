# Factory Pattern

Using the `Factory Method Pattern`, we can defer the creation of an object to subclasses.
And this is possible through inheritance.

The `Factory Method Pattern` is one of the most mis-understood patterns. A lot of people don't realize that
the `Factory Method Pattern` relies on inheritance. So using inheritance and polymorphism we're adding flexibility to
this design, we're allowing other developers to change the type of ViewEngine.

The poor way of implementing `Factory Method Pattern` is using static methods like
as `ViewEngineFactory.createViewEngine()` this is not the right way to implement the factory method pattern, because
with this structure we won't be able to change the implementation of the `createViewEngine()` method, because we can not
override static methods.