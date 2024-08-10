# Flyweight Pattern

With this implementation we're storing all icon of a IconType **in a single place in memory**.

So with the `flyweight pattern`:

We need to separate the data that we need to share store it somewhere else in a flyweight class(PointIcon)
and then implement a factory for caching these objects.